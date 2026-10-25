## Goal and required source

Create one editable Entity–Relationship Diagram (ERD) for the research paper in the existing [Uel ERD document](https://lucid.app/lucidchart/c56b9f9a-911b-4161-8082-0d547b3b4f50/edit), using one shared canvas with a separate titled area for each database section. These areas are organizational groups within one connected database diagram. Relationships must remain physically connected across area boundaries wherever the SQL declares them.

## ERD section order

Follow the numbered order below

| ID | ERD section | Primary tables in `public` |
|---|---|---|
| ERD-01 | Accounts and store foundation | `profiles`, `merchants`, `countries`, `currency_presets` |
| ERD-02 | Store feature preferences | `feature_preferences` |
| ERD-03 | Staff access and notifications | `access_codes`, `access_requests`, `merchant_members`, `notifications` |
| ERD-04 | Roles and permissions | `roles`, `permissions`, `role_grants`, `member_overrides`, `permission_rules`, `doctypes` |
| ERD-05 | Accounting and fiscal years | `accounts`, `fiscal_years`, `gl_entries` |
| ERD-06 | Store configuration | `global_defaults`, `system_settings`, `accounts_settings`, `selling_settings`, `stock_settings`, `print_settings` |
| ERD-07 | Currency and payment methods | `currencies`, `modes_of_payment` |
| ERD-08 | Stock configuration | `warehouses`, `uoms`, `uom_conversion_factors`, `brands`, `item_groups` |
| ERD-09 | Tax configuration | `tax_categories`, `tax_presets`, `sales_tax_templates`, `sales_tax_template_rows`, `item_tax_templates`, `item_tax_template_rows`, `tax_rules` |
| ERD-10 | Price lists and pricing rules | `price_lists`, `pricing_rules`, `pricing_rule_targets` |
| ERD-11 | Document naming and receipt configuration | `naming_series`, `naming_series_counters`, `letter_heads`, `print_formats` |
| ERD-12 | POS profiles | `pos_profiles`, `pos_profile_users`, `pos_profile_item_groups`, `pos_profile_payments` |
| ERD-13 | Items and item-level configuration | `items`, `item_uoms`, `item_taxes`, `item_group_taxes`, `item_prices` |
| ERD-14 | Inventory balances and transactions | `bins`, `stock_entries`, `stock_entry_items`, `stock_reconciliations`, `stock_reconciliation_items`, `stock_ledger_entries` |
| ERD-15 | POS opening sessions | `pos_opening_entries`, `pos_opening_entry_balances` |
| ERD-16 | Sales invoices and returns | `pos_invoices`, `pos_invoice_items`, `pos_invoice_payments`, `pos_invoice_taxes` |
| ERD-17 | POS closing sessions | `pos_closing_entries`, `pos_closing_entry_payments` |

# instructions
- Lines are strictly only Limited to
  Horizontal and Vertical
- Use Proper Relationships
- The Lines must not go through the table
- Lines can Only intertwine, when they point
  to the same Key
  ( other wise, add the most minimal spacing for each of them )
- Tables are grouped based on ERD-*number, so meaning each ERD-*number has a group
  of tables

  now say two ERDs has tables that are related to one another
  but are in different ERDs, you must still connect those relationships
