"""Generate the architecture section. Requires PyMuPDF and Windows Garamond fonts."""

from pathlib import Path
import math
import os
import sys

try:
    import pymupdf as pdf
except ImportError:
    sys.path.insert(0, str(Path(os.environ['TEMP']) / 'merchant-pdf-inspection'))
    import pymupdf as pdf


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / 'Merchant-Software_Architecture.pdf'
FONTS = Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts'
DOC = pdf.open()
BODY = pdf.Font(fontfile=str(FONTS / 'GARA.TTF'))
ITALIC = pdf.Font(fontfile=str(FONTS / 'GARAIT.TTF'))
BLACK = (0, 0, 0)


def new_page():
    page = DOC.new_page(width=595.25, height=842)
    for name, filename in [('Garamond', 'GARA.TTF'), ('GaramondBold', 'GARABD.TTF'),
                           ('GaramondItalic', 'GARAIT.TTF')]:
        page.insert_font(fontname=name, fontfile=str(FONTS / filename))
    return page


def label(page, rect, text, size=8, bold=False):
    """Center compact diagram text using baseline placement."""
    font = 'hebo' if bold else 'helv'
    lines = text.split('\n')
    leading = size * 1.3
    baseline = (rect[1] + rect[3]) / 2 - (len(lines) - 1) * leading / 2 + size * .34
    for line in lines:
        width = pdf.get_text_length(line, fontname=font, fontsize=size)
        assert width <= rect[2] - rect[0] - 4, (line, width, rect)
        page.insert_text(((rect[0] + rect[2] - width) / 2, baseline), line,
                         fontname=font, fontsize=size, color=BLACK)
        baseline += leading


def box(page, rect, text=None, size=8, bold=False, dashed=False):
    page.draw_rect(pdf.Rect(rect), color=BLACK, width=.8,
                   dashes='[3 2] 0' if dashed else None)
    if text:
        label(page, rect, text, size, bold)


def arrow(page, start, end, both=False, dashed=False):
    page.draw_line(start, end, color=BLACK, width=1,
                   dashes='[3 2] 0' if dashed else None)
    def head(tip, other):
        angle = math.atan2(other[1] - tip[1], other[0] - tip[0])
        points = [pdf.Point(tip),
                  pdf.Point(tip[0] + 5 * math.cos(angle + .42), tip[1] + 5 * math.sin(angle + .42)),
                  pdf.Point(tip[0] + 5 * math.cos(angle - .42), tip[1] + 5 * math.sin(angle - .42))]
        shape = page.new_shape()
        shape.draw_polyline(points + [points[0]])
        shape.finish(color=BLACK, fill=BLACK, width=.5)
        shape.commit()
    head(end, start)
    if both:
        head(start, end)


def diagram(page):
    # Match the reference figure's bounding box and monochrome visual language.
    box(page, (136.2, 121.25, 459.1, 639.29))
    label(page, (148, 128, 447, 143), 'Tier 1: Mobile Client', 9, True)
    box(page, (148, 147, 447, 340))
    label(page, (158, 151, 437, 166), 'Phone and tablet application (Android / iOS)', 8)
    box(page, (160, 171, 435, 207))
    page.draw_line((160, 189), (435, 189), width=.65)
    page.draw_line((297.5, 171), (297.5, 207), width=.65)
    label(page, (160, 171, 297.5, 189), 'React Native + Expo')
    label(page, (297.5, 171, 435, 189), 'React + Expo Router')
    label(page, (160, 189, 297.5, 207), 'React Native Paper')
    label(page, (297.5, 189, 435, 207), 'Zustand')
    box(page, (160, 215, 435, 238), 'expo-secure-store: Keychain / Keystore', 8)
    box(page, (160, 246, 435, 301))
    label(page, (166, 248, 429, 264), 'Product label recognition (on device)', 8, True)
    box(page, (167, 271, 236, 292), 'Camera / photo', 7)
    box(page, (253, 271, 342, 292), 'Google ML Kit OCR', 7)
    box(page, (359, 268, 428, 296), 'Item fields\nUser review', 7)
    arrow(page, (236, 281.5), (253, 281.5))
    arrow(page, (342, 281.5), (359, 281.5))
    label(page, (160, 309, 435, 332), 'Supabase client: authenticated service requests', 8)

    # Providers are outside both numbered tier boundaries; dashed edges denote integration.
    box(page, (148, 370, 266, 413), dashed=True)
    label(page, (151, 373, 263, 393), 'External identity providers', 7.6)
    label(page, (151, 393, 263, 410), 'Google | Facebook', 8, True)
    arrow(page, (207, 340), (207, 370), both=True, dashed=True)
    label(page, (148, 347, 201, 361), 'Sign-in', 7)
    arrow(page, (207, 413), (207, 477), both=True, dashed=True)
    label(page, (148, 419, 205, 439), 'Auth\nintegration', 6.8)
    arrow(page, (433, 340), (433, 467), both=True)
    label(page, (279, 375, 424, 407), 'HTTPS\nREQUEST / RESPONSE', 8, True)

    label(page, (148, 445, 447, 462), 'Tier 2: Supabase Backend', 9, True)
    box(page, (148, 467, 447, 625))
    box(page, (160, 477, 435, 526))
    page.draw_line((291, 477), (291, 526), width=.65)
    label(page, (160, 479, 291, 522), 'Supabase Auth\nIdentity and sessions', 8)
    label(page, (291, 479, 435, 522), 'REST API / PostgREST\nData access and RPC', 8)
    arrow(page, (225, 526), (225, 550), both=True)
    arrow(page, (363, 526), (363, 550), both=True)
    box(page, (166, 550, 429, 613))
    label(page, (170, 553, 425, 569), 'PostgreSQL Database', 8.5, True)
    label(page, (170, 573, 425, 590), 'auth.users | profiles | merchants', 8)
    label(page, (170, 594, 425, 609), 'RLS policies | SQL functions | Triggers', 7.7)


