# Architecture source notes

The deliverable is `Merchant-Software_Architecture.pdf`. Its layout follows the supplied
`02_3.2_Software_Architecture.pdf`: two A4 pages, Garamond prose, section 3.2,
centered monochrome diagram, and italic figure caption. The diagram and text are newly drawn
and written for Mobile Merchant. `build_merchant_architecture.py` reproduces the document
using PyMuPDF and the installed Garamond font files.

## System evidence and architecture decision

- `tech-stack.txt` supplies the mobile and backend technology descriptions. It is a scaffold
  description, not a complete inventory of the current application's business tables.
  The database names in the diagram are the ones explicitly documented there.
- The user explicitly added the implemented Google ML Kit OCR capability and selected two tiers.
- `../Flowchart/current-system-features.md`, section 18, confirms on-device label recognition,
  camera/photo input, populated item fields, and review before saving. Only the OCR-related
  information supplements the requested stack source.
- [Supabase Data REST API](https://supabase.com/docs/guides/api) explicitly calls direct client
  access to its managed Data API a two-tier architecture. The PDF uses this application-level
  view, grouping managed services and PostgreSQL in the backend tier; it does not claim that
  all Supabase processes occupy one machine or constitute one internal service.
- [Supabase Auth architecture](https://supabase.com/docs/guides/auth/architecture) distinguishes
  the client SDK, API gateway, Auth service, and PostgreSQL. The PDF summarizes those backend
  responsibilities without adding an undocumented custom server or unused Supabase products.
- [Google ML Kit Text Recognition](https://developers.google.com/ml-kit/vision/text-recognition/v2)
  describes recognition of text and its structure for document and product data entry.

## Requested reference-link review

The following supplied sources were accessible and reviewed for separation of presentation,
services, and persistence responsibilities. Their ASP.NET technologies were not transferred
to Mobile Merchant:

- [Creating N-Tier ASP.NET Web API application](https://weblogs.asp.net/sukumarraju/creating-n-tier-web-api-application/).
- [ASP.NET N-Layered Applications — Introduction](https://imar.spaanjaars.com/573/aspnet-n-layered-applications-introduction-part-1).
- [DBMS Architecture](https://www.tutorialspoint.com/dbms/dbms_architecture.htm).
- The original MSDN `bb384570` URL could not be fetched. The accessible current Microsoft
  [N-tier data applications overview](https://learn.microsoft.com/en-us/visualstudio/data-tools/n-tier-data-applications-overview?view=vs-2022)
  was consulted as a related replacement, alongside its
  [N-tier architecture guidance](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/n-tier).

The following links were attempted but could not be reviewed because their content was
unavailable through the retrieval tool. They are not represented as verified sources:

- `https://stackify.com/n-tier-architecture/` — repeated fetch timeouts.
- `https://www.guru99.com/n-tier-architecture-system-concepts-tips.html` — HTTP 403.
- `https://www.tutorialspoint.com/software_architecture_design/distributed_architecture.html` — inaccessible.
- `https://dotnetdaily.net/featured/n-tier-architecture-asp-net` — inaccessible.
- `https://www.c-sharpcorner.com/article/n-layered-architecture-using-entity-framework-generic-repository-and-unit-of-wo/` — fetch/cache failure.

These research notes are separate from the PDF to preserve the reference section's presentation.
