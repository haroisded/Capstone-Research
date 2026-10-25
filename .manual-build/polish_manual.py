from pathlib import Path
import json
import re
import ctypes
from ctypes import wintypes
from docx import Document
from docx.shared import Pt
import win32com.client
from PIL import Image

BASE = Path(__file__).resolve().parent
TARGET = BASE.parent / 'User-Manual.docx'
d = Document(TARGET)
d.styles['Normal'].font.name = 'Calibri'
d.styles['Normal'].font.size = Pt(11)
d.styles['Normal'].paragraph_format.space_after = Pt(5)
d.styles['Normal'].paragraph_format.line_spacing = 1.02
d.styles['Heading 2'].paragraph_format.space_before = Pt(10)
d.styles['Heading 2'].paragraph_format.space_after = Pt(5)
for name in ['toc 1', 'toc 2']:
    st = d.styles[name]
    st.font.name = 'Calibri'
    st.font.size = Pt(10)
    st.paragraph_format.space_before = Pt(2 if name == 'toc 1' else 0)
    st.paragraph_format.space_after = Pt(1)
    st.paragraph_format.line_spacing = 1.0
    st.paragraph_format.keep_with_next = name == 'toc 1'
paras = d.paragraphs
for i, p in enumerate(paras):
    if re.match(r'^\d+\. ', p.text) and p.style.name == 'Normal':
        p.paragraph_format.space_after = Pt(3)
        if i + 1 < len(paras) and re.match(r'^\d+\. ', paras[i+1].text) and paras[i+1].style.name == 'Normal':
            p.paragraph_format.keep_with_next = True
    if p.text.startswith('Where:') or p.text.startswith('Who:'):
        p.paragraph_format.keep_with_next = True
    # Slightly compact this short chapter so its conclusion is not isolated.
    if p.text == '12. Set document numbers and receipt appearance':
        compact = True
    elif p.text == '13. Manage your account':
        compact = False
    if 'compact' in locals() and compact and p.style.name == 'Normal':
        p.paragraph_format.space_after = Pt(3)
d.save(TARGET)


def render_emf(data, destination):
    gdi = ctypes.WinDLL('gdi32')
    gdi.SetEnhMetaFileBits.argtypes = [wintypes.UINT, ctypes.c_void_p]
    gdi.SetEnhMetaFileBits.restype = wintypes.HANDLE
    gdi.CreateCompatibleDC.argtypes = [wintypes.HDC]
    gdi.CreateCompatibleDC.restype = wintypes.HDC
    gdi.CreateDIBSection.argtypes = [wintypes.HDC, ctypes.c_void_p, wintypes.UINT, ctypes.POINTER(ctypes.c_void_p), wintypes.HANDLE, wintypes.DWORD]
    gdi.CreateDIBSection.restype = wintypes.HBITMAP
    gdi.SelectObject.argtypes = [wintypes.HDC, wintypes.HANDLE]
    gdi.SelectObject.restype = wintypes.HANDLE
    gdi.PlayEnhMetaFile.argtypes = [wintypes.HDC, wintypes.HANDLE, ctypes.POINTER(wintypes.RECT)]
    gdi.DeleteObject.argtypes = [wintypes.HANDLE]
    gdi.DeleteDC.argtypes = [wintypes.HDC]
    gdi.DeleteEnhMetaFile.argtypes = [wintypes.HANDLE]
    class Header(ctypes.Structure):
        _fields_ = [('size', wintypes.DWORD), ('width', wintypes.LONG), ('height', wintypes.LONG), ('planes', wintypes.WORD), ('bits', wintypes.WORD), ('compression', wintypes.DWORD), ('imagesize', wintypes.DWORD), ('xppm', wintypes.LONG), ('yppm', wintypes.LONG), ('used', wintypes.DWORD), ('important', wintypes.DWORD)]
    w, h = 1240, 1754
    head = Header(40, w, -h, 1, 32, 0, 0, 0, 0, 0, 0)
    payload = ctypes.create_string_buffer(bytes(data))
    emf = gdi.SetEnhMetaFileBits(len(data), payload)
    assert emf, 'Cannot decode EMF'
    dc = gdi.CreateCompatibleDC(None)
    pixels = ctypes.c_void_p()
    bmp = gdi.CreateDIBSection(dc, ctypes.byref(head), 0, ctypes.byref(pixels), None, 0)
    old = gdi.SelectObject(dc, bmp)
    try:
        ctypes.memset(pixels, 255, w*h*4)
        assert gdi.PlayEnhMetaFile(dc, emf, ctypes.byref(wintypes.RECT(0, 0, w, h))), 'Cannot render EMF'
        Image.frombytes('RGB', (w, h), ctypes.string_at(pixels, w*h*4), 'raw', 'BGRX').save(destination)
    finally:
        gdi.SelectObject(dc, old)
        gdi.DeleteObject(bmp)
        gdi.DeleteDC(dc)
        gdi.DeleteEnhMetaFile(emf)


app = win32com.client.DispatchEx('Word.Application')
app.Visible = False
app.DisplayAlerts = 0
doc = None
try:
    doc = app.Documents.Open(str(TARGET), AddToRecentFiles=False)
    doc.Repaginate()
    doc.Fields.Update()
    for toc in doc.TablesOfContents:
        toc.Update()
    doc.Repaginate()
    for toc in doc.TablesOfContents:
        toc.UpdatePageNumbers()
    doc.Save()
    total = doc.ComputeStatistics(2)
    pages = []
    for n in range(1, total+1):
        start = doc.GoTo(What=1, Which=1, Count=n).Start
        end = doc.GoTo(What=1, Which=1, Count=n+1).Start if n < total else doc.Content.End
        txt = doc.Range(start, end).Text
        pages.append({'page': n, 'characters': len(txt.strip()), 'start': txt[:180], 'end': txt[-180:]})
    doc.ExportAsFixedFormat(str(BASE / 'manual-preview.pdf'), 17)
    rendered = []
    render_error = None
    try:
        app.ActiveWindow.View.Type = 3
        # Inspect cover, contents, task instructions, permissions, and the final page.
        samples = sorted({1, 2, 4, 7, 12, 13, 15, 17, 18, total})
        for n in samples:
            bits = doc.ActiveWindow.Panes(1).Pages(n).EnhMetaFileBits
            render_emf(bits, BASE / f'page-{n:02}.png')
            rendered.append(n)
    except Exception as error:
        render_error = str(error)
    report = {'pages': total, 'words': doc.ComputeStatistics(0), 'toc_count': doc.TablesOfContents.Count, 'rendered_pages': rendered, 'render_error': render_error, 'page_texts': pages}
    (BASE / 'final-validation.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k != 'page_texts'}, indent=2))
    print('Short body pages:', [p for p in pages if p['page'] > 3 and p['characters'] < 400])
finally:
    if doc is not None:
        doc.Close(SaveChanges=False)
    app.Quit()