PARAGRAPHS = [
    'This illustrates the 2-Tier Software Architecture of the Mobile Merchant System. '
    'The architecture consists of the Mobile Client Tier and the Supabase Backend Tier. '
    'The application communicates directly with managed backend services through HTTPS, '
    'without a separate custom application server. Authentication, API access, and database '
    'storage are shown as components within the backend tier. Google and Facebook are '
    'external identity providers and are not counted as additional application tiers.',

    'The Mobile Client Tier provides the interface and application interactions on Android '
    'and iOS phones and tablets. React Native and Expo support the native application, '
    'while React, Expo Router, and React Native Paper provide screen composition, navigation, '
    'and interface components. Zustand manages session state, and expo-secure-store retains '
    'session information using the device Keychain or Keystore. Google sign-in uses the '
    'native sign-in interface, while Facebook authentication uses the system browser and '
    'returns to the application through its registered deep link.',

    'Google ML Kit OCR operates within the Mobile Client Tier to recognize text from '
    'product-label photographs captured by the camera or selected from the device. The '
    'recognized text is used to populate applicable item fields for user review before '
    'saving. Text recognition runs locally on the phone and does not require a remote '
    'OCR server. This component therefore remains part of the client tier, while saving '
    'records to Supabase requires communication with the backend.',

    'The Supabase Backend Tier provides authentication, data access, and persistent storage. '
    'Supabase Auth verifies sign-in credentials and manages authenticated sessions. The '
    'REST API, implemented through PostgREST, exposes permitted data operations and database '
    'function calls to the application. PostgreSQL stores authentication records, user '
    'profiles, and merchant records. Row-Level Security policies enforce access restrictions, '
    'while SQL functions and triggers support profile creation, merchant access checks, '
    'and account deletion. The mobile client sends authenticated requests to the managed '
    'services, which interact with the database and return results. This arrangement '
    'separates local interaction and recognition from centralized identity, authorization, '
    'and data management.'
]


def body_text(page):
    y = 688.25
    for paragraph in PARAGRAPHS:
        words = paragraph.split()
        first_line = True
        while words:
            if y > 749.5:
                page = new_page()
                y = 82.25
            x = 108.05 if first_line else 72
            available = 526 - x
            line = []
            while words and BODY.text_length(' '.join(line + [words[0]]), fontsize=12) <= available:
                line.append(words.pop(0))
            assert line, 'A word exceeds the body column width'
            if words and len(line) > 1:
                # Justify all but the last line of each paragraph.
                lengths = [BODY.text_length(word, fontsize=12) for word in line]
                gap = (available - sum(lengths)) / (len(line) - 1)
                for word, width in zip(line, lengths):
                    page.insert_text((x, y), word, fontsize=12, fontname='Garamond')
                    x += width + gap
            else:
                page.insert_text((x, y), ' '.join(line), fontsize=12, fontname='Garamond')
            first_line = False
            y += 20.25
        y += 8.1


def main():
    page = new_page()
    page.insert_text((72, 82.25), '3.2 Software Architecture',
                     fontname='GaramondBold', fontsize=12)
    diagram(page)
    caption = 'Figure 3.1.1: 2-Tier Software Architecture Diagram'
    width = ITALIC.text_length(caption, fontsize=10)
    page.insert_text(((595.25 - width) / 2, 661.75), caption,
                     fontname='GaramondItalic', fontsize=10)
    body_text(page)
    assert len(DOC) == 2, f'Expected two pages, got {len(DOC)}'
    DOC.set_metadata({'title': 'Mobile Merchant - Software Architecture',
                      'subject': 'Two-tier mobile application architecture with on-device OCR',
                      'creator': 'Mobile Merchant architecture document generator'})
    DOC.subset_fonts()
    DOC.save(str(OUTPUT), garbage=4, deflate=True)
    print(f'Created {OUTPUT} ({len(DOC)} pages)')


if __name__ == '__main__':
    main()
