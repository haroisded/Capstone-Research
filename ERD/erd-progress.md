# ERD Implementation Progress & Master Inventory

> Authoritative inventory and tracking document generated according to [`Plan.md`](Plan.md).

## Source Metadata

- **Source SQL File**: `supabase_schema.sql`
- **SHA256 Content Hash**: `3837a8267359504363971eaaf60214baad8639e98e29225924c18f4d40ce08cb`
- **Total Public Tables**: 68
- **Total Foreign Key Constraints**: 202
- **External Tables Referenced**: `auth.users` (referenced by 6 tables: `profiles`, `merchants`, `feature_preferences`, `access_requests`, `merchant_members`, `notifications`)
- **Lucid Document**: [Uel ERD document](https://lucid.app/lucidchart/c56b9f9a-911b-4161-8082-0d547b3b4f50/edit)

## Global Canvas Layout Architecture

The canvas is organized into 4 major vertical columns with dedicated whitespace corridors (width: 250px) between columns and 150px vertical corridors between section areas. This guarantees orthogonal routing without crossing table boundaries.

| Column | Focus Areas | Sections Included |
|---|---|---|
| **Column 1 (Identity & Foundation)** | Identity, Store Setup, Team, Access Control | `EXT (auth.users)`, `ERD-01 (Foundation)`, `ERD-02 (Preferences)`, `ERD-03 (Staff Access)`, `ERD-04 (Roles & Permissions)` |
| **Column 2 (Financial Core & Settings)** | General Ledger, Fiscal Years, System Configuration, Payment | `ERD-05 (Accounting)`, `ERD-06 (Store Config)`, `ERD-07 (Currency & Payments)`, `ERD-11 (Naming & Prints)` |
| **Column 3 (Catalog, Stock & Tax Rules)** | Stock Architecture, Pricing, Taxes, Item Masters | `ERD-08 (Stock Config)`, `ERD-09 (Taxes)`, `ERD-10 (Price Lists & Rules)`, `ERD-13 (Items Master)` |
| **Column 4 (Operations & POS Sessions)** | Inventory Transactions, POS Terminal Profiles, Shift Sessions, Invoicing | `ERD-14 (Inventory Balances & Ledger)`, `ERD-12 (POS Profiles)`, `ERD-15 (Opening Sessions)`, `ERD-16 (Sales Invoices)`, `ERD-17 (Closing Sessions)` |

### Key Routing Rules

1. **Merchants to Accounts Corridor**: `merchants` (ERD-01, Col 1) has 11 distinct account references to `accounts` (ERD-05, Col 2). These routes use the designated horizontal conduit between Row 1 of Col 1 and Row 1 of Col 2.

2. **Merchants Global Fan-out**: Most tables contain `merchant_id -> merchants.id`. Dedicated perimeter trunk routes run along the top and left margins so perimeter lines never intersect interior table boxes.

3. **Canonical Single-Shape Rule**: Every defined table exists in exactly one area. Placeholders in future sections use the exact target area and name, marked `pending full detail — ERD-XX`.

4. **No Table Crossing**: Connectors use orthogonal bends and enter target tables through designated perimeter ports.

## Canonical Table Registry (68 Public Tables + 1 External)

| Schema.Table | Section | Columns | PK Columns | Unconditional UQs | Status | Lucid Item ID |
|---|---|---|---|---|---|---|
| `auth.users` | `EXT` | `id` (referenced) | `id` | - | External Reference | Pending |
| `public.profiles` | `ERD-01` | 4 | `id` | None | Pending | - |
| `public.merchants` | `ERD-01` | 19 | `id` | None | Pending | - |
| `public.countries` | `ERD-01` | 5 | `code` | country_name | Pending | - |
| `public.currency_presets` | `ERD-01` | 7 | `code` | None | Pending | - |
| `public.feature_preferences` | `ERD-02` | 4 | `user_id, merchant_id` | None | Pending | - |
| `public.access_codes` | `ERD-03` | 7 | `id` | code | Pending | - |
| `public.access_requests` | `ERD-03` | 12 | `id` | None | Pending | - |
| `public.merchant_members` | `ERD-03` | 9 | `id` | id, merchant_id; merchant_id, user_id | Pending | - |
| `public.notifications` | `ERD-03` | 9 | `id` | None | Pending | - |
| `public.roles` | `ERD-04` | 6 | `id` | id, merchant_id; merchant_id, role_name | Pending | - |
| `public.permissions` | `ERD-04` | 5 | `key` | None | Pending | - |
| `public.role_grants` | `ERD-04` | 3 | `role_id, permission` | None | Pending | - |
| `public.member_overrides` | `ERD-04` | 4 | `member_id, permission` | None | Pending | - |
| `public.permission_rules` | `ERD-04` | 3 | `permission, doctype, ptype` | None | Pending | - |
| `public.doctypes` | `ERD-04` | 3 | `name` | None | Pending | - |
| `public.accounts` | `ERD-05` | 10 | `id` | id, merchant_id; merchant_id, account_name; merchant_id, account_number | Pending | - |
| `public.fiscal_years` | `ERD-05` | 9 | `id` | id, merchant_id; merchant_id, year | Pending | - |
| `public.gl_entries` | `ERD-05` | 12 | `id` | None | Pending | - |
| `public.global_defaults` | `ERD-06` | 3 | `merchant_id` | None | Pending | - |
| `public.system_settings` | `ERD-06` | 6 | `merchant_id` | None | Pending | - |
| `public.accounts_settings` | `ERD-06` | 8 | `merchant_id` | None | Pending | - |
| `public.selling_settings` | `ERD-06` | 5 | `merchant_id` | None | Pending | - |
| `public.stock_settings` | `ERD-06` | 8 | `merchant_id` | None | Pending | - |
| `public.print_settings` | `ERD-06` | 4 | `merchant_id` | None | Pending | - |
| `public.currencies` | `ERD-07` | 10 | `id` | merchant_id, code; id, merchant_id | Pending | - |
| `public.modes_of_payment` | `ERD-07` | 7 | `id` | id, merchant_id; merchant_id, mode_of_payment | Pending | - |
| `public.warehouses` | `ERD-08` | 8 | `id` | id, merchant_id; merchant_id, warehouse_name | Pending | - |
| `public.uoms` | `ERD-08` | 6 | `id` | id, merchant_id; merchant_id, uom_name | Pending | - |
| `public.uom_conversion_factors` | `ERD-08` | 6 | `id` | id, merchant_id; merchant_id, from_uom, to_uom | Pending | - |
| `public.brands` | `ERD-08` | 8 | `id` | id, merchant_id; merchant_id, brand | Pending | - |
| `public.item_groups` | `ERD-08` | 10 | `id` | id, merchant_id; merchant_id, item_group_name | Pending | - |
| `public.tax_categories` | `ERD-09` | 5 | `id` | id, merchant_id; merchant_id, title | Pending | - |
| `public.tax_presets` | `ERD-09` | 5 | `country_code, template` | None | Pending | - |
| `public.sales_tax_templates` | `ERD-09` | 7 | `id` | id, merchant_id; merchant_id, title | Pending | - |
| `public.sales_tax_template_rows` | `ERD-09` | 11 | `id` | template_id, idx | Pending | - |
| `public.item_tax_templates` | `ERD-09` | 5 | `id` | id, merchant_id; merchant_id, title | Pending | - |
| `public.item_tax_template_rows` | `ERD-09` | 7 | `id` | template_id, account | Pending | - |
| `public.tax_rules` | `ERD-09` | 9 | `id` | id, merchant_id | Pending | - |
| `public.price_lists` | `ERD-10` | 7 | `id` | id, merchant_id; merchant_id, price_list_name | Pending | - |
| `public.pricing_rules` | `ERD-10` | 18 | `id` | id, merchant_id; merchant_id, title | Pending | - |
| `public.pricing_rule_targets` | `ERD-10` | 7 | `id` | None | Pending | - |
| `public.naming_series` | `ERD-11` | 4 | `merchant_id, document_type` | None | Pending | - |
| `public.naming_series_counters` | `ERD-11` | 3 | `merchant_id, prefix` | None | Pending | - |
| `public.letter_heads` | `ERD-11` | 8 | `id` | id, merchant_id; merchant_id, letter_head_name | Pending | - |
| `public.print_formats` | `ERD-11` | 10 | `id` | id, merchant_id; merchant_id, print_format_name | Pending | - |
| `public.pos_profiles` | `ERD-12` | 24 | `id` | id, merchant_id; merchant_id, pos_profile_name | Pending | - |
| `public.pos_profile_users` | `ERD-12` | 6 | `id` | pos_profile_id, member_id | Pending | - |
| `public.pos_profile_item_groups` | `ERD-12` | 5 | `id` | pos_profile_id, item_group_id | Pending | - |
| `public.pos_profile_payments` | `ERD-12` | 7 | `id` | pos_profile_id, mode_of_payment_id | Pending | - |
| `public.items` | `ERD-13` | 22 | `id` | merchant_id, item_code; id, merchant_id | Pending | - |
| `public.item_uoms` | `ERD-13` | 6 | `id` | item_id, uom_id | Pending | - |
| `public.item_taxes` | `ERD-13` | 7 | `id` | None | Pending | - |
| `public.item_group_taxes` | `ERD-13` | 9 | `id` | None | Pending | - |
| `public.item_prices` | `ERD-13` | 9 | `id` | id, merchant_id | Pending | - |
| `public.bins` | `ERD-14` | 8 | `item_id, warehouse_id` | None | Pending | - |
| `public.stock_entries` | `ERD-14` | 10 | `id` | id, merchant_id; merchant_id, name | Pending | - |
| `public.stock_entry_items` | `ERD-14` | 8 | `id` | None | Pending | - |
| `public.stock_reconciliations` | `ERD-14` | 8 | `id` | id, merchant_id; merchant_id, name | Pending | - |
| `public.stock_reconciliation_items` | `ERD-14` | 11 | `id` | stock_reconciliation_id, item_id, warehouse_id | Pending | - |
| `public.stock_ledger_entries` | `ERD-14` | 16 | `id` | None | Pending | - |
| `public.pos_opening_entries` | `ERD-15` | 10 | `id` | id, merchant_id; merchant_id, name | Pending | - |
| `public.pos_opening_entry_balances` | `ERD-15` | 6 | `id` | pos_opening_entry_id, mode_of_payment_id | Pending | - |
| `public.pos_invoices` | `ERD-16` | 27 | `id` | id, merchant_id; merchant_id, name | Pending | - |
| `public.pos_invoice_items` | `ERD-16` | 25 | `id` | id, merchant_id | Pending | - |
| `public.pos_invoice_payments` | `ERD-16` | 7 | `id` | None | Pending | - |
| `public.pos_invoice_taxes` | `ERD-16` | 13 | `id` | None | Pending | - |
| `public.pos_closing_entries` | `ERD-17` | 12 | `id` | id, merchant_id; merchant_id, name | Pending | - |
| `public.pos_closing_entry_payments` | `ERD-17` | 9 | `id` | pos_closing_entry_id, mode_of_payment_id | Pending | - |

---

## Section Detailed Specifications and FK Inventory

### ERD-01 — Accounts and store foundation

- **Primary Tables**: `profiles`, `merchants`, `countries`, `currency_presets`
- **Outgoing FK Count**: 16
- **Status**: Ready for Drawing

#### Table Definitions

##### Table `public.profiles` (SQL Line 2462)

- **Primary Key**: `profiles_pkey` on `(id)` (Line 3587)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | - | PK, FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (users) |
| `display_name` | `text` | NULL | - | - |
| `avatar_url` | `text` | NULL | - | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

##### Table `public.merchants` (SQL Line 1978)

- **Primary Key**: `merchants_pkey` on `(id)` (Line 3219)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK, FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (users) |
| `owner_id` | `uuid` | NOT NULL | - | FK (users) |
| `name` | `text` | NOT NULL | - | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |
| `country_code` | `text` | NOT NULL | - | FK (countries) |
| `default_currency` | `text` | NOT NULL | - | FK (currency_presets) |
| `default_cash_account` | `uuid` | NULL | - | FK (accounts) |
| `default_bank_account` | `uuid` | NULL | - | FK (accounts) |
| `default_income_account` | `uuid` | NULL | - | FK (accounts) |
| `default_expense_account` | `uuid` | NULL | - | FK (accounts) |
| `write_off_account` | `uuid` | NULL | - | FK (accounts) |
| `round_off_account` | `uuid` | NULL | - | FK (accounts) |
| `enable_perpetual_inventory` | `boolean` | NOT NULL | `true` | - |
| `default_inventory_account` | `uuid` | NULL | - | FK (accounts) |
| `stock_adjustment_account` | `uuid` | NULL | - | FK (accounts) |
| `stock_received_but_not_billed` | `uuid` | NULL | - | FK (accounts) |
| `expenses_included_in_valuation` | `uuid` | NULL | - | FK (accounts) |
| `default_discount_account` | `uuid` | NULL | - | FK (accounts) |
| `level` | `smallint` | NOT NULL | `5` | - |

##### Table `public.countries` (SQL Line 1629)

- **Primary Key**: `countries_pkey` on `(code)` (Line 2915)
- **Unique Constraint**: `countries_country_name_key` on `(country_name)` (Line 2907)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `code` | `text` | NOT NULL | - | PK |
| `country_name` | `text` | NOT NULL | - | UQ |
| `currency_code` | `text` | NULL | - | FK (currency_presets) |
| `time_zones` | `text[]` | NOT NULL | `''::text[]` | - |
| `number_format` | `text` | NOT NULL | - | - |

##### Table `public.currency_presets` (SQL Line 1666)

- **Primary Key**: `currency_presets_pkey` on `(code)` (Line 2947)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `code` | `text` | NOT NULL | - | PK |
| `currency_name` | `text` | NOT NULL | - | - |
| `symbol` | `text` | NULL | - | - |
| `fraction` | `text` | NULL | - | - |
| `fraction_units` | `integer` | NULL | - | - |
| `smallest_currency_fraction_value` | `numeric` | NULL | - | - |
| `number_format` | `text` | NOT NULL | - | - |

#### Declared Outgoing Foreign Keys

| Constraint Name | Child Columns | Referenced Entity | Parent End | Child End | Delete / Update Action | SQL Line | Connector ID |
|---|---|---|---|---|---|---|---|
| `countries_currency_code_fkey` | `public.countries(currency_code)` | `public.currency_presets(code)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5580 | - |
| `merchants_country_fk` | `public.merchants(country_code)` | `public.countries(code)` | `1` | `0..*` | RESTRICT/NO ACTION | 5980 | - |
| `merchants_default_bank_account_fk` | `public.merchants(default_bank_account, id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5988 | - |
| `merchants_default_cash_account_fk` | `public.merchants(default_cash_account, id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5996 | - |
| `merchants_default_currency_fk` | `public.merchants(default_currency)` | `public.currency_presets(code)` | `1` | `0..*` | RESTRICT/NO ACTION | 6004 | - |
| `merchants_default_discount_account_fk` | `public.merchants(default_discount_account, id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6012 | - |
| `merchants_default_expense_account_fk` | `public.merchants(default_expense_account, id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6020 | - |
| `merchants_default_income_account_fk` | `public.merchants(default_income_account, id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6028 | - |
| `merchants_default_inventory_account_fk` | `public.merchants(default_inventory_account, id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6036 | - |
| `merchants_expenses_included_in_valuation_fk` | `public.merchants(expenses_included_in_valuation, id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6044 | - |
| `merchants_owner_id_fkey` | `public.merchants(owner_id)` | `auth.users(id)` | `1` | `0..*` | ON DELETE CASCADE | 6052 | - |
| `merchants_round_off_account_fk` | `public.merchants(round_off_account, id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6060 | - |
| `merchants_stock_adjustment_account_fk` | `public.merchants(stock_adjustment_account, id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6068 | - |
| `merchants_stock_received_but_not_billed_fk` | `public.merchants(stock_received_but_not_billed, id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6076 | - |
| `merchants_write_off_account_fk` | `public.merchants(write_off_account, id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6084 | - |
| `profiles_id_fkey` | `public.profiles(id)` | `auth.users(id)` | `1` | `0..1` | ON DELETE CASCADE | 6716 | - |

---

### ERD-02 — Store feature preferences

- **Primary Tables**: `feature_preferences`
- **Outgoing FK Count**: 2
- **Status**: Ready for Drawing

#### Table Definitions

##### Table `public.feature_preferences` (SQL Line 1694)

- **Primary Key**: `feature_preferences_pkey` on `(user_id, merchant_id)` (Line 2963)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `user_id` | `uuid` | NOT NULL | - | PK, FK (users) |
| `merchant_id` | `uuid` | NOT NULL | - | PK, FK (merchants) |
| `hidden` | `text[]` | NOT NULL | `''::text[]` | - |
| `updated_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

#### Declared Outgoing Foreign Keys

| Constraint Name | Child Columns | Referenced Entity | Parent End | Child End | Delete / Update Action | SQL Line | Connector ID |
|---|---|---|---|---|---|---|---|
| `feature_preferences_merchant_id_fkey` | `public.feature_preferences(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 5604 | - |
| `feature_preferences_user_id_fkey` | `public.feature_preferences(user_id)` | `auth.users(id)` | `1` | `0..*` | ON DELETE CASCADE | 5612 | - |

---

### ERD-03 — Staff access and notifications

- **Primary Tables**: `access_codes`, `access_requests`, `merchant_members`, `notifications`
- **Outgoing FK Count**: 10
- **Status**: Ready for Drawing

#### Table Definitions

##### Table `public.access_codes` (SQL Line 192)

- **Primary Key**: `access_codes_pkey` on `(id)` (Line 2819)
- **Unique Constraint**: `access_codes_code_unique` on `(code)` (Line 2811)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (merchants), FK (merchants), FK (merchants), FK (roles), FK (merchants) |
| `code` | `text` | NOT NULL | - | UQ |
| `label` | `text` | NULL | - | - |
| `expires_at` | `timestamp with time zone` | NULL | - | - |
| `max_uses` | `integer` | NULL | - | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

##### Table `public.access_requests` (SQL Line 1544)

- **Primary Key**: `access_requests_pkey` on `(id)` (Line 2827)
- **Partial Unique Index**: `access_requests_one_pending` on `(merchant_id, user_id)` WHERE `(status = 'pending'::text)` (Line 3920)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (merchants), FK (merchants), FK (merchants), FK (roles), FK (merchants) |
| `merchant_name` | `text` | NOT NULL | - | - |
| `access_code_id` | `uuid` | NULL | - | FK (access_codes) |
| `code` | `text` | NOT NULL | - | - |
| `user_id` | `uuid` | NOT NULL | - | FK (users), FK (users), FK (users) |
| `full_name` | `text` | NULL | - | - |
| `email` | `text` | NULL | - | - |
| `avatar_url` | `text` | NULL | - | - |
| `status` | `text` | NOT NULL | `''::text` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |
| `decided_at` | `timestamp with time zone` | NULL | - | - |

##### Table `public.merchant_members` (SQL Line 1960)

- **Primary Key**: `merchant_members_pkey` on `(id)` (Line 3203)
- **Unique Constraint**: `merchant_members_id_merchant` on `(id, merchant_id)` (Line 3195)
- **Unique Constraint**: `merchant_members_user_unique` on `(merchant_id, user_id)` (Line 3211)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (merchants), FK (merchants), FK (merchants), FK (roles), FK (merchants) |
| `email` | `text` | NULL | - | - |
| `full_name` | `text` | NULL | - | - |
| `user_id` | `uuid` | NOT NULL | - | FK (users), FK (users), FK (users) |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |
| `avatar_url` | `text` | NULL | - | - |
| `access_code` | `text` | NULL | - | - |
| `role_id` | `uuid` | NULL | - | FK (roles) |

##### Table `public.notifications` (SQL Line 2051)

- **Primary Key**: `notifications_pkey` on `(id)` (Line 3267)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `user_id` | `uuid` | NOT NULL | - | FK (users), FK (users), FK (users) |
| `merchant_id` | `uuid` | NULL | - | FK (merchants), FK (merchants), FK (merchants), FK (roles), FK (merchants) |
| `kind` | `text` | NOT NULL | - | - |
| `title` | `text` | NOT NULL | - | - |
| `body` | `text` | NULL | - | - |
| `request_id` | `uuid` | NULL | - | FK (access_requests) |
| `read_at` | `timestamp with time zone` | NULL | - | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

#### Declared Outgoing Foreign Keys

| Constraint Name | Child Columns | Referenced Entity | Parent End | Child End | Delete / Update Action | SQL Line | Connector ID |
|---|---|---|---|---|---|---|---|
| `access_codes_merchant_id_fkey` | `public.access_codes(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 5460 | - |
| `access_requests_access_code_id_fkey` | `public.access_requests(access_code_id)` | `public.access_codes(id)` | `0..1` | `0..*` | ON DELETE SET NULL | 5468 | - |
| `access_requests_merchant_id_fkey` | `public.access_requests(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 5476 | - |
| `access_requests_user_id_fkey` | `public.access_requests(user_id)` | `auth.users(id)` | `1` | `0..*` | ON DELETE CASCADE | 5484 | - |
| `merchant_members_merchant_id_fkey` | `public.merchant_members(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 5956 | - |
| `merchant_members_role_fk` | `public.merchant_members(role_id, merchant_id)` | `public.roles(id, merchant_id)` | `0..1` | `0..*` | ON DELETE SET NULL (role_id) | 5964 | - |
| `merchant_members_user_id_fkey` | `public.merchant_members(user_id)` | `auth.users(id)` | `1` | `0..*` | ON DELETE CASCADE | 5972 | - |
| `notifications_merchant_id_fkey` | `public.notifications(merchant_id)` | `public.merchants(id)` | `0..1` | `0..*` | ON DELETE CASCADE | 6124 | - |
| `notifications_request_id_fkey` | `public.notifications(request_id)` | `public.access_requests(id)` | `0..1` | `0..*` | ON DELETE SET NULL | 6132 | - |
| `notifications_user_id_fkey` | `public.notifications(user_id)` | `auth.users(id)` | `1` | `0..*` | ON DELETE CASCADE | 6140 | - |

---

### ERD-04 — Roles and permissions

- **Primary Tables**: `roles`, `permissions`, `role_grants`, `member_overrides`, `permission_rules`, `doctypes`
- **Outgoing FK Count**: 8
- **Status**: Ready for Drawing

#### Table Definitions

##### Table `public.roles` (SQL Line 2485)

- **Primary Key**: `roles_pkey` on `(id)` (Line 3619)
- **Unique Constraint**: `roles_id_merchant` on `(id, merchant_id)` (Line 3603)
- **Unique Constraint**: `roles_name_unique` on `(merchant_id, role_name)` (Line 3611)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (merchant_members), FK (roles), FK (merchants) |
| `role_name` | `text` | NOT NULL | - | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |
| `description` | `text` | NULL | - | - |
| `color` | `text` | NOT NULL | `''::text` | - |

##### Table `public.permissions` (SQL Line 2081)

- **Primary Key**: `permissions_pkey` on `(key)` (Line 3283)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `key` | `text` | NOT NULL | - | PK |
| `category` | `text` | NOT NULL | - | - |
| `label` | `text` | NOT NULL | - | - |
| `description` | `text` | NOT NULL | - | - |
| `requires` | `text` | NULL | - | FK (permissions) |

##### Table `public.role_grants` (SQL Line 2474)

- **Primary Key**: `role_grants_pkey` on `(role_id, permission)` (Line 3595)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `merchant_id` | `uuid` | NOT NULL | - | FK (merchant_members), FK (roles), FK (merchants) |
| `role_id` | `uuid` | NOT NULL | - | PK, FK (roles) |
| `permission` | `text` | NOT NULL | - | PK, FK (permissions), FK (permissions), FK (permissions) |

##### Table `public.member_overrides` (SQL Line 1948)

- **Primary Key**: `member_overrides_pkey` on `(member_id, permission)` (Line 3187)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `merchant_id` | `uuid` | NOT NULL | - | FK (merchant_members), FK (roles), FK (merchants) |
| `member_id` | `uuid` | NOT NULL | - | PK, FK (merchant_members) |
| `permission` | `text` | NOT NULL | - | PK, FK (permissions), FK (permissions), FK (permissions) |
| `allowed` | `boolean` | NOT NULL | - | - |

##### Table `public.permission_rules` (SQL Line 2069)

- **Primary Key**: `permission_rules_pkey` on `(permission, doctype, ptype)` (Line 3275)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `permission` | `text` | NOT NULL | - | PK, FK (permissions), FK (permissions), FK (permissions) |
| `doctype` | `text` | NOT NULL | - | PK, FK (doctypes) |
| `ptype` | `text` | NOT NULL | - | PK |

##### Table `public.doctypes` (SQL Line 1682)

- **Primary Key**: `doctypes_pkey` on `(name)` (Line 2955)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `name` | `text` | NOT NULL | - | PK |
| `table_name` | `text` | NOT NULL | - | - |
| `kind` | `text` | NOT NULL | - | - |

#### Declared Outgoing Foreign Keys

| Constraint Name | Child Columns | Referenced Entity | Parent End | Child End | Delete / Update Action | SQL Line | Connector ID |
|---|---|---|---|---|---|---|---|
| `member_overrides_member_fk` | `public.member_overrides(member_id, merchant_id)` | `public.merchant_members(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 5940 | - |
| `member_overrides_permission_fkey` | `public.member_overrides(permission)` | `public.permissions(key)` | `1` | `0..*` | ON DELETE CASCADE | 5948 | - |
| `permission_rules_doctype_fkey` | `public.permission_rules(doctype)` | `public.doctypes(name)` | `1` | `0..*` | ON DELETE CASCADE | 6148 | - |
| `permission_rules_permission_fkey` | `public.permission_rules(permission)` | `public.permissions(key)` | `1` | `0..*` | ON DELETE CASCADE | 6156 | - |
| `permissions_requires_fkey` | `public.permissions(requires)` | `public.permissions(key)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6164 | - |
| `role_grants_permission_fkey` | `public.role_grants(permission)` | `public.permissions(key)` | `1` | `0..*` | ON DELETE CASCADE | 6724 | - |
| `role_grants_role_fk` | `public.role_grants(role_id, merchant_id)` | `public.roles(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 6732 | - |
| `roles_merchant_id_fkey` | `public.roles(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6740 | - |

---

### ERD-05 — Accounting and fiscal years

- **Primary Tables**: `accounts`, `fiscal_years`, `gl_entries`
- **Outgoing FK Count**: 5
- **Status**: Ready for Drawing

#### Table Definitions

##### Table `public.accounts` (SQL Line 1565)

- **Primary Key**: `accounts_pkey` on `(id)` (Line 2859)
- **Unique Constraint**: `accounts_id_merchant` on `(id, merchant_id)` (Line 2835)
- **Unique Constraint**: `accounts_name_unique` on `(merchant_id, account_name)` (Line 2843)
- **Unique Constraint**: `accounts_number_unique` on `(merchant_id, account_number)` (Line 2851)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (merchants), FK (accounts), FK (merchants), FK (accounts), FK (merchants) |
| `account_name` | `text` | NOT NULL | - | - |
| `account_number` | `text` | NULL | - | - |
| `parent_id` | `uuid` | NULL | - | FK (accounts) |
| `is_group` | `boolean` | NOT NULL | `false` | - |
| `root_type` | `text` | NOT NULL | - | - |
| `account_type` | `text` | NULL | - | - |
| `disabled` | `boolean` | NOT NULL | `false` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

##### Table `public.fiscal_years` (SQL Line 1707)

- **Primary Key**: `fiscal_years_pkey` on `(id)` (Line 2987)
- **Unique Constraint**: `fiscal_years_id_merchant` on `(id, merchant_id)` (Line 2971)
- **Unique Constraint**: `fiscal_years_year_unique` on `(merchant_id, year)` (Line 2995)
- **Partial Unique Index**: `fiscal_years_one_default` on `(merchant_id)` WHERE `is_default` (Line 4011)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (merchants), FK (accounts), FK (merchants), FK (accounts), FK (merchants) |
| `year` | `text` | NOT NULL | - | - |
| `year_start_date` | `date` | NOT NULL | - | - |
| `year_end_date` | `date` | NOT NULL | - | - |
| `is_short_year` | `boolean` | NOT NULL | `false` | - |
| `is_default` | `boolean` | NOT NULL | `false` | - |
| `disabled` | `boolean` | NOT NULL | `false` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

##### Table `public.gl_entries` (SQL Line 1730)

- **Primary Key**: `gl_entries_pkey` on `(id)` (Line 3003)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `bigint` | NOT NULL | - | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (merchants), FK (accounts), FK (merchants), FK (accounts), FK (merchants) |
| `posting_date` | `date` | NOT NULL | - | - |
| `account_id` | `uuid` | NOT NULL | - | FK (accounts) |
| `debit` | `numeric` | NOT NULL | `0` | - |
| `credit` | `numeric` | NOT NULL | `0` | - |
| `voucher_type` | `text` | NOT NULL | - | - |
| `voucher_id` | `uuid` | NOT NULL | - | - |
| `voucher_no` | `text` | NOT NULL | - | - |
| `remarks` | `text` | NULL | - | - |
| `is_cancelled` | `boolean` | NOT NULL | `false` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

#### Declared Outgoing Foreign Keys

| Constraint Name | Child Columns | Referenced Entity | Parent End | Child End | Delete / Update Action | SQL Line | Connector ID |
|---|---|---|---|---|---|---|---|
| `accounts_merchant_id_fkey` | `public.accounts(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 5492 | - |
| `accounts_parent_fk` | `public.accounts(parent_id, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5500 | - |
| `fiscal_years_merchant_id_fkey` | `public.fiscal_years(merchant_id)` | `public.merchants(id)` | `1` | `0..* *(cond: is_default)*` | ON DELETE CASCADE | 5620 | - |
| `gl_entries_account_fk` | `public.gl_entries(account_id, merchant_id)` | `public.accounts(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 5628 | - |
| `gl_entries_merchant_id_fkey` | `public.gl_entries(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 5636 | - |

---

### ERD-06 — Store configuration

- **Primary Tables**: `global_defaults`, `system_settings`, `accounts_settings`, `selling_settings`, `stock_settings`, `print_settings`
- **Outgoing FK Count**: 11
- **Status**: Ready for Drawing

#### Table Definitions

##### Table `public.global_defaults` (SQL Line 1765)

- **Primary Key**: `global_defaults_pkey` on `(merchant_id)` (Line 3011)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `merchant_id` | `uuid` | NOT NULL | - | PK, FK (merchants), FK (roles), FK (merchants), FK (merchants), FK (merchants), FK (price_lists), FK (item_groups), FK (merchants), FK (uoms), FK (warehouses), FK (merchants) |
| `disable_rounded_total` | `boolean` | NOT NULL | `false` | - |
| `disable_in_words` | `boolean` | NOT NULL | `false` | - |

##### Table `public.system_settings` (SQL Line 2699)

- **Primary Key**: `system_settings_pkey` on `(merchant_id)` (Line 3763)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `merchant_id` | `uuid` | NOT NULL | - | PK, FK (merchants), FK (roles), FK (merchants), FK (merchants), FK (merchants), FK (price_lists), FK (item_groups), FK (merchants), FK (uoms), FK (warehouses), FK (merchants) |
| `time_zone` | `text` | NOT NULL | - | - |
| `number_format` | `text` | NOT NULL | `''::text` | - |
| `float_precision` | `smallint` | NOT NULL | `3` | - |
| `currency_precision` | `smallint` | NOT NULL | `2` | - |
| `rounding_method` | `text` | NOT NULL | `''''::text` | - |

##### Table `public.accounts_settings` (SQL Line 1595)

- **Primary Key**: `accounts_settings_pkey` on `(merchant_id)` (Line 2867)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `merchant_id` | `uuid` | NOT NULL | - | PK, FK (merchants), FK (roles), FK (merchants), FK (merchants), FK (merchants), FK (price_lists), FK (item_groups), FK (merchants), FK (uoms), FK (warehouses), FK (merchants) |
| `unlink_payment_on_cancellation` | `boolean` | NOT NULL | `true` | - |
| `delete_linked_ledger_entries` | `boolean` | NOT NULL | `false` | - |
| `enable_immutable_ledger` | `boolean` | NOT NULL | `true` | - |
| `enable_discount_accounting` | `boolean` | NOT NULL | `false` | - |
| `add_taxes_from_item_tax_template` | `boolean` | NOT NULL | `true` | - |
| `accounts_frozen_till_date` | `date` | NULL | - | - |
| `frozen_accounts_modifier` | `uuid` | NULL | - | FK (roles) |

##### Table `public.selling_settings` (SQL Line 2547)

- **Primary Key**: `selling_settings_pkey` on `(merchant_id)` (Line 3667)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `merchant_id` | `uuid` | NOT NULL | - | PK, FK (merchants), FK (roles), FK (merchants), FK (merchants), FK (merchants), FK (price_lists), FK (item_groups), FK (merchants), FK (uoms), FK (warehouses), FK (merchants) |
| `default_price_list` | `uuid` | NULL | - | FK (price_lists) |
| `fallback_to_default_price_list` | `boolean` | NOT NULL | `false` | - |
| `editable_price_list_rate` | `boolean` | NOT NULL | `false` | - |
| `validate_selling_price` | `boolean` | NOT NULL | `false` | - |

##### Table `public.stock_settings` (SQL Line 2681)

- **Primary Key**: `stock_settings_pkey` on `(merchant_id)` (Line 3755)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `merchant_id` | `uuid` | NOT NULL | - | PK, FK (merchants), FK (roles), FK (merchants), FK (merchants), FK (merchants), FK (price_lists), FK (item_groups), FK (merchants), FK (uoms), FK (warehouses), FK (merchants) |
| `item_naming_by` | `text` | NOT NULL | `''::text` | - |
| `item_group` | `uuid` | NULL | - | FK (item_groups) |
| `stock_uom` | `uuid` | NULL | - | FK (uoms) |
| `default_warehouse` | `uuid` | NULL | - | FK (warehouses) |
| `valuation_method` | `text` | NOT NULL | `''::text` | - |
| `allow_negative_stock` | `boolean` | NOT NULL | `false` | - |
| `auto_insert_price_list_rate_if_missing` | `boolean` | NOT NULL | `false` | - |

##### Table `public.print_settings` (SQL Line 2450)

- **Primary Key**: `print_settings_pkey` on `(merchant_id)` (Line 3579)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `merchant_id` | `uuid` | NOT NULL | - | PK, FK (merchants), FK (roles), FK (merchants), FK (merchants), FK (merchants), FK (price_lists), FK (item_groups), FK (merchants), FK (uoms), FK (warehouses), FK (merchants) |
| `with_letterhead` | `boolean` | NOT NULL | `true` | - |
| `compact_item_print` | `boolean` | NOT NULL | `true` | - |
| `print_taxes_with_zero_amount` | `boolean` | NOT NULL | `false` | - |

#### Declared Outgoing Foreign Keys

| Constraint Name | Child Columns | Referenced Entity | Parent End | Child End | Delete / Update Action | SQL Line | Connector ID |
|---|---|---|---|---|---|---|---|
| `accounts_settings_merchant_id_fkey` | `public.accounts_settings(merchant_id)` | `public.merchants(id)` | `1` | `0..1` | ON DELETE CASCADE | 5508 | - |
| `accounts_settings_modifier_fk` | `public.accounts_settings(frozen_accounts_modifier, merchant_id)` | `public.roles(id, merchant_id)` | `0..1` | `0..*` | ON DELETE SET NULL (frozen_accounts_modifier) | 5516 | - |
| `global_defaults_merchant_id_fkey` | `public.global_defaults(merchant_id)` | `public.merchants(id)` | `1` | `0..1` | ON DELETE CASCADE | 5644 | - |
| `print_settings_merchant_id_fkey` | `public.print_settings(merchant_id)` | `public.merchants(id)` | `1` | `0..1` | ON DELETE CASCADE | 6708 | - |
| `selling_settings_merchant_id_fkey` | `public.selling_settings(merchant_id)` | `public.merchants(id)` | `1` | `0..1` | ON DELETE CASCADE | 6788 | - |
| `selling_settings_price_list_fk` | `public.selling_settings(default_price_list, merchant_id)` | `public.price_lists(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6796 | - |
| `stock_settings_item_group_fk` | `public.stock_settings(item_group, merchant_id)` | `public.item_groups(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6932 | - |
| `stock_settings_merchant_id_fkey` | `public.stock_settings(merchant_id)` | `public.merchants(id)` | `1` | `0..1` | ON DELETE CASCADE | 6940 | - |
| `stock_settings_uom_fk` | `public.stock_settings(stock_uom, merchant_id)` | `public.uoms(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6948 | - |
| `stock_settings_warehouse_fk` | `public.stock_settings(default_warehouse, merchant_id)` | `public.warehouses(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6956 | - |
| `system_settings_merchant_id_fkey` | `public.system_settings(merchant_id)` | `public.merchants(id)` | `1` | `0..1` | ON DELETE CASCADE | 6964 | - |

---

### ERD-07 — Currency and payment methods

- **Primary Tables**: `currencies`, `modes_of_payment`
- **Outgoing FK Count**: 4
- **Status**: Ready for Drawing

#### Table Definitions

##### Table `public.currencies` (SQL Line 1643)

- **Primary Key**: `currencies_pkey` on `(id)` (Line 2939)
- **Unique Constraint**: `currencies_code_unique` on `(merchant_id, code)` (Line 2923)
- **Unique Constraint**: `currencies_id_merchant` on `(id, merchant_id)` (Line 2931)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (merchants), FK (accounts), FK (merchants) |
| `code` | `text` | NOT NULL | - | FK (currency_presets) |
| `enabled` | `boolean` | NOT NULL | `true` | - |
| `symbol` | `text` | NULL | - | - |
| `fraction` | `text` | NULL | - | - |
| `fraction_units` | `integer` | NULL | - | - |
| `smallest_currency_fraction_value` | `numeric` | NULL | - | - |
| `number_format` | `text` | NOT NULL | - | - |
| `symbol_on_right` | `boolean` | NOT NULL | `false` | - |

##### Table `public.modes_of_payment` (SQL Line 2007)

- **Primary Key**: `modes_of_payment_pkey` on `(id)` (Line 3243)
- **Unique Constraint**: `modes_of_payment_id_merchant` on `(id, merchant_id)` (Line 3227)
- **Unique Constraint**: `modes_of_payment_name_unique` on `(merchant_id, mode_of_payment)` (Line 3235)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (merchants), FK (accounts), FK (merchants) |
| `mode_of_payment` | `text` | NOT NULL | - | - |
| `type` | `text` | NOT NULL | `''::text` | - |
| `enabled` | `boolean` | NOT NULL | `true` | - |
| `default_account` | `uuid` | NULL | - | FK (accounts) |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

#### Declared Outgoing Foreign Keys

| Constraint Name | Child Columns | Referenced Entity | Parent End | Child End | Delete / Update Action | SQL Line | Connector ID |
|---|---|---|---|---|---|---|---|
| `currencies_code_fkey` | `public.currencies(code)` | `public.currency_presets(code)` | `1` | `0..*` | RESTRICT/NO ACTION | 5588 | - |
| `currencies_merchant_id_fkey` | `public.currencies(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 5596 | - |
| `modes_of_payment_account_fk` | `public.modes_of_payment(default_account, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6092 | - |
| `modes_of_payment_merchant_id_fkey` | `public.modes_of_payment(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6100 | - |

---

### ERD-08 — Stock configuration

- **Primary Tables**: `warehouses`, `uoms`, `uom_conversion_factors`, `brands`, `item_groups`
- **Outgoing FK Count**: 17
- **Status**: Ready for Drawing

#### Table Definitions

##### Table `public.warehouses` (SQL Line 2794)

- **Primary Key**: `warehouses_pkey` on `(id)` (Line 3891)
- **Unique Constraint**: `warehouses_id_merchant` on `(id, merchant_id)` (Line 3875)
- **Unique Constraint**: `warehouses_name_unique` on `(merchant_id, warehouse_name)` (Line 3883)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (accounts), FK (merchants), FK (price_lists), FK (warehouses), FK (accounts), FK (accounts), FK (merchants), FK (item_groups), FK (price_lists), FK (warehouses), FK (uoms), FK (merchants), FK (uoms), FK (merchants), FK (accounts), FK (merchants), FK (warehouses) |
| `warehouse_name` | `text` | NOT NULL | - | - |
| `parent_id` | `uuid` | NULL | - | FK (item_groups), FK (warehouses) |
| `is_group` | `boolean` | NOT NULL | `false` | - |
| `account` | `uuid` | NULL | - | FK (accounts) |
| `disabled` | `boolean` | NOT NULL | `false` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

##### Table `public.uoms` (SQL Line 2779)

- **Primary Key**: `uoms_pkey` on `(id)` (Line 3867)
- **Unique Constraint**: `uoms_id_merchant` on `(id, merchant_id)` (Line 3851)
- **Unique Constraint**: `uoms_name_unique` on `(merchant_id, uom_name)` (Line 3859)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (accounts), FK (merchants), FK (price_lists), FK (warehouses), FK (accounts), FK (accounts), FK (merchants), FK (item_groups), FK (price_lists), FK (warehouses), FK (uoms), FK (merchants), FK (uoms), FK (merchants), FK (accounts), FK (merchants), FK (warehouses) |
| `uom_name` | `text` | NOT NULL | - | - |
| `must_be_whole_number` | `boolean` | NOT NULL | `false` | - |
| `enabled` | `boolean` | NOT NULL | `true` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

##### Table `public.uom_conversion_factors` (SQL Line 2763)

- **Primary Key**: `uom_conversion_factors_pkey` on `(id)` (Line 3843)
- **Unique Constraint**: `uom_conversion_factors_id_merchant` on `(id, merchant_id)` (Line 3827)
- **Unique Constraint**: `uom_conversion_factors_pair_unique` on `(merchant_id, from_uom, to_uom)` (Line 3835)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (accounts), FK (merchants), FK (price_lists), FK (warehouses), FK (accounts), FK (accounts), FK (merchants), FK (item_groups), FK (price_lists), FK (warehouses), FK (uoms), FK (merchants), FK (uoms), FK (merchants), FK (accounts), FK (merchants), FK (warehouses) |
| `from_uom` | `uuid` | NOT NULL | - | FK (uoms) |
| `to_uom` | `uuid` | NOT NULL | - | FK (uoms) |
| `value` | `numeric` | NOT NULL | - | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

##### Table `public.brands` (SQL Line 1611)

- **Primary Key**: `brands_pkey` on `(id)` (Line 2899)
- **Unique Constraint**: `brands_id_merchant` on `(id, merchant_id)` (Line 2883)
- **Unique Constraint**: `brands_name_unique` on `(merchant_id, brand)` (Line 2891)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (accounts), FK (merchants), FK (price_lists), FK (warehouses), FK (accounts), FK (accounts), FK (merchants), FK (item_groups), FK (price_lists), FK (warehouses), FK (uoms), FK (merchants), FK (uoms), FK (merchants), FK (accounts), FK (merchants), FK (warehouses) |
| `brand` | `text` | NOT NULL | - | - |
| `description` | `text` | NULL | - | - |
| `default_warehouse` | `uuid` | NULL | - | FK (warehouses), FK (warehouses) |
| `default_price_list` | `uuid` | NULL | - | FK (price_lists), FK (price_lists) |
| `income_account` | `uuid` | NULL | - | FK (accounts), FK (accounts) |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

##### Table `public.item_groups` (SQL Line 1795)

- **Primary Key**: `item_groups_pkey` on `(id)` (Line 3043)
- **Unique Constraint**: `item_groups_id_merchant` on `(id, merchant_id)` (Line 3027)
- **Unique Constraint**: `item_groups_name_unique` on `(merchant_id, item_group_name)` (Line 3035)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (accounts), FK (merchants), FK (price_lists), FK (warehouses), FK (accounts), FK (accounts), FK (merchants), FK (item_groups), FK (price_lists), FK (warehouses), FK (uoms), FK (merchants), FK (uoms), FK (merchants), FK (accounts), FK (merchants), FK (warehouses) |
| `item_group_name` | `text` | NOT NULL | - | - |
| `parent_id` | `uuid` | NULL | - | FK (item_groups), FK (warehouses) |
| `is_group` | `boolean` | NOT NULL | `false` | - |
| `default_price_list` | `uuid` | NULL | - | FK (price_lists), FK (price_lists) |
| `default_warehouse` | `uuid` | NULL | - | FK (warehouses), FK (warehouses) |
| `income_account` | `uuid` | NULL | - | FK (accounts), FK (accounts) |
| `expense_account` | `uuid` | NULL | - | FK (accounts) |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

#### Declared Outgoing Foreign Keys

| Constraint Name | Child Columns | Referenced Entity | Parent End | Child End | Delete / Update Action | SQL Line | Connector ID |
|---|---|---|---|---|---|---|---|
| `brands_income_account_fk` | `public.brands(income_account, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5548 | - |
| `brands_merchant_id_fkey` | `public.brands(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 5556 | - |
| `brands_price_list_fk` | `public.brands(default_price_list, merchant_id)` | `public.price_lists(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5564 | - |
| `brands_warehouse_fk` | `public.brands(default_warehouse, merchant_id)` | `public.warehouses(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5572 | - |
| `item_groups_expense_account_fk` | `public.item_groups(expense_account, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5684 | - |
| `item_groups_income_account_fk` | `public.item_groups(income_account, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5692 | - |
| `item_groups_merchant_id_fkey` | `public.item_groups(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 5700 | - |
| `item_groups_parent_fk` | `public.item_groups(parent_id, merchant_id)` | `public.item_groups(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5708 | - |
| `item_groups_price_list_fk` | `public.item_groups(default_price_list, merchant_id)` | `public.price_lists(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5716 | - |
| `item_groups_warehouse_fk` | `public.item_groups(default_warehouse, merchant_id)` | `public.warehouses(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5724 | - |
| `uom_conversion_factors_from_fk` | `public.uom_conversion_factors(from_uom, merchant_id)` | `public.uoms(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 7020 | - |
| `uom_conversion_factors_merchant_id_fkey` | `public.uom_conversion_factors(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 7028 | - |
| `uom_conversion_factors_to_fk` | `public.uom_conversion_factors(to_uom, merchant_id)` | `public.uoms(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 7036 | - |
| `uoms_merchant_id_fkey` | `public.uoms(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 7044 | - |
| `warehouses_account_fk` | `public.warehouses(account, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 7052 | - |
| `warehouses_merchant_id_fkey` | `public.warehouses(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 7060 | - |
| `warehouses_parent_fk` | `public.warehouses(parent_id, merchant_id)` | `public.warehouses(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 7068 | - |

---

### ERD-09 — Tax configuration

- **Primary Tables**: `tax_categories`, `tax_presets`, `sales_tax_templates`, `sales_tax_template_rows`, `item_tax_templates`, `item_tax_template_rows`, `tax_rules`
- **Outgoing FK Count**: 15
- **Status**: Ready for Drawing

#### Table Definitions

##### Table `public.tax_categories` (SQL Line 2717)

- **Primary Key**: `tax_categories_pkey` on `(id)` (Line 3779)
- **Unique Constraint**: `tax_categories_id_merchant` on `(id, merchant_id)` (Line 3771)
- **Unique Constraint**: `tax_categories_title_unique` on `(merchant_id, title)` (Line 3787)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (accounts), FK (merchants), FK (item_tax_templates), FK (merchants), FK (accounts), FK (merchants), FK (sales_tax_templates), FK (tax_categories), FK (merchants), FK (merchants), FK (tax_categories), FK (item_groups), FK (merchants), FK (sales_tax_templates) |
| `title` | `text` | NOT NULL | - | - |
| `disabled` | `boolean` | NOT NULL | `false` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

##### Table `public.tax_presets` (SQL Line 2731)

- **Primary Key**: `tax_presets_pkey` on `(country_code, template)` (Line 3795)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `country_code` | `text` | NOT NULL | - | PK, FK (countries) |
| `template` | `text` | NOT NULL | - | PK |
| `account_name` | `text` | NOT NULL | - | - |
| `tax_rate` | `numeric` | NOT NULL | - | - |
| `is_default` | `boolean` | NOT NULL | `false` | - |

##### Table `public.sales_tax_templates` (SQL Line 2530)

- **Primary Key**: `sales_tax_templates_pkey` on `(id)` (Line 3651)
- **Unique Constraint**: `sales_tax_templates_id_merchant` on `(id, merchant_id)` (Line 3643)
- **Unique Constraint**: `sales_tax_templates_title_unique` on `(merchant_id, title)` (Line 3659)
- **Partial Unique Index**: `sales_tax_templates_one_default` on `(merchant_id)` WHERE `is_default` (Line 4753)
- **Partial Unique Index**: `sales_tax_templates_one_per_category` on `(merchant_id, tax_category_id)` WHERE `((tax_category_id IS NOT NULL) AND (NOT disabled))` (Line 4760)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (accounts), FK (merchants), FK (item_tax_templates), FK (merchants), FK (accounts), FK (merchants), FK (sales_tax_templates), FK (tax_categories), FK (merchants), FK (merchants), FK (tax_categories), FK (item_groups), FK (merchants), FK (sales_tax_templates) |
| `title` | `text` | NOT NULL | - | - |
| `is_default` | `boolean` | NOT NULL | `false` | - |
| `disabled` | `boolean` | NOT NULL | `false` | - |
| `tax_category_id` | `uuid` | NULL | - | FK (tax_categories), FK (tax_categories) |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

##### Table `public.sales_tax_template_rows` (SQL Line 2502)

- **Primary Key**: `sales_tax_template_rows_pkey` on `(id)` (Line 3635)
- **Unique Constraint**: `sales_tax_template_rows_idx` on `(template_id, idx)` (Line 3627)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (accounts), FK (merchants), FK (item_tax_templates), FK (merchants), FK (accounts), FK (merchants), FK (sales_tax_templates), FK (tax_categories), FK (merchants), FK (merchants), FK (tax_categories), FK (item_groups), FK (merchants), FK (sales_tax_templates) |
| `template_id` | `uuid` | NOT NULL | - | FK (item_tax_templates), FK (sales_tax_templates) |
| `idx` | `integer` | NOT NULL | - | - |
| `charge_type` | `text` | NOT NULL | - | - |
| `account` | `uuid` | NOT NULL | - | FK (accounts), FK (accounts) |
| `description` | `text` | NOT NULL | - | - |
| `rate` | `numeric` | NOT NULL | `0` | - |
| `tax_amount` | `numeric` | NOT NULL | `0` | - |
| `row_id` | `integer` | NULL | - | - |
| `included_in_print_rate` | `boolean` | NOT NULL | `false` | - |

##### Table `public.item_tax_templates` (SQL Line 1848)

- **Primary Key**: `item_tax_templates_pkey` on `(id)` (Line 3099)
- **Unique Constraint**: `item_tax_templates_id_merchant` on `(id, merchant_id)` (Line 3091)
- **Unique Constraint**: `item_tax_templates_title_unique` on `(merchant_id, title)` (Line 3107)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (accounts), FK (merchants), FK (item_tax_templates), FK (merchants), FK (accounts), FK (merchants), FK (sales_tax_templates), FK (tax_categories), FK (merchants), FK (merchants), FK (tax_categories), FK (item_groups), FK (merchants), FK (sales_tax_templates) |
| `title` | `text` | NOT NULL | - | - |
| `disabled` | `boolean` | NOT NULL | `false` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

##### Table `public.item_tax_template_rows` (SQL Line 1833)

- **Primary Key**: `item_tax_template_rows_pkey` on `(id)` (Line 3083)
- **Unique Constraint**: `item_tax_template_rows_account_unique` on `(template_id, account)` (Line 3075)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (accounts), FK (merchants), FK (item_tax_templates), FK (merchants), FK (accounts), FK (merchants), FK (sales_tax_templates), FK (tax_categories), FK (merchants), FK (merchants), FK (tax_categories), FK (item_groups), FK (merchants), FK (sales_tax_templates) |
| `template_id` | `uuid` | NOT NULL | - | FK (item_tax_templates), FK (sales_tax_templates) |
| `idx` | `integer` | NOT NULL | - | - |
| `account` | `uuid` | NOT NULL | - | FK (accounts), FK (accounts) |
| `tax_rate` | `numeric` | NOT NULL | `0` | - |
| `not_applicable` | `boolean` | NOT NULL | `false` | - |

##### Table `public.tax_rules` (SQL Line 2744)

- **Primary Key**: `tax_rules_pkey` on `(id)` (Line 3819)
- **Unique Constraint**: `tax_rules_id_merchant` on `(id, merchant_id)` (Line 3803)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (accounts), FK (merchants), FK (item_tax_templates), FK (merchants), FK (accounts), FK (merchants), FK (sales_tax_templates), FK (tax_categories), FK (merchants), FK (merchants), FK (tax_categories), FK (item_groups), FK (merchants), FK (sales_tax_templates) |
| `sales_tax_template_id` | `uuid` | NOT NULL | - | FK (sales_tax_templates) |
| `tax_category_id` | `uuid` | NULL | - | FK (tax_categories), FK (tax_categories) |
| `item_group_id` | `uuid` | NULL | - | FK (item_groups) |
| `from_date` | `date` | NULL | - | - |
| `to_date` | `date` | NULL | - | - |
| `priority` | `integer` | NOT NULL | `1` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

#### Declared Outgoing Foreign Keys

| Constraint Name | Child Columns | Referenced Entity | Parent End | Child End | Delete / Update Action | SQL Line | Connector ID |
|---|---|---|---|---|---|---|---|
| `item_tax_template_rows_account_fk` | `public.item_tax_template_rows(account, merchant_id)` | `public.accounts(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 5764 | - |
| `item_tax_template_rows_merchant_id_fkey` | `public.item_tax_template_rows(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 5772 | - |
| `item_tax_template_rows_template_fk` | `public.item_tax_template_rows(template_id, merchant_id)` | `public.item_tax_templates(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 5780 | - |
| `item_tax_templates_merchant_id_fkey` | `public.item_tax_templates(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 5788 | - |
| `sales_tax_template_rows_account_fk` | `public.sales_tax_template_rows(account, merchant_id)` | `public.accounts(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 6748 | - |
| `sales_tax_template_rows_merchant_id_fkey` | `public.sales_tax_template_rows(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6756 | - |
| `sales_tax_template_rows_template_fk` | `public.sales_tax_template_rows(template_id, merchant_id)` | `public.sales_tax_templates(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 6764 | - |
| `sales_tax_templates_category_fk` | `public.sales_tax_templates(tax_category_id, merchant_id)` | `public.tax_categories(id, merchant_id)` | `0..1` | `0..* *(cond: ((tax_category_id IS NOT NULL) AND (NOT disabled)))*` | RESTRICT/NO ACTION | 6772 | - |
| `sales_tax_templates_merchant_id_fkey` | `public.sales_tax_templates(merchant_id)` | `public.merchants(id)` | `1` | `0..* *(cond: is_default)*` | ON DELETE CASCADE | 6780 | - |
| `tax_categories_merchant_id_fkey` | `public.tax_categories(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6972 | - |
| `tax_presets_country_code_fkey` | `public.tax_presets(country_code)` | `public.countries(code)` | `1` | `0..*` | RESTRICT/NO ACTION | 6980 | - |
| `tax_rules_category_fk` | `public.tax_rules(tax_category_id, merchant_id)` | `public.tax_categories(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6988 | - |
| `tax_rules_item_group_fk` | `public.tax_rules(item_group_id, merchant_id)` | `public.item_groups(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6996 | - |
| `tax_rules_merchant_id_fkey` | `public.tax_rules(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 7004 | - |
| `tax_rules_template_fk` | `public.tax_rules(sales_tax_template_id, merchant_id)` | `public.sales_tax_templates(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 7012 | - |

---

### ERD-10 — Price lists and pricing rules

- **Primary Tables**: `price_lists`, `pricing_rules`, `pricing_rule_targets`
- **Outgoing FK Count**: 9
- **Status**: Ready for Drawing

#### Table Definitions

##### Table `public.price_lists` (SQL Line 2363)

- **Primary Key**: `price_lists_pkey` on `(id)` (Line 3515)
- **Unique Constraint**: `price_lists_id_merchant` on `(id, merchant_id)` (Line 3499)
- **Unique Constraint**: `price_lists_name_unique` on `(merchant_id, price_list_name)` (Line 3507)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (currencies), FK (merchants), FK (brands), FK (items), FK (item_groups), FK (merchants), FK (pricing_rules), FK (merchants), FK (price_lists) |
| `price_list_name` | `text` | NOT NULL | - | - |
| `currency` | `text` | NOT NULL | - | FK (currencies) |
| `enabled` | `boolean` | NOT NULL | `true` | - |
| `price_not_uom_dependent` | `boolean` | NOT NULL | `false` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

##### Table `public.pricing_rules` (SQL Line 2395)

- **Primary Key**: `pricing_rules_pkey` on `(id)` (Line 3539)
- **Unique Constraint**: `pricing_rules_id_merchant` on `(id, merchant_id)` (Line 3531)
- **Unique Constraint**: `pricing_rules_title_unique` on `(merchant_id, title)` (Line 3547)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (currencies), FK (merchants), FK (brands), FK (items), FK (item_groups), FK (merchants), FK (pricing_rules), FK (merchants), FK (price_lists) |
| `title` | `text` | NOT NULL | - | - |
| `apply_on` | `text` | NOT NULL | `''::text` | - |
| `min_qty` | `numeric` | NOT NULL | `0` | - |
| `max_qty` | `numeric` | NOT NULL | `0` | - |
| `min_amt` | `numeric` | NOT NULL | `0` | - |
| `max_amt` | `numeric` | NOT NULL | `0` | - |
| `valid_from` | `date` | NULL | - | - |
| `valid_upto` | `date` | NULL | - | - |
| `for_price_list` | `uuid` | NULL | - | FK (price_lists) |
| `priority` | `integer` | NOT NULL | `1` | - |
| `disable` | `boolean` | NOT NULL | `false` | - |
| `rate_or_discount` | `text` | NOT NULL | `''::text` | - |
| `rate` | `numeric` | NOT NULL | `0` | - |
| `discount_percentage` | `numeric` | NOT NULL | `0` | - |
| `discount_amount` | `numeric` | NOT NULL | `0` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

##### Table `public.pricing_rule_targets` (SQL Line 2379)

- **Primary Key**: `pricing_rule_targets_pkey` on `(id)` (Line 3523)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (currencies), FK (merchants), FK (brands), FK (items), FK (item_groups), FK (merchants), FK (pricing_rules), FK (merchants), FK (price_lists) |
| `pricing_rule_id` | `uuid` | NOT NULL | - | FK (pricing_rules) |
| `idx` | `integer` | NOT NULL | - | - |
| `item_id` | `uuid` | NULL | - | FK (items) |
| `item_group_id` | `uuid` | NULL | - | FK (item_groups) |
| `brand_id` | `uuid` | NULL | - | FK (brands) |

#### Declared Outgoing Foreign Keys

| Constraint Name | Child Columns | Referenced Entity | Parent End | Child End | Delete / Update Action | SQL Line | Connector ID |
|---|---|---|---|---|---|---|---|
| `price_lists_currency_fk` | `public.price_lists(merchant_id, currency)` | `public.currencies(merchant_id, code)` | `1` | `0..*` | RESTRICT/NO ACTION | 6628 | - |
| `price_lists_merchant_id_fkey` | `public.price_lists(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6636 | - |
| `pricing_rule_targets_brand_fk` | `public.pricing_rule_targets(brand_id, merchant_id)` | `public.brands(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6644 | - |
| `pricing_rule_targets_item_fk` | `public.pricing_rule_targets(item_id, merchant_id)` | `public.items(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6652 | - |
| `pricing_rule_targets_item_group_fk` | `public.pricing_rule_targets(item_group_id, merchant_id)` | `public.item_groups(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6660 | - |
| `pricing_rule_targets_merchant_id_fkey` | `public.pricing_rule_targets(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6668 | - |
| `pricing_rule_targets_rule_fk` | `public.pricing_rule_targets(pricing_rule_id, merchant_id)` | `public.pricing_rules(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 6676 | - |
| `pricing_rules_merchant_id_fkey` | `public.pricing_rules(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6684 | - |
| `pricing_rules_price_list_fk` | `public.pricing_rules(for_price_list, merchant_id)` | `public.price_lists(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6692 | - |

---

### ERD-11 — Document naming and receipt configuration

- **Primary Tables**: `naming_series`, `naming_series_counters`, `letter_heads`, `print_formats`
- **Outgoing FK Count**: 4
- **Status**: Ready for Drawing

#### Table Definitions

##### Table `public.naming_series` (SQL Line 2024)

- **Primary Key**: `naming_series_pkey` on `(merchant_id, document_type)` (Line 3259)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `merchant_id` | `uuid` | NOT NULL | - | PK, FK (merchants), FK (merchants), FK (merchants), FK (merchants) |
| `document_type` | `text` | NOT NULL | - | PK |
| `options` | `text[]` | NOT NULL | - | - |
| `user_must_select` | `boolean` | NOT NULL | `false` | - |

##### Table `public.naming_series_counters` (SQL Line 2038)

- **Primary Key**: `naming_series_counters_pkey` on `(merchant_id, prefix)` (Line 3251)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `merchant_id` | `uuid` | NOT NULL | - | PK, FK (merchants), FK (merchants), FK (merchants), FK (merchants) |
| `prefix` | `text` | NOT NULL | - | PK |
| `current_value` | `bigint` | NOT NULL | `0` | - |

##### Table `public.letter_heads` (SQL Line 1928)

- **Primary Key**: `letter_heads_pkey` on `(id)` (Line 3179)
- **Unique Constraint**: `letter_heads_id_merchant` on `(id, merchant_id)` (Line 3163)
- **Unique Constraint**: `letter_heads_name_unique` on `(merchant_id, letter_head_name)` (Line 3171)
- **Partial Unique Index**: `letter_heads_one_default` on `(merchant_id)` WHERE `is_default` (Line 4235)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (merchants), FK (merchants), FK (merchants), FK (merchants) |
| `letter_head_name` | `text` | NOT NULL | - | - |
| `content` | `text` | NOT NULL | `''::text` | - |
| `footer` | `text` | NOT NULL | `''::text` | - |
| `is_default` | `boolean` | NOT NULL | `false` | - |
| `disabled` | `boolean` | NOT NULL | `false` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

##### Table `public.print_formats` (SQL Line 2427)

- **Primary Key**: `print_formats_pkey` on `(id)` (Line 3571)
- **Unique Constraint**: `print_formats_id_merchant` on `(id, merchant_id)` (Line 3555)
- **Unique Constraint**: `print_formats_name_unique` on `(merchant_id, print_format_name)` (Line 3563)
- **Partial Unique Index**: `print_formats_one_default` on `(merchant_id)` WHERE `is_default` (Line 4704)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (merchants), FK (merchants), FK (merchants), FK (merchants) |
| `print_format_name` | `text` | NOT NULL | - | - |
| `paper` | `text` | NOT NULL | `''::text` | - |
| `print_heading` | `text` | NOT NULL | `''::text` | - |
| `show_item_code` | `boolean` | NOT NULL | `true` | - |
| `footer_note` | `text` | NOT NULL | `''::text` | - |
| `is_default` | `boolean` | NOT NULL | `false` | - |
| `disabled` | `boolean` | NOT NULL | `false` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

#### Declared Outgoing Foreign Keys

| Constraint Name | Child Columns | Referenced Entity | Parent End | Child End | Delete / Update Action | SQL Line | Connector ID |
|---|---|---|---|---|---|---|---|
| `letter_heads_merchant_id_fkey` | `public.letter_heads(merchant_id)` | `public.merchants(id)` | `1` | `0..* *(cond: is_default)*` | ON DELETE CASCADE | 5932 | - |
| `naming_series_counters_merchant_id_fkey` | `public.naming_series_counters(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6108 | - |
| `naming_series_merchant_id_fkey` | `public.naming_series(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6116 | - |
| `print_formats_merchant_id_fkey` | `public.print_formats(merchant_id)` | `public.merchants(id)` | `1` | `0..* *(cond: is_default)*` | ON DELETE CASCADE | 6700 | - |

---

### ERD-12 — POS profiles

- **Primary Tables**: `pos_profiles`, `pos_profile_users`, `pos_profile_item_groups`, `pos_profile_payments`
- **Outgoing FK Count**: 21
- **Status**: Ready for Drawing

#### Table Definitions

##### Table `public.pos_profiles` (SQL Line 2328)

- **Primary Key**: `pos_profiles_pkey` on `(id)` (Line 3491)
- **Unique Constraint**: `pos_profiles_id_merchant` on `(id, merchant_id)` (Line 3475)
- **Unique Constraint**: `pos_profiles_name_unique` on `(merchant_id, pos_profile_name)` (Line 3483)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (item_groups), FK (merchants), FK (pos_profiles), FK (merchants), FK (modes_of_payment), FK (pos_profiles), FK (merchant_members), FK (merchants), FK (pos_profiles), FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (letter_heads), FK (merchants), FK (price_lists), FK (print_formats), FK (tax_categories), FK (sales_tax_templates), FK (warehouses), FK (accounts) |
| `pos_profile_name` | `text` | NOT NULL | - | - |
| `disabled` | `boolean` | NOT NULL | `false` | - |
| `warehouse` | `uuid` | NOT NULL | - | FK (warehouses) |
| `selling_price_list` | `uuid` | NULL | - | FK (price_lists) |
| `taxes_and_charges` | `uuid` | NULL | - | FK (sales_tax_templates) |
| `tax_category` | `uuid` | NULL | - | FK (tax_categories) |
| `print_format` | `uuid` | NULL | - | FK (print_formats) |
| `letter_head` | `uuid` | NULL | - | FK (letter_heads) |
| `account_for_change_amount` | `uuid` | NULL | - | FK (accounts) |
| `write_off_account` | `uuid` | NULL | - | FK (accounts) |
| `write_off_limit` | `numeric` | NOT NULL | `0` | - |
| `income_account` | `uuid` | NULL | - | FK (accounts) |
| `expense_account` | `uuid` | NULL | - | FK (accounts) |
| `hide_unavailable_items` | `boolean` | NOT NULL | `false` | - |
| `allow_rate_change` | `boolean` | NOT NULL | `false` | - |
| `set_grand_total_to_default_mop` | `boolean` | NOT NULL | `true` | - |
| `print_receipt_on_order_complete` | `boolean` | NOT NULL | `false` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |
| `apply_discount_on` | `text` | NOT NULL | `''::text` | - |
| `allow_discount_change` | `boolean` | NOT NULL | `false` | - |
| `ignore_pricing_rule` | `boolean` | NOT NULL | `false` | - |
| `discount_account` | `uuid` | NULL | - | FK (accounts) |

##### Table `public.pos_profile_users` (SQL Line 2314)

- **Primary Key**: `pos_profile_users_pkey` on `(id)` (Line 3459)
- **Unique Constraint**: `pos_profile_users_unique` on `(pos_profile_id, member_id)` (Line 3467)
- **Partial Unique Index**: `pos_profile_users_one_default` on `(member_id)` WHERE `is_default` (Line 4585)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (item_groups), FK (merchants), FK (pos_profiles), FK (merchants), FK (modes_of_payment), FK (pos_profiles), FK (merchant_members), FK (merchants), FK (pos_profiles), FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (letter_heads), FK (merchants), FK (price_lists), FK (print_formats), FK (tax_categories), FK (sales_tax_templates), FK (warehouses), FK (accounts) |
| `pos_profile_id` | `uuid` | NOT NULL | - | FK (pos_profiles), FK (pos_profiles), FK (pos_profiles) |
| `idx` | `integer` | NOT NULL | - | - |
| `member_id` | `uuid` | NOT NULL | - | FK (merchant_members) |
| `is_default` | `boolean` | NOT NULL | `false` | - |

##### Table `public.pos_profile_item_groups` (SQL Line 2286)

- **Primary Key**: `pos_profile_item_groups_pkey` on `(id)` (Line 3427)
- **Unique Constraint**: `pos_profile_item_groups_unique` on `(pos_profile_id, item_group_id)` (Line 3435)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (item_groups), FK (merchants), FK (pos_profiles), FK (merchants), FK (modes_of_payment), FK (pos_profiles), FK (merchant_members), FK (merchants), FK (pos_profiles), FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (letter_heads), FK (merchants), FK (price_lists), FK (print_formats), FK (tax_categories), FK (sales_tax_templates), FK (warehouses), FK (accounts) |
| `pos_profile_id` | `uuid` | NOT NULL | - | FK (pos_profiles), FK (pos_profiles), FK (pos_profiles) |
| `idx` | `integer` | NOT NULL | - | - |
| `item_group_id` | `uuid` | NOT NULL | - | FK (item_groups) |

##### Table `public.pos_profile_payments` (SQL Line 2299)

- **Primary Key**: `pos_profile_payments_pkey` on `(id)` (Line 3443)
- **Unique Constraint**: `pos_profile_payments_unique` on `(pos_profile_id, mode_of_payment_id)` (Line 3451)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (item_groups), FK (merchants), FK (pos_profiles), FK (merchants), FK (modes_of_payment), FK (pos_profiles), FK (merchant_members), FK (merchants), FK (pos_profiles), FK (accounts), FK (accounts), FK (accounts), FK (accounts), FK (letter_heads), FK (merchants), FK (price_lists), FK (print_formats), FK (tax_categories), FK (sales_tax_templates), FK (warehouses), FK (accounts) |
| `pos_profile_id` | `uuid` | NOT NULL | - | FK (pos_profiles), FK (pos_profiles), FK (pos_profiles) |
| `idx` | `integer` | NOT NULL | - | - |
| `mode_of_payment_id` | `uuid` | NOT NULL | - | FK (modes_of_payment) |
| `is_default` | `boolean` | NOT NULL | `false` | - |
| `allow_in_returns` | `boolean` | NOT NULL | `false` | - |

#### Declared Outgoing Foreign Keys

| Constraint Name | Child Columns | Referenced Entity | Parent End | Child End | Delete / Update Action | SQL Line | Connector ID |
|---|---|---|---|---|---|---|---|
| `pos_profile_item_groups_group_fk` | `public.pos_profile_item_groups(item_group_id, merchant_id)` | `public.item_groups(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 6460 | - |
| `pos_profile_item_groups_merchant_id_fkey` | `public.pos_profile_item_groups(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6468 | - |
| `pos_profile_item_groups_profile_fk` | `public.pos_profile_item_groups(pos_profile_id, merchant_id)` | `public.pos_profiles(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 6476 | - |
| `pos_profile_payments_merchant_id_fkey` | `public.pos_profile_payments(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6484 | - |
| `pos_profile_payments_mode_fk` | `public.pos_profile_payments(mode_of_payment_id, merchant_id)` | `public.modes_of_payment(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 6492 | - |
| `pos_profile_payments_profile_fk` | `public.pos_profile_payments(pos_profile_id, merchant_id)` | `public.pos_profiles(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 6500 | - |
| `pos_profile_users_member_fk` | `public.pos_profile_users(member_id, merchant_id)` | `public.merchant_members(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 6508 | - |
| `pos_profile_users_merchant_id_fkey` | `public.pos_profile_users(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6516 | - |
| `pos_profile_users_profile_fk` | `public.pos_profile_users(pos_profile_id, merchant_id)` | `public.pos_profiles(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 6524 | - |
| `pos_profiles_change_account_fk` | `public.pos_profiles(account_for_change_amount, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6532 | - |
| `pos_profiles_discount_account_fk` | `public.pos_profiles(discount_account, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6540 | - |
| `pos_profiles_expense_account_fk` | `public.pos_profiles(expense_account, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6548 | - |
| `pos_profiles_income_account_fk` | `public.pos_profiles(income_account, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6556 | - |
| `pos_profiles_letter_head_fk` | `public.pos_profiles(letter_head, merchant_id)` | `public.letter_heads(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6564 | - |
| `pos_profiles_merchant_id_fkey` | `public.pos_profiles(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6572 | - |
| `pos_profiles_price_list_fk` | `public.pos_profiles(selling_price_list, merchant_id)` | `public.price_lists(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6580 | - |
| `pos_profiles_print_format_fk` | `public.pos_profiles(print_format, merchant_id)` | `public.print_formats(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6588 | - |
| `pos_profiles_tax_category_fk` | `public.pos_profiles(tax_category, merchant_id)` | `public.tax_categories(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6596 | - |
| `pos_profiles_template_fk` | `public.pos_profiles(taxes_and_charges, merchant_id)` | `public.sales_tax_templates(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6604 | - |
| `pos_profiles_warehouse_fk` | `public.pos_profiles(warehouse, merchant_id)` | `public.warehouses(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 6612 | - |
| `pos_profiles_write_off_account_fk` | `public.pos_profiles(write_off_account, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6620 | - |

---

### ERD-13 — Items and item-level configuration

- **Primary Tables**: `items`, `item_uoms`, `item_taxes`, `item_group_taxes`, `item_prices`
- **Outgoing FK Count**: 25
- **Status**: Ready for Drawing

#### Table Definitions

##### Table `public.items` (SQL Line 1892)

- **Primary Key**: `items_pkey` on `(id)` (Line 3155)
- **Unique Constraint**: `items_code_unique` on `(merchant_id, item_code)` (Line 3139)
- **Unique Constraint**: `items_id_merchant` on `(id, merchant_id)` (Line 3147)
- **Partial Unique Index**: `items_barcode_unique` on `(merchant_id, barcode)` WHERE `(barcode IS NOT NULL)` (Line 4165)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (tax_categories), FK (item_groups), FK (merchants), FK (item_tax_templates), FK (items), FK (merchants), FK (price_lists), FK (uoms), FK (tax_categories), FK (items), FK (merchants), FK (item_tax_templates), FK (items), FK (merchants), FK (uoms), FK (brands), FK (accounts), FK (accounts), FK (accounts), FK (item_groups), FK (merchants), FK (price_lists), FK (uoms), FK (uoms), FK (warehouses) |
| `item_code` | `text` | NOT NULL | - | - |
| `item_name` | `text` | NOT NULL | - | - |
| `item_group_id` | `uuid` | NOT NULL | - | FK (item_groups), FK (item_groups) |
| `stock_uom` | `uuid` | NOT NULL | - | FK (uoms) |
| `description` | `text` | NULL | - | - |
| `brand_id` | `uuid` | NULL | - | FK (brands) |
| `disabled` | `boolean` | NOT NULL | `false` | - |
| `is_stock_item` | `boolean` | NOT NULL | `true` | - |
| `valuation_method` | `text` | NULL | - | - |
| `allow_negative_stock` | `boolean` | NOT NULL | `false` | - |
| `reorder_level` | `numeric` | NULL | - | - |
| `sales_uom` | `uuid` | NULL | - | FK (uoms) |
| `default_warehouse` | `uuid` | NULL | - | FK (warehouses) |
| `default_price_list` | `uuid` | NULL | - | FK (price_lists) |
| `income_account` | `uuid` | NULL | - | FK (accounts) |
| `expense_account` | `uuid` | NULL | - | FK (accounts) |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |
| `max_discount` | `numeric` | NOT NULL | `0` | - |
| `discount_account` | `uuid` | NULL | - | FK (accounts) |
| `barcode` | `text` | NULL | - | - |

##### Table `public.item_uoms` (SQL Line 1877)

- **Primary Key**: `item_uoms_pkey` on `(id)` (Line 3123)
- **Unique Constraint**: `item_uoms_unique` on `(item_id, uom_id)` (Line 3131)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (tax_categories), FK (item_groups), FK (merchants), FK (item_tax_templates), FK (items), FK (merchants), FK (price_lists), FK (uoms), FK (tax_categories), FK (items), FK (merchants), FK (item_tax_templates), FK (items), FK (merchants), FK (uoms), FK (brands), FK (accounts), FK (accounts), FK (accounts), FK (item_groups), FK (merchants), FK (price_lists), FK (uoms), FK (uoms), FK (warehouses) |
| `item_id` | `uuid` | NOT NULL | - | FK (items), FK (items), FK (items) |
| `idx` | `integer` | NOT NULL | - | - |
| `uom_id` | `uuid` | NOT NULL | - | FK (uoms), FK (uoms) |
| `conversion_factor` | `numeric` | NOT NULL | - | - |

##### Table `public.item_taxes` (SQL Line 1862)

- **Primary Key**: `item_taxes_pkey` on `(id)` (Line 3115)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (tax_categories), FK (item_groups), FK (merchants), FK (item_tax_templates), FK (items), FK (merchants), FK (price_lists), FK (uoms), FK (tax_categories), FK (items), FK (merchants), FK (item_tax_templates), FK (items), FK (merchants), FK (uoms), FK (brands), FK (accounts), FK (accounts), FK (accounts), FK (item_groups), FK (merchants), FK (price_lists), FK (uoms), FK (uoms), FK (warehouses) |
| `item_id` | `uuid` | NOT NULL | - | FK (items), FK (items), FK (items) |
| `idx` | `integer` | NOT NULL | - | - |
| `item_tax_template_id` | `uuid` | NOT NULL | - | FK (item_tax_templates), FK (item_tax_templates) |
| `tax_category_id` | `uuid` | NULL | - | FK (tax_categories), FK (tax_categories) |
| `valid_from` | `date` | NULL | - | - |

##### Table `public.item_group_taxes` (SQL Line 1776)

- **Primary Key**: `item_group_taxes_pkey` on `(id)` (Line 3019)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (tax_categories), FK (item_groups), FK (merchants), FK (item_tax_templates), FK (items), FK (merchants), FK (price_lists), FK (uoms), FK (tax_categories), FK (items), FK (merchants), FK (item_tax_templates), FK (items), FK (merchants), FK (uoms), FK (brands), FK (accounts), FK (accounts), FK (accounts), FK (item_groups), FK (merchants), FK (price_lists), FK (uoms), FK (uoms), FK (warehouses) |
| `item_group_id` | `uuid` | NOT NULL | - | FK (item_groups), FK (item_groups) |
| `idx` | `integer` | NOT NULL | - | - |
| `item_tax_template_id` | `uuid` | NOT NULL | - | FK (item_tax_templates), FK (item_tax_templates) |
| `tax_category_id` | `uuid` | NULL | - | FK (tax_categories), FK (tax_categories) |
| `valid_from` | `date` | NULL | - | - |
| `minimum_net_rate` | `numeric` | NOT NULL | `0` | - |
| `maximum_net_rate` | `numeric` | NOT NULL | `0` | - |

##### Table `public.item_prices` (SQL Line 1814)

- **Primary Key**: `item_prices_pkey` on `(id)` (Line 3059)
- **Unique Constraint**: `item_prices_id_merchant` on `(id, merchant_id)` (Line 3051)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (tax_categories), FK (item_groups), FK (merchants), FK (item_tax_templates), FK (items), FK (merchants), FK (price_lists), FK (uoms), FK (tax_categories), FK (items), FK (merchants), FK (item_tax_templates), FK (items), FK (merchants), FK (uoms), FK (brands), FK (accounts), FK (accounts), FK (accounts), FK (item_groups), FK (merchants), FK (price_lists), FK (uoms), FK (uoms), FK (warehouses) |
| `item_id` | `uuid` | NOT NULL | - | FK (items), FK (items), FK (items) |
| `price_list_id` | `uuid` | NOT NULL | - | FK (price_lists) |
| `uom_id` | `uuid` | NOT NULL | - | FK (uoms), FK (uoms) |
| `price_list_rate` | `numeric` | NOT NULL | - | - |
| `valid_from` | `date` | NULL | - | - |
| `valid_upto` | `date` | NULL | - | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

#### Declared Outgoing Foreign Keys

| Constraint Name | Child Columns | Referenced Entity | Parent End | Child End | Delete / Update Action | SQL Line | Connector ID |
|---|---|---|---|---|---|---|---|
| `item_group_taxes_category_fk` | `public.item_group_taxes(tax_category_id, merchant_id)` | `public.tax_categories(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5652 | - |
| `item_group_taxes_group_fk` | `public.item_group_taxes(item_group_id, merchant_id)` | `public.item_groups(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 5660 | - |
| `item_group_taxes_merchant_id_fkey` | `public.item_group_taxes(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 5668 | - |
| `item_group_taxes_template_fk` | `public.item_group_taxes(item_tax_template_id, merchant_id)` | `public.item_tax_templates(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 5676 | - |
| `item_prices_item_fk` | `public.item_prices(item_id, merchant_id)` | `public.items(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 5732 | - |
| `item_prices_merchant_id_fkey` | `public.item_prices(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 5740 | - |
| `item_prices_price_list_fk` | `public.item_prices(price_list_id, merchant_id)` | `public.price_lists(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 5748 | - |
| `item_prices_uom_fk` | `public.item_prices(uom_id, merchant_id)` | `public.uoms(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 5756 | - |
| `item_taxes_category_fk` | `public.item_taxes(tax_category_id, merchant_id)` | `public.tax_categories(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5796 | - |
| `item_taxes_item_fk` | `public.item_taxes(item_id, merchant_id)` | `public.items(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 5804 | - |
| `item_taxes_merchant_id_fkey` | `public.item_taxes(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 5812 | - |
| `item_taxes_template_fk` | `public.item_taxes(item_tax_template_id, merchant_id)` | `public.item_tax_templates(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 5820 | - |
| `item_uoms_item_fk` | `public.item_uoms(item_id, merchant_id)` | `public.items(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 5828 | - |
| `item_uoms_merchant_id_fkey` | `public.item_uoms(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 5836 | - |
| `item_uoms_uom_fk` | `public.item_uoms(uom_id, merchant_id)` | `public.uoms(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 5844 | - |
| `items_brand_fk` | `public.items(brand_id, merchant_id)` | `public.brands(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5852 | - |
| `items_discount_account_fk` | `public.items(discount_account, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5860 | - |
| `items_expense_account_fk` | `public.items(expense_account, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5868 | - |
| `items_income_account_fk` | `public.items(income_account, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5876 | - |
| `items_item_group_fk` | `public.items(item_group_id, merchant_id)` | `public.item_groups(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 5884 | - |
| `items_merchant_id_fkey` | `public.items(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 5892 | - |
| `items_price_list_fk` | `public.items(default_price_list, merchant_id)` | `public.price_lists(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5900 | - |
| `items_sales_uom_fk` | `public.items(sales_uom, merchant_id)` | `public.uoms(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5908 | - |
| `items_stock_uom_fk` | `public.items(stock_uom, merchant_id)` | `public.uoms(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 5916 | - |
| `items_warehouse_fk` | `public.items(default_warehouse, merchant_id)` | `public.warehouses(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 5924 | - |

---

### ERD-14 — Inventory balances and transactions

- **Primary Tables**: `bins`, `stock_entries`, `stock_entry_items`, `stock_reconciliations`, `stock_reconciliation_items`, `stock_ledger_entries`
- **Outgoing FK Count**: 19
- **Status**: Ready for Drawing

#### Table Definitions

##### Table `public.bins` (SQL Line 44)

- **Primary Key**: `bins_pkey` on `(item_id, warehouse_id)` (Line 2875)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `merchant_id` | `uuid` | NOT NULL | - | FK (items), FK (merchants), FK (warehouses), FK (accounts), FK (warehouses), FK (merchants), FK (warehouses), FK (items), FK (merchants), FK (stock_entries), FK (items), FK (merchants), FK (warehouses), FK (items), FK (merchants), FK (stock_reconciliations), FK (warehouses), FK (accounts), FK (merchants) |
| `item_id` | `uuid` | NOT NULL | - | PK, FK (items), FK (items), FK (items), FK (items) |
| `warehouse_id` | `uuid` | NOT NULL | - | PK, FK (warehouses), FK (warehouses), FK (warehouses) |
| `actual_qty` | `numeric` | NOT NULL | `0` | - |
| `valuation_rate` | `numeric` | NOT NULL | `0` | - |
| `stock_value` | `numeric` | NOT NULL | `0` | - |
| `fifo_queue` | `jsonb` | NOT NULL | `''::jsonb` | - |
| `last_posting_date` | `date` | NULL | - | - |

##### Table `public.stock_entries` (SQL Line 2560)

- **Primary Key**: `stock_entries_pkey` on `(id)` (Line 3691)
- **Unique Constraint**: `stock_entries_id_merchant` on `(id, merchant_id)` (Line 3675)
- **Unique Constraint**: `stock_entries_name_unique` on `(merchant_id, name)` (Line 3683)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (items), FK (merchants), FK (warehouses), FK (accounts), FK (warehouses), FK (merchants), FK (warehouses), FK (items), FK (merchants), FK (stock_entries), FK (items), FK (merchants), FK (warehouses), FK (items), FK (merchants), FK (stock_reconciliations), FK (warehouses), FK (accounts), FK (merchants) |
| `name` | `text` | NOT NULL | - | - |
| `posting_date` | `date` | NOT NULL | - | - |
| `purpose` | `text` | NOT NULL | - | - |
| `from_warehouse` | `uuid` | NULL | - | FK (warehouses) |
| `to_warehouse` | `uuid` | NULL | - | FK (warehouses) |
| `difference_account` | `uuid` | NULL | - | FK (accounts), FK (accounts) |
| `docstatus` | `smallint` | NOT NULL | `0` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

##### Table `public.stock_entry_items` (SQL Line 2586)

- **Primary Key**: `stock_entry_items_pkey` on `(id)` (Line 3699)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (items), FK (merchants), FK (warehouses), FK (accounts), FK (warehouses), FK (merchants), FK (warehouses), FK (items), FK (merchants), FK (stock_entries), FK (items), FK (merchants), FK (warehouses), FK (items), FK (merchants), FK (stock_reconciliations), FK (warehouses), FK (accounts), FK (merchants) |
| `stock_entry_id` | `uuid` | NOT NULL | - | FK (stock_entries) |
| `idx` | `integer` | NOT NULL | - | - |
| `item_id` | `uuid` | NOT NULL | - | FK (items), FK (items), FK (items), FK (items) |
| `qty` | `numeric` | NOT NULL | - | - |
| `basic_rate` | `numeric` | NULL | - | - |
| `amount` | `numeric` | NULL | - | - |

##### Table `public.stock_reconciliations` (SQL Line 2663)

- **Primary Key**: `stock_reconciliations_pkey` on `(id)` (Line 3747)
- **Unique Constraint**: `stock_reconciliations_id_merchant` on `(id, merchant_id)` (Line 3731)
- **Unique Constraint**: `stock_reconciliations_name_unique` on `(merchant_id, name)` (Line 3739)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (items), FK (merchants), FK (warehouses), FK (accounts), FK (warehouses), FK (merchants), FK (warehouses), FK (items), FK (merchants), FK (stock_entries), FK (items), FK (merchants), FK (warehouses), FK (items), FK (merchants), FK (stock_reconciliations), FK (warehouses), FK (accounts), FK (merchants) |
| `name` | `text` | NOT NULL | - | - |
| `posting_date` | `date` | NOT NULL | - | - |
| `purpose` | `text` | NOT NULL | `''::text` | - |
| `difference_account` | `uuid` | NULL | - | FK (accounts), FK (accounts) |
| `docstatus` | `smallint` | NOT NULL | `0` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

##### Table `public.stock_reconciliation_items` (SQL Line 2642)

- **Primary Key**: `stock_reconciliation_items_pkey` on `(id)` (Line 3715)
- **Unique Constraint**: `stock_reconciliation_items_unique` on `(stock_reconciliation_id, item_id, warehouse_id)` (Line 3723)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (items), FK (merchants), FK (warehouses), FK (accounts), FK (warehouses), FK (merchants), FK (warehouses), FK (items), FK (merchants), FK (stock_entries), FK (items), FK (merchants), FK (warehouses), FK (items), FK (merchants), FK (stock_reconciliations), FK (warehouses), FK (accounts), FK (merchants) |
| `stock_reconciliation_id` | `uuid` | NOT NULL | - | FK (stock_reconciliations) |
| `idx` | `integer` | NOT NULL | - | - |
| `item_id` | `uuid` | NOT NULL | - | FK (items), FK (items), FK (items), FK (items) |
| `warehouse_id` | `uuid` | NOT NULL | - | FK (warehouses), FK (warehouses), FK (warehouses) |
| `qty` | `numeric` | NOT NULL | - | - |
| `valuation_rate` | `numeric` | NOT NULL | - | - |
| `current_qty` | `numeric` | NULL | - | - |
| `current_valuation_rate` | `numeric` | NULL | - | - |
| `amount_difference` | `numeric` | NULL | - | - |

##### Table `public.stock_ledger_entries` (SQL Line 2604)

- **Primary Key**: `stock_ledger_entries_pkey` on `(id)` (Line 3707)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `bigint` | NOT NULL | - | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (items), FK (merchants), FK (warehouses), FK (accounts), FK (warehouses), FK (merchants), FK (warehouses), FK (items), FK (merchants), FK (stock_entries), FK (items), FK (merchants), FK (warehouses), FK (items), FK (merchants), FK (stock_reconciliations), FK (warehouses), FK (accounts), FK (merchants) |
| `posting_date` | `date` | NOT NULL | - | - |
| `item_id` | `uuid` | NOT NULL | - | FK (items), FK (items), FK (items), FK (items) |
| `warehouse_id` | `uuid` | NOT NULL | - | FK (warehouses), FK (warehouses), FK (warehouses) |
| `actual_qty` | `numeric` | NOT NULL | - | - |
| `incoming_rate` | `numeric` | NOT NULL | `0` | - |
| `valuation_rate` | `numeric` | NOT NULL | `0` | - |
| `qty_after_transaction` | `numeric` | NOT NULL | - | - |
| `stock_value` | `numeric` | NOT NULL | - | - |
| `stock_value_difference` | `numeric` | NOT NULL | - | - |
| `voucher_type` | `text` | NOT NULL | - | - |
| `voucher_id` | `uuid` | NOT NULL | - | - |
| `voucher_no` | `text` | NOT NULL | - | - |
| `is_cancelled` | `boolean` | NOT NULL | `false` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

#### Declared Outgoing Foreign Keys

| Constraint Name | Child Columns | Referenced Entity | Parent End | Child End | Delete / Update Action | SQL Line | Connector ID |
|---|---|---|---|---|---|---|---|
| `bins_item_fk` | `public.bins(item_id, merchant_id)` | `public.items(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 5524 | - |
| `bins_merchant_id_fkey` | `public.bins(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 5532 | - |
| `bins_warehouse_fk` | `public.bins(warehouse_id, merchant_id)` | `public.warehouses(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 5540 | - |
| `stock_entries_account_fk` | `public.stock_entries(difference_account, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6804 | - |
| `stock_entries_from_warehouse_fk` | `public.stock_entries(from_warehouse, merchant_id)` | `public.warehouses(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6812 | - |
| `stock_entries_merchant_id_fkey` | `public.stock_entries(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6820 | - |
| `stock_entries_to_warehouse_fk` | `public.stock_entries(to_warehouse, merchant_id)` | `public.warehouses(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6828 | - |
| `stock_entry_items_item_fk` | `public.stock_entry_items(item_id, merchant_id)` | `public.items(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 6836 | - |
| `stock_entry_items_merchant_id_fkey` | `public.stock_entry_items(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6844 | - |
| `stock_entry_items_parent_fk` | `public.stock_entry_items(stock_entry_id, merchant_id)` | `public.stock_entries(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 6852 | - |
| `stock_ledger_entries_item_fk` | `public.stock_ledger_entries(item_id, merchant_id)` | `public.items(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 6860 | - |
| `stock_ledger_entries_merchant_id_fkey` | `public.stock_ledger_entries(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6868 | - |
| `stock_ledger_entries_warehouse_fk` | `public.stock_ledger_entries(warehouse_id, merchant_id)` | `public.warehouses(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 6876 | - |
| `stock_reconciliation_items_item_fk` | `public.stock_reconciliation_items(item_id, merchant_id)` | `public.items(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 6884 | - |
| `stock_reconciliation_items_merchant_id_fkey` | `public.stock_reconciliation_items(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6892 | - |
| `stock_reconciliation_items_parent_fk` | `public.stock_reconciliation_items(stock_reconciliation_id, merchant_id)` | `public.stock_reconciliations(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 6900 | - |
| `stock_reconciliation_items_warehouse_fk` | `public.stock_reconciliation_items(warehouse_id, merchant_id)` | `public.warehouses(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 6908 | - |
| `stock_reconciliations_account_fk` | `public.stock_reconciliations(difference_account, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6916 | - |
| `stock_reconciliations_merchant_id_fkey` | `public.stock_reconciliations(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6924 | - |

---

### ERD-15 — POS opening sessions

- **Primary Tables**: `pos_opening_entries`, `pos_opening_entry_balances`
- **Outgoing FK Count**: 5
- **Status**: Ready for Drawing

#### Table Definitions

##### Table `public.pos_opening_entries` (SQL Line 2251)

- **Primary Key**: `pos_opening_entries_pkey` on `(id)` (Line 3403)
- **Unique Constraint**: `pos_opening_entries_id_merchant` on `(id, merchant_id)` (Line 3387)
- **Unique Constraint**: `pos_opening_entries_name_unique` on `(merchant_id, name)` (Line 3395)
- **Partial Unique Index**: `pos_opening_entries_one_open` on `(pos_profile_id, user_id)` WHERE `((docstatus = 1) AND (status = 'Open'::text))` (Line 4529)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (merchants), FK (pos_profiles), FK (merchants), FK (modes_of_payment), FK (pos_opening_entries) |
| `name` | `text` | NOT NULL | - | - |
| `posting_date` | `date` | NOT NULL | - | - |
| `pos_profile_id` | `uuid` | NOT NULL | - | FK (pos_profiles) |
| `user_id` | `uuid` | NOT NULL | `auth.uid()` | - |
| `period_start` | `timestamp with time zone` | NOT NULL | `now()` | - |
| `status` | `text` | NOT NULL | `''::text` | - |
| `docstatus` | `smallint` | NOT NULL | `0` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

##### Table `public.pos_opening_entry_balances` (SQL Line 2271)

- **Primary Key**: `pos_opening_entry_balances_pkey` on `(id)` (Line 3411)
- **Unique Constraint**: `pos_opening_entry_balances_unique` on `(pos_opening_entry_id, mode_of_payment_id)` (Line 3419)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (merchants), FK (pos_profiles), FK (merchants), FK (modes_of_payment), FK (pos_opening_entries) |
| `pos_opening_entry_id` | `uuid` | NOT NULL | - | FK (pos_opening_entries) |
| `idx` | `integer` | NOT NULL | - | - |
| `mode_of_payment_id` | `uuid` | NOT NULL | - | FK (modes_of_payment) |
| `opening_amount` | `numeric` | NOT NULL | `0` | - |

#### Declared Outgoing Foreign Keys

| Constraint Name | Child Columns | Referenced Entity | Parent End | Child End | Delete / Update Action | SQL Line | Connector ID |
|---|---|---|---|---|---|---|---|
| `pos_opening_entries_merchant_id_fkey` | `public.pos_opening_entries(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6420 | - |
| `pos_opening_entries_profile_fk` | `public.pos_opening_entries(pos_profile_id, merchant_id)` | `public.pos_profiles(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 6428 | - |
| `pos_opening_entry_balances_merchant_id_fkey` | `public.pos_opening_entry_balances(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6436 | - |
| `pos_opening_entry_balances_mode_fk` | `public.pos_opening_entry_balances(mode_of_payment_id, merchant_id)` | `public.modes_of_payment(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 6444 | - |
| `pos_opening_entry_balances_parent_fk` | `public.pos_opening_entry_balances(pos_opening_entry_id, merchant_id)` | `public.pos_opening_entries(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 6452 | - |

---

### ERD-16 — Sales invoices and returns

- **Primary Tables**: `pos_invoices`, `pos_invoice_items`, `pos_invoice_payments`, `pos_invoice_taxes`
- **Outgoing FK Count**: 26
- **Status**: Ready for Drawing

#### Table Definitions

##### Table `public.pos_invoices` (SQL Line 2209)

- **Primary Key**: `pos_invoices_pkey` on `(id)` (Line 3379)
- **Unique Constraint**: `pos_invoices_id_merchant` on `(id, merchant_id)` (Line 3363)
- **Unique Constraint**: `pos_invoices_name_unique` on `(merchant_id, name)` (Line 3371)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (accounts), FK (accounts), FK (accounts), FK (items), FK (merchants), FK (pos_invoices), FK (pricing_rules), FK (pos_invoice_items), FK (item_tax_templates), FK (uoms), FK (accounts), FK (merchants), FK (modes_of_payment), FK (pos_invoices), FK (accounts), FK (merchants), FK (pos_invoices), FK (accounts), FK (merchants), FK (price_lists), FK (pos_profiles), FK (pos_invoices), FK (pos_opening_entries), FK (tax_categories), FK (sales_tax_templates), FK (warehouses) |
| `name` | `text` | NOT NULL | - | - |
| `posting_date` | `date` | NOT NULL | - | - |
| `pos_profile_id` | `uuid` | NOT NULL | - | FK (pos_profiles) |
| `pos_opening_entry_id` | `uuid` | NOT NULL | - | FK (pos_opening_entries) |
| `user_id` | `uuid` | NOT NULL | `auth.uid()` | - |
| `warehouse` | `uuid` | NULL | - | FK (warehouses) |
| `selling_price_list` | `uuid` | NULL | - | FK (price_lists) |
| `taxes_and_charges` | `uuid` | NULL | - | FK (sales_tax_templates) |
| `tax_category` | `uuid` | NULL | - | FK (tax_categories) |
| `net_total` | `numeric` | NOT NULL | `0` | - |
| `total_taxes_and_charges` | `numeric` | NOT NULL | `0` | - |
| `grand_total` | `numeric` | NOT NULL | `0` | - |
| `rounding_adjustment` | `numeric` | NOT NULL | `0` | - |
| `rounded_total` | `numeric` | NOT NULL | `0` | - |
| `paid_amount` | `numeric` | NOT NULL | `0` | - |
| `change_amount` | `numeric` | NOT NULL | `0` | - |
| `write_off_amount` | `numeric` | NOT NULL | `0` | - |
| `docstatus` | `smallint` | NOT NULL | `0` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |
| `is_return` | `boolean` | NOT NULL | `false` | - |
| `return_against` | `uuid` | NULL | - | FK (pos_invoices) |
| `apply_discount_on` | `text` | NOT NULL | `''::text` | - |
| `additional_discount_percentage` | `numeric` | NOT NULL | `0` | - |
| `discount_amount` | `numeric` | NOT NULL | `0` | - |
| `additional_discount_account` | `uuid` | NULL | - | FK (accounts) |

##### Table `public.pos_invoice_items` (SQL Line 2134)

- **Primary Key**: `pos_invoice_items_pkey` on `(id)` (Line 3339)
- **Unique Constraint**: `pos_invoice_items_id_merchant` on `(id, merchant_id)` (Line 3331)
- **Partial Unique Index**: `pos_invoice_items_return_once` on `(pos_invoice_id, return_against_item)` WHERE `(return_against_item IS NOT NULL)` (Line 4403)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (accounts), FK (accounts), FK (accounts), FK (items), FK (merchants), FK (pos_invoices), FK (pricing_rules), FK (pos_invoice_items), FK (item_tax_templates), FK (uoms), FK (accounts), FK (merchants), FK (modes_of_payment), FK (pos_invoices), FK (accounts), FK (merchants), FK (pos_invoices), FK (accounts), FK (merchants), FK (price_lists), FK (pos_profiles), FK (pos_invoices), FK (pos_opening_entries), FK (tax_categories), FK (sales_tax_templates), FK (warehouses) |
| `pos_invoice_id` | `uuid` | NOT NULL | - | FK (pos_invoices), FK (pos_invoices), FK (pos_invoices) |
| `idx` | `integer` | NOT NULL | - | - |
| `item_id` | `uuid` | NOT NULL | - | FK (items) |
| `item_name` | `text` | NULL | - | - |
| `qty` | `numeric` | NOT NULL | - | - |
| `uom_id` | `uuid` | NOT NULL | - | FK (uoms) |
| `conversion_factor` | `numeric` | NOT NULL | `1` | - |
| `stock_qty` | `numeric` | NOT NULL | - | - |
| `price_list_rate` | `numeric` | NOT NULL | `0` | - |
| `rate` | `numeric` | NOT NULL | - | - |
| `amount` | `numeric` | NOT NULL | - | - |
| `net_rate` | `numeric` | NOT NULL | - | - |
| `net_amount` | `numeric` | NOT NULL | - | - |
| `item_tax_template_id` | `uuid` | NULL | - | FK (item_tax_templates) |
| `income_account` | `uuid` | NULL | - | FK (accounts) |
| `expense_account` | `uuid` | NULL | - | FK (accounts) |
| `valuation_rate` | `numeric` | NULL | - | - |
| `return_against_item` | `uuid` | NULL | - | FK (pos_invoice_items) |
| `discount_percentage` | `numeric` | NOT NULL | `0` | - |
| `discount_amount` | `numeric` | NOT NULL | `0` | - |
| `distributed_discount_amount` | `numeric` | NOT NULL | `0` | - |
| `pricing_rule_id` | `uuid` | NULL | - | FK (pricing_rules) |
| `discount_account` | `uuid` | NULL | - | FK (accounts) |

##### Table `public.pos_invoice_payments` (SQL Line 2170)

- **Primary Key**: `pos_invoice_payments_pkey` on `(id)` (Line 3347)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (accounts), FK (accounts), FK (accounts), FK (items), FK (merchants), FK (pos_invoices), FK (pricing_rules), FK (pos_invoice_items), FK (item_tax_templates), FK (uoms), FK (accounts), FK (merchants), FK (modes_of_payment), FK (pos_invoices), FK (accounts), FK (merchants), FK (pos_invoices), FK (accounts), FK (merchants), FK (price_lists), FK (pos_profiles), FK (pos_invoices), FK (pos_opening_entries), FK (tax_categories), FK (sales_tax_templates), FK (warehouses) |
| `pos_invoice_id` | `uuid` | NOT NULL | - | FK (pos_invoices), FK (pos_invoices), FK (pos_invoices) |
| `idx` | `integer` | NOT NULL | - | - |
| `mode_of_payment_id` | `uuid` | NOT NULL | - | FK (modes_of_payment) |
| `amount` | `numeric` | NOT NULL | - | - |
| `account` | `uuid` | NULL | - | FK (accounts) |

##### Table `public.pos_invoice_taxes` (SQL Line 2186)

- **Primary Key**: `pos_invoice_taxes_pkey` on `(id)` (Line 3355)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (accounts), FK (accounts), FK (accounts), FK (items), FK (merchants), FK (pos_invoices), FK (pricing_rules), FK (pos_invoice_items), FK (item_tax_templates), FK (uoms), FK (accounts), FK (merchants), FK (modes_of_payment), FK (pos_invoices), FK (accounts), FK (merchants), FK (pos_invoices), FK (accounts), FK (merchants), FK (price_lists), FK (pos_profiles), FK (pos_invoices), FK (pos_opening_entries), FK (tax_categories), FK (sales_tax_templates), FK (warehouses) |
| `pos_invoice_id` | `uuid` | NOT NULL | - | FK (pos_invoices), FK (pos_invoices), FK (pos_invoices) |
| `idx` | `integer` | NOT NULL | - | - |
| `charge_type` | `text` | NOT NULL | - | - |
| `account_head` | `uuid` | NOT NULL | - | FK (accounts) |
| `description` | `text` | NOT NULL | - | - |
| `rate` | `numeric` | NOT NULL | `0` | - |
| `row_id` | `integer` | NULL | - | - |
| `included_in_print_rate` | `boolean` | NOT NULL | `false` | - |
| `tax_amount` | `numeric` | NOT NULL | `0` | - |
| `total` | `numeric` | NOT NULL | `0` | - |
| `item_wise_tax_detail` | `jsonb` | NOT NULL | `''::jsonb` | - |

#### Declared Outgoing Foreign Keys

| Constraint Name | Child Columns | Referenced Entity | Parent End | Child End | Delete / Update Action | SQL Line | Connector ID |
|---|---|---|---|---|---|---|---|
| `pos_invoice_items_discount_account_fk` | `public.pos_invoice_items(discount_account, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6212 | - |
| `pos_invoice_items_expense_fk` | `public.pos_invoice_items(expense_account, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6220 | - |
| `pos_invoice_items_income_fk` | `public.pos_invoice_items(income_account, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6228 | - |
| `pos_invoice_items_item_fk` | `public.pos_invoice_items(item_id, merchant_id)` | `public.items(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 6236 | - |
| `pos_invoice_items_merchant_id_fkey` | `public.pos_invoice_items(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6244 | - |
| `pos_invoice_items_parent_fk` | `public.pos_invoice_items(pos_invoice_id, merchant_id)` | `public.pos_invoices(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 6252 | - |
| `pos_invoice_items_pricing_rule_fk` | `public.pos_invoice_items(pricing_rule_id, merchant_id)` | `public.pricing_rules(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6260 | - |
| `pos_invoice_items_return_fk` | `public.pos_invoice_items(return_against_item, merchant_id)` | `public.pos_invoice_items(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6268 | - |
| `pos_invoice_items_template_fk` | `public.pos_invoice_items(item_tax_template_id, merchant_id)` | `public.item_tax_templates(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6276 | - |
| `pos_invoice_items_uom_fk` | `public.pos_invoice_items(uom_id, merchant_id)` | `public.uoms(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 6284 | - |
| `pos_invoice_payments_account_fk` | `public.pos_invoice_payments(account, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6292 | - |
| `pos_invoice_payments_merchant_id_fkey` | `public.pos_invoice_payments(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6300 | - |
| `pos_invoice_payments_mode_fk` | `public.pos_invoice_payments(mode_of_payment_id, merchant_id)` | `public.modes_of_payment(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 6308 | - |
| `pos_invoice_payments_parent_fk` | `public.pos_invoice_payments(pos_invoice_id, merchant_id)` | `public.pos_invoices(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 6316 | - |
| `pos_invoice_taxes_account_fk` | `public.pos_invoice_taxes(account_head, merchant_id)` | `public.accounts(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 6324 | - |
| `pos_invoice_taxes_merchant_id_fkey` | `public.pos_invoice_taxes(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6332 | - |
| `pos_invoice_taxes_parent_fk` | `public.pos_invoice_taxes(pos_invoice_id, merchant_id)` | `public.pos_invoices(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 6340 | - |
| `pos_invoices_discount_account_fk` | `public.pos_invoices(additional_discount_account, merchant_id)` | `public.accounts(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6348 | - |
| `pos_invoices_merchant_id_fkey` | `public.pos_invoices(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6356 | - |
| `pos_invoices_price_list_fk` | `public.pos_invoices(selling_price_list, merchant_id)` | `public.price_lists(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6364 | - |
| `pos_invoices_profile_fk` | `public.pos_invoices(pos_profile_id, merchant_id)` | `public.pos_profiles(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 6372 | - |
| `pos_invoices_return_fk` | `public.pos_invoices(return_against, merchant_id)` | `public.pos_invoices(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6380 | - |
| `pos_invoices_session_fk` | `public.pos_invoices(pos_opening_entry_id, merchant_id)` | `public.pos_opening_entries(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 6388 | - |
| `pos_invoices_tax_category_fk` | `public.pos_invoices(tax_category, merchant_id)` | `public.tax_categories(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6396 | - |
| `pos_invoices_template_fk` | `public.pos_invoices(taxes_and_charges, merchant_id)` | `public.sales_tax_templates(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6404 | - |
| `pos_invoices_warehouse_fk` | `public.pos_invoices(warehouse, merchant_id)` | `public.warehouses(id, merchant_id)` | `0..1` | `0..*` | RESTRICT/NO ACTION | 6412 | - |

---

### ERD-17 — POS closing sessions

- **Primary Tables**: `pos_closing_entries`, `pos_closing_entry_payments`
- **Outgoing FK Count**: 5
- **Status**: Ready for Drawing

#### Table Definitions

##### Table `public.pos_closing_entries` (SQL Line 2095)

- **Primary Key**: `pos_closing_entries_pkey` on `(id)` (Line 3307)
- **Unique Constraint**: `pos_closing_entries_id_merchant` on `(id, merchant_id)` (Line 3291)
- **Unique Constraint**: `pos_closing_entries_name_unique` on `(merchant_id, name)` (Line 3299)
- **Partial Unique Index**: `pos_closing_entries_one_per_session` on `(pos_opening_entry_id)` WHERE `(docstatus = 1)` (Line 4333)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (merchants), FK (pos_opening_entries), FK (merchants), FK (modes_of_payment), FK (pos_closing_entries) |
| `name` | `text` | NOT NULL | - | - |
| `posting_date` | `date` | NOT NULL | - | - |
| `pos_opening_entry_id` | `uuid` | NOT NULL | - | FK (pos_opening_entries) |
| `user_id` | `uuid` | NOT NULL | `auth.uid()` | - |
| `period_end` | `timestamp with time zone` | NOT NULL | `now()` | - |
| `grand_total` | `numeric` | NOT NULL | `0` | - |
| `net_total` | `numeric` | NOT NULL | `0` | - |
| `total_quantity` | `numeric` | NOT NULL | `0` | - |
| `docstatus` | `smallint` | NOT NULL | `0` | - |
| `created_at` | `timestamp with time zone` | NOT NULL | `now()` | - |

##### Table `public.pos_closing_entry_payments` (SQL Line 2116)

- **Primary Key**: `pos_closing_entry_payments_pkey` on `(id)` (Line 3315)
- **Unique Constraint**: `pos_closing_entry_payments_unique` on `(pos_closing_entry_id, mode_of_payment_id)` (Line 3323)

| Column Name | Data Type | Nullability | Default Value | Key Role |
|---|---|---|---|---|
| `id` | `uuid` | NOT NULL | `gen_random_uuid()` | PK |
| `merchant_id` | `uuid` | NOT NULL | - | FK (merchants), FK (pos_opening_entries), FK (merchants), FK (modes_of_payment), FK (pos_closing_entries) |
| `pos_closing_entry_id` | `uuid` | NOT NULL | - | FK (pos_closing_entries) |
| `idx` | `integer` | NOT NULL | - | - |
| `mode_of_payment_id` | `uuid` | NOT NULL | - | FK (modes_of_payment) |
| `closing_amount` | `numeric` | NOT NULL | `0` | - |
| `opening_amount` | `numeric` | NOT NULL | `0` | - |
| `expected_amount` | `numeric` | NOT NULL | `0` | - |
| `difference` | `numeric` | NOT NULL | `0` | - |

#### Declared Outgoing Foreign Keys

| Constraint Name | Child Columns | Referenced Entity | Parent End | Child End | Delete / Update Action | SQL Line | Connector ID |
|---|---|---|---|---|---|---|---|
| `pos_closing_entries_merchant_id_fkey` | `public.pos_closing_entries(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6172 | - |
| `pos_closing_entries_session_fk` | `public.pos_closing_entries(pos_opening_entry_id, merchant_id)` | `public.pos_opening_entries(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 6180 | - |
| `pos_closing_entry_payments_merchant_id_fkey` | `public.pos_closing_entry_payments(merchant_id)` | `public.merchants(id)` | `1` | `0..*` | ON DELETE CASCADE | 6188 | - |
| `pos_closing_entry_payments_mode_fk` | `public.pos_closing_entry_payments(mode_of_payment_id, merchant_id)` | `public.modes_of_payment(id, merchant_id)` | `1` | `0..*` | RESTRICT/NO ACTION | 6196 | - |
| `pos_closing_entry_payments_parent_fk` | `public.pos_closing_entry_payments(pos_closing_entry_id, merchant_id)` | `public.pos_closing_entries(id, merchant_id)` | `1` | `0..*` | ON DELETE CASCADE | 6204 | - |

---
