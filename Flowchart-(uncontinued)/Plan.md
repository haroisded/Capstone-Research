\## Goal and required sources



Create editable flowcharts for the research paper in the existing Uel ERD document (https://lucid.app/lucidchart/c56b9f9a-911b-4161-8082-0d547b3b4f50/edit), using one shared canvas with a separate titled area for each workflow.



Before creating any flowchart, the implementing AI must read both files completely:



\- C:\\Users\\uel36\\OneDrive\\Desktop\\Research Paper\\Capstone-Research\\Flowchart\\current-system-features.md

\- C:\\Users\\uel36\\OneDrive\\Desktop\\Research Paper\\Capstone-Research\\Flowchart\\Flowchart-Best-Practices.pdf



The Markdown supplies the system behavior. The PDF supplies the required flowchart structure, symbols, format, and practices. Follow both strictly.



Show user actions, system responses, relevant decisions, validation, permissions, and outcomes. Summarize internal processing. Research-paper descriptions are outside this session. The user will take the screenshots.



\## Workflow order



Follow the numbered order below. Every numbered item is a separate stopping point, including items sharing a table row.



| Stage | Workflows in exact order |

|---|---|

| Entry and store setup | 01. Sign-in and legal pages; 02. Home: browse and open stores; 03. Store Creation Form; 04. Store side menu and in-store Home |

| Store customization and learning | 05. Change Store Level; 06. Features: customize menu visibility; 07. Store Guide: select a role and practise |

| Staff access | 08. Generate and manage access codes; 09. Enter Access Code; 10. Approve or decline access requests; 11. Revoke member access |

| Staff management | 12. Employees: find and select an employee; 13. Create, edit, and delete roles; 14. Assign an employee’s role and permission exceptions; 15. Read and act on notifications |

| Store and accounting configuration | 16. Chart of Accounts; 17. Store settings; 18. Fiscal Years; 19. Global Defaults; 20. System Settings; 21. Currency; 22. Accounts Settings; 23. Modes of Payment |

| Stock configuration | 24. Warehouses; 25. UOMs; 26. UOM Conversion Factors; 27. Price Lists; 28. Brands; 29. Item Groups; 30. Stock Settings |

| Tax configuration | 31. Tax Categories; 32. Sales Taxes and Charges Templates, including Test Template; 33. Item Tax Templates; 34. Tax Rules, including Which Template? |

| Selling and receipt configuration | 35. Selling Settings; 36. Pricing Rules; 37. Document Naming Settings; 38. Letter Heads; 39. Print Formats; 40. Print Settings; 41. POS Profiles |

| Products and inventory | 42. Items; 43. Scan Product; 44. Item Prices; 45. Import Items; 46. Stock Entries; 47. Stock Reconciliations |

| Selling | 48. Sell index and Open Session; 49. Register: search and add items; 50. Scan to Sell; 51. Cart, payment, and Complete Order |

| Sales and shift follow-up | 52. Orders and sale receipt; 53. Return and refund; 54. Cancel/void a sale; 55. Close Session; 56. Review POS Opening Entries; 57. Review POS Closing Entries |

| Reports | 58. Stock Balance; 59. Stock Ledger; 60. General Ledger; 61. Dashboard |

| Account and store maintenance | 62. Account settings and sign-out; 63. Delete one or multiple owned stores |



This sequence covers all 22 source groups. Shared behavior is referenced rather than redrawn: permission rules apply throughout; scanning has dedicated flows; opening and closing sessions each have their own flow.



Only document behavior supported by the source. For example, do not invent a working Themes feature or an account-deletion procedure from the presence of a button.



\## Diagram structure and Lucid implementation



\- Use Lucid MCP to edit document ID c56b9f9a-911b-4161-8082-0d547b3b4f50. Inspect its current content before each addition.

\- Read Lucid’s required MCP instructions and its diagram-layout and flowchart guidance. Use the document’s available canvas-editing and shape-library APIs to create editable shapes.

\- Title each area FC-01 — Sign-in and Legal Pages, continuing with stable sequential IDs.

\- Arrange completed workflow areas vertically down the shared canvas, with clear whitespace between them. Keep each independently screenshot-ready. Add new areas below existing content without moving finished figures.

\- Default to white backgrounds, black outlines and text, a consistent readable font, and top-to-bottom flow. These are project presentation defaults; preserve the PDF’s required symbol proportions.

\- Use the PDF’s process, input/output, decision, terminal, and connector symbols according to their defined meanings. Use specialized symbols only where appropriate.

\- Label every decision exit. Use open arrowheads, including on reverse-direction loops. Keep crossings distinguishable from junctions and avoid crossings where practical.

\- Follow the PDF’s identification and cross-reference placement rules. For detailed flows elsewhere in this same set, use its striping/reference convention rather than treating all references as predefined processes.

\- When a workflow needs multiple screenshot panels, label them FC-XX-A, FC-XX-B, and connect them using matching connector identifiers. Finish those panels as one workflow before stopping.

\- Keep labels concise. Use annotations for necessary conditions rather than stretching symbols or crowding them with paragraphs.



\## Repeatable process and stopping rule



For each workflow:



1\. Re-read its source section and related rules. Identify the actor, entry point, actions, decisions, outcomes, and documented alternative paths.

2\. Resolve general statements against explicit conditions. Examples include store-level defaults, negative-stock permissions, receipt settings, and the distinction between hidden screens and access permissions.

3\. If an essential behavior remains undocumented or contradictory, ask a focused question before drawing that part. Do not silently invent behavior.

4\. Create only the current workflow’s titled Lucid area.

5\. Validate the connections and visually inspect the rendered diagram. Fix overlaps, clipped labels, unclear branches, and unreadable spacing.

6\. Record its ID, source sections, Lucid area/item identifiers, completion status, and next workflow in Capstone-Research\\Flowchart\\flowchart-progress.md.

7\. Report: “FC-XX — \[workflow] is finished and ready for your screenshot. Next is FC-YY — \[workflow]. I’ll wait for you to continue.”

8\. Stop. Do not create the next workflow until the user explicitly continues. If revisions are requested, finish them before advancing.



On resumption, inspect both the progress record and the Lucid canvas to avoid duplicates. Completion means the diagram is checked and ready; it does not mean the user has already captured its screenshot.



\## Acceptance checks and first deliverable



Before marking a workflow finished, confirm:



\- Its behavior matches the feature file, including relevant permissions and level-dependent rules.

\- Every branch reaches a valid outcome, continuation, or explicit loop.

\- It follows the PDF’s symbol shapes, proportions, flow direction, labels, and reference conventions.

\- The current workflow is readable when framed alone for a research-paper screenshot.

\- Previously completed workflows remain intact.

\- No research-paper description has been written.



First deliverable: FC-01 — Sign-in and Legal Pages. Show the sign-in screen, optional reading of either legal page and return, and selection of Google or Facebook sign-in. Keep authentication internals summarized; do not invent provider-specific screens or undocumented error handling. After validation, report completion and wait before beginning FC-02.

