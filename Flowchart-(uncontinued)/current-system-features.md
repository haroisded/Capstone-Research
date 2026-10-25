# 1) Store Creation Form

## 1) Store Creation Form

### 1) Feature Itself

- The feature is a full page in two steps. A bar at the top shows **STEP 1 OF 2** or **STEP 2 OF 2**, the step's title and
  a progress line.
- Tap **Create New Store** on the **Home** tab. The page opens on step 1, **Your store**, titled **Name your store**.
- Step 1 has three fields. All three are required.
  - **STORE NAME**: text.
  - **COUNTRY**: one country from a list.
  - **DEFAULT CURRENCY**: one currency. It is the currency the books are kept in.
- Step 1 has one button: **Next**. It checks the three fields first.
- Step 2, **Its level**, is titled **How much do you want to manage?**. It lists the five store levels in one box, each with
  its name, one line and what it gives (see 20) Store Levels). **Level 1 · Just Sell** is picked to start with.
- Step 2 has one button: **Create Store**. The small back arrow at the top returns to step 1 with the fields kept; so does
  Android's back. The back arrow in the dark bar leaves the page.
- Each new store is listed on the **Home** tab, under **Active Stores** on a phone and **Your Stores** on a tablet. Each card shows the name and, for the owner, a red
  delete icon. **Create New Store** is the first card, the same size as a store card.

### 2) Feature Purpose

- A store is one business with no branches. This page makes the store.
- The fields give the store its name, country and currency.
- The database then adds the first records of the store. These records include a default fiscal year, three roles (Cashier, Stock Clerk, Store Manager), settings, a chart of accounts, accounts, modes of payment, a tax, warehouses, units, a price list, item groups, naming series and a receipt format.
- The level then adds what it sets up (see 20) Store Levels): at Levels 1 to 4 a register, **Main Register**.
- A new store does not start with empty pages.
- There is no abbreviation and no cost center. Account and warehouse names carry no suffix, for example "Cash".

### 3) Feature Expectations

1. Open the **Home** tab.
2. Tap **Create New Store**.
3. Type the name in **STORE NAME**.
4. Tap **COUNTRY** and select a country.
5. Check the **DEFAULT CURRENCY**. Tap **Next**.
6. Tap the level the store needs. Tap **Create Store**.

Rules:

- A tap on a card opens the store.

### 4) Feature Visibilty

- **Home tab**: the stores list. Each card opens its store. **Create New Store** is the first card. The header holds
  **Enter Access Code**, **Store Guide** (see 21) Store Guide) and the bell.
- **Store page**: it shows the same values. You can change them there (see 2) Store).

# 2) Setup > Store & Calendar

## 1) Store

### 1) Feature Itself

- The feature is one page: **Setup > Store & Calendar > Store**.
- The page has three parts.
- Part 1 has the identity fields: **STORE NAME**, **COUNTRY** and **DEFAULT CURRENCY**.
- Part 2 is **Accounts**. Each field opens a list of ledgers. The fields are:
  - **DEFAULT CASH ACCOUNT**, **DEFAULT BANK ACCOUNT**, **DEFAULT INCOME ACCOUNT**, **DEFAULT EXPENSE ACCOUNT**;
  - **WRITE OFF ACCOUNT**, **ROUND OFF ACCOUNT**;
  - **DEFAULT DISCOUNT ACCOUNT**.
- Part 3 is **Stock**. It has the **PERPETUAL INVENTORY** switch and four fields: **DEFAULT INVENTORY ACCOUNT**, **STOCK ADJUSTMENT ACCOUNT**, **STOCK RECEIVED BUT NOT BILLED** and **EXPENSES INCLUDED IN VALUATION**.
- The page has a **Save** button.

### 2) Feature Purpose

- The store owns the books.
- Part 2 gives fallback accounts. A sale, a payment or a line uses them when it names no account of its own.
- Part 3 controls stock accounting. With **PERPETUAL INVENTORY** on, each stock movement also posts to the books.

### 3) Feature Expectations

1. Open **Setup**. Tap **Store**.
2. Change a field. For an account, tap the field, then tap an account in the list.
3. Tap **Save**.

Rules:

- A default account must be an enabled ledger of the correct type. Otherwise the page shows an error and does not save.

### 4) Feature Visibilty

- **Accounts and warehouses**: the default accounts are the fallbacks.
- **Warehouses**: a warehouse without its own account uses the **DEFAULT INVENTORY ACCOUNT**.
- **Chart of Accounts**: a store default cannot be deleted. Disable it instead.
- **Sale**: a sale posts to the accounts above (see 13) Sell).

## 2) Fiscal Years

### 1) Feature Itself

- The feature is a list page and a form: **Setup > Store & Calendar > Fiscal Years**.
- Each row shows the year name, its first day and its last day. A row can show **DEFAULT**, **SHORT YEAR** or **DISABLED**.
- **New Fiscal Year** opens the form. The form has:
  - **YEAR NAME**, **YEAR START DATE** and **YEAR END DATE** (required);
  - **SHORT YEAR** switch: a period shorter than twelve months;
  - **DEFAULT** switch: the only default year;
  - **DISABLED** switch.
- The form has **Cancel** and **Save**. A saved year also has **Delete**.

### 2) Feature Purpose

- A fiscal year is an accounting period. Every posting date must fall in an enabled year.
- The default year is where new transactions and reports start.

### 3) Feature Expectations

1. Open **Setup**. Tap **Fiscal Years**.
2. Tap **New Fiscal Year**. The form fills the next year.
3. Check the dates. Turn on **SHORT YEAR** only for a shorter year.
4. Tap **Save**.

Rules:

- A full year ends one day before the same date of the next year.
- Two years cannot share a day.
- Only one year is the default.

### 4) Feature Visibilty

- **Fiscal Years page**: the list and form.
- **Sales and stock**: a posting date must fall in an enabled year (see 13) Sell and 12) Stock).
- **Document Naming Settings**: the `.FY.` part of a series uses the year of today.

# 3) Setup > Defaults & Money

## 1) Global Defaults

### 1) Feature Itself

- The feature is one page: **Setup > Defaults & Money > Global Defaults**.
- It shows three values as text: **DEFAULT STORE**, **DEFAULT COUNTRY** and **DEFAULT CURRENCY**. They change on the Store page.
- It has two switches: **DISABLE ROUNDED TOTAL** and **DISABLE IN WORDS**.
- The page has **Save**.

### 2) Feature Purpose

- The switches control two lines at the bottom of a receipt: the **Rounded Total** line and the amount in words.

### 3) Feature Expectations

1. Open **Setup**. Tap **Global Defaults**.
2. Turn a switch on or off.
3. Tap **Save**.

Rules:

- Both switches start off.

### 4) Feature Visibilty

- **Receipts**: the sale receipt and the print format sample.
- **Currency page**: its sample total.

## 2) System Settings

### 1) Feature Itself

- The feature is one page: **Setup > Defaults & Money > System Settings**.
- It has five required fields:
  - **TIME ZONE** (for example Asia/Manila);
  - **NUMBER FORMAT** (for example 1,234,567.89);
  - **FLOAT PRECISION** (decimals in quantities);
  - **CURRENCY PRECISION** (decimals in amounts);
  - **ROUNDING METHOD**: **Banker's Rounding** or **Commercial Rounding**.
- The page has **Save**.

### 2) Feature Purpose

- The page sets how the store counts "today", shows numbers and rounds values.

### 3) Feature Expectations

1. Open **Setup**. Tap **System Settings**.
2. Tap a field. Tap a value in the list.
3. Tap **Save**.

Rules:

- Set the time zone before the first sale.

### 4) Feature Visibilty

- **Currency page and receipts**: the precision and rounding method.
- **Naming series**: the time zone sets the date parts of a series.

## 3) Currency

### 1) Feature Itself

- The feature is one page: **Setup > Defaults & Money > Currency**. It shows the record of the default currency (PHP).
- Fields: **SYMBOL** (₱), a switch for the symbol side, **FRACTION** (Centavo), **FRACTION UNITS** (100), **SMALLEST CURRENCY FRACTION VALUE** (may be empty) and **NUMBER FORMAT**.
- **SAMPLE RECEIPT TOTAL** shows a sample with **Grand Total**, **Rounded Total** and the amount in words. It changes as you type.

### 2) Feature Purpose

- The page sets how an amount looks and how it is written in words.
- The smallest coin sets cash rounding.

### 3) Feature Expectations

1. Open **Setup**. Tap **Currency**.
2. Change a field. Read the sample.
3. Tap **Save**.

Rules:

- With no smallest coin, the rounded total is a whole amount.

### 4) Feature Visibilty

- **Price List form and sample receipt**: they use this currency.
- **Sale receipt**: the amount in words.

# 4) Setup > Accounting

## 1) Chart of Accounts

### 1) Feature Itself

- The feature is a tree of folders and forms: **Setup > Accounting > Chart of Accounts**.
- The first page shows five root groups: **Application of Funds (Assets)**, **Equity**, **Expenses**, **Income** and **Source of Funds (Liabilities)**. Each row shows the number of accounts in it.
- A group page has the root type above the title, a path, **Edit Group** and **New Account**.
- The account form has **Account Name**, **Account Number**, **Account Type**, **Parent Account**, **Is Group** and **Disabled** (saved accounts only).
- On a tablet each level is a table: **ACCOUNT** and **DETAILS** columns, a folder icon before each group, the path of folders above the table.

### 2) Feature Purpose

- The chart lists every place where the books record money.
- Sales, payments and stock post to ledgers of this chart.

### 3) Feature Expectations

1. Open **Setup**. Tap **Chart of Accounts**.
2. Open the group that must hold the new account.
3. Tap **New Account**. Type the name and choose the type.
4. Turn on **Is Group** only for a folder.
5. Tap **Save**.

Rules:

- A parent must be a group.
- An account used by a default, a mode of payment or a tax cannot be deleted. Disable it instead.

### 4) Feature Visibilty

- **Store, modes of payment, tax templates, warehouses, brands, item groups**: each picks an account from this chart.
- **Posting**: every sale and return posts to these ledgers (see 13) Sell).

## 2) Accounts Settings

### 1) Feature Itself

- The feature is one page: **Setup > Accounting > Accounts Settings**.
- Five switches: **IMMUTABLE LEDGER** (on), **UNLINK PAYMENT ON CANCELLATION** (on), **DELETE LEDGER ENTRIES WITH THE DOCUMENT** (off), **DISCOUNT ACCOUNTING** (off), **TAXES FROM ITEM TAX TEMPLATES** (on).
- Two more fields: **ACCOUNTS FROZEN TILL** (a date) and **ROLE ALLOWED PAST THE FROZEN DATE** (a role, or None).

### 2) Feature Purpose

- The page sets what happens when a document is cancelled or deleted.
- **DISCOUNT ACCOUNTING** sets whether discounts post to their own accounts.
- The frozen date closes a period. Only the chosen role may post in it.

### 3) Feature Expectations

1. Open **Setup**. Tap **Accounts Settings**.
2. Change a switch, or pick a frozen date.
3. Tap **Save**.

Rules:

- When the chosen role is deleted, this field becomes None.

### 4) Feature Visibilty

- **Cancel a sale**: **IMMUTABLE LEDGER** writes reversing entries.
- **Discounts on a sale**: **DISCOUNT ACCOUNTING** posts the discount to its own account (see 13) Sell).
- **Postings**: the frozen date blocks a posting on or before it.

# 5) Setup > Payments

## 1) Modes of Payment

### 1) Feature Itself

- The feature is a list and a form: **Setup > Payments > Modes of Payment**.
- Each row shows the mode, its default account and its type. A new store has **Cash** (account **Cash**) and **Credit Card** (type Bank, no account).
- The form has **Name**, **Type** (Cash, Bank, General or Phone), **Default Account** and **Enabled**.

### 2) Feature Purpose

- A mode is one way a customer pays. The type says how the money arrives. The default account says where it is recorded.

### 3) Feature Expectations

1. Open **Setup**. Tap **Modes of Payment**.
2. Tap **New Mode of Payment**. Type the name.
3. Choose the type and the default account.
4. Tap **Save**.

Rules:

- A Cash mode accepts only a Cash ledger. A Bank mode accepts only a Bank ledger.

### 4) Feature Visibilty

- **POS Profile**: the payment methods a register offers (see 9) Point of Sale).
- **Sale page**: the payment lines show the mode name.

# 6) Setup > Taxes

## 1) Sales Taxes and Charges Templates

### 1) Feature Itself

- The feature is a list and a template page: **Setup > Taxes > Sales Taxes and Charges Templates**.
- The list shows **Default: …** or **No default template**. A new store has **Philippines Tax** (row **VAT @ 12**), and it is not the default.
- The list has two buttons: **Test Template** (outlined), left of **New Template**.
- The template page has **Title**, **Tax Category**, **Default** and **Disabled**.
- The **Taxes and Charges** rows each have **Type** (On Net Total, Actual, On Previous Row Amount, On Previous Row Total, On Item Quantity), **Account Head**, **Tax Rate**, **Reference Row #** (for the previous-row types), **Description** and **Is this Tax included in Basic Rate?**.
- **Test Template** is its own check: a page on a phone, a box over the list on a tablet. It has **Template** (the default first, enabled templates only), **Price**, **Quantity** and **Item Tax Template**, then what **The sale gets**: **Net Rate**, **Net Total**, each tax row, **Total Taxes and Charges**, **Grand Total** and **Rounded Total**. It saves nothing.
- The template page has no preview. Save the template, then test it.

### 2) Feature Purpose

- A template gives a sale its tax rows. Each row names the ledger that receives the tax.
- The included switch is for a price that already holds the tax.

### 3) Feature Expectations

1. Open **Setup**. Tap **Sales Taxes and Charges Templates**.
2. Tap **New Template**. Type the title.
3. Tap **Add Row**. Choose the type and the account. Type the rate.
4. Turn on **Default** if all new sales must start with it.
5. Tap **Save**.
6. Tap **Test Template**. Choose the template, type a price and a quantity, and check the totals.

Rules:

- Only one template is the default.
- A template used by a tax rule cannot be deleted.
- **Test Template** shows only saved templates. A template whose rows do not add up says so instead of totals.

### 4) Feature Visibilty

- **Sale**: the template a sale takes (see 13) Sell).
- **Tax Rules**: each rule names a template.

## 2) Item Tax Templates

### 1) Feature Itself

- The feature is a list and a form: **Setup > Taxes > Item Tax Templates**.
- A new store has **Philippines Tax** with the row **VAT 12%**, status **ENABLED**.
- The form has **Title**, **Disabled** and a list of rows: **Tax**, **Tax Rate** and **Not Applicable**.

### 2) Feature Purpose

- An item tax template gives some items a different rate for a tax account (for example zero-rated items).

### 3) Feature Expectations

1. Open **Setup**. Tap **New Item Tax Template**.
2. Type the title. In the row, choose the tax account and type the rate, or turn on **Not Applicable**.
3. Tap **Save**.

Rules:

- A tax account can be in one row only.

### 4) Feature Visibilty

- **Item**: the **Item Tax** section names one template.
- **Item group**: its **Item Tax** rows name templates.

## 3) Tax Categories

### 1) Feature Itself

- A list and a form: **Setup > Taxes > Tax Categories**.
- A new store has no categories. The page shows "No tax categories yet."
- The form has **Title** and **Disabled**.

### 2) Feature Purpose

- A tax category names a tax treatment, for example Exempt or Zero Rated. A tax rule uses it to choose a template.

### 3) Feature Expectations

1. Open **Setup**. Tap **New Tax Category**.
2. Type the title. Tap **Save**.

Rules:

- A category used by a template cannot be deleted.

### 4) Feature Visibilty

- **Sales Taxes and Charges Template**, **Tax Rules** and **POS Profile**: each names a category.

## 4) Tax Rules

### 1) Feature Itself

- A list and a form: **Setup > Taxes > Tax Rules**.
- A new store has no rules. The page shows "No tax rules yet."
- The form has **Sales Taxes and Charges Template**, **Tax Category**, **Item Group**, **From Date**, **To Date** and **Priority** (1 is the highest).
- **Which Template?** is a check. It takes a tax category, an item group and a sale date, and shows **The sale takes** with the template and the rule that chose it.

### 2) Feature Purpose

- A rule picks the template for a sale by its category, item group and date.

### 3) Feature Expectations

1. Open **Setup**. Tap **New Tax Rule**.
2. Choose the template. Choose the conditions and the dates.
3. Type the priority. Tap **Save**.

Rules:

- An empty condition matches every sale.
- The rule with the most conditions wins. Then priority, then the older rule.

### 4) Feature Visibilty

- **Sale**: the rule chooses the template when the POS Profile names none (see 13) Sell).

# 7) Setup > Stock

## 1) Warehouses

### 1) Feature Itself

- A tree of folders and forms: **Setup > Stock > Warehouses**.
- The root is **All Warehouses**. A new store has **Stores** under it.
- Each row shows the stock account and where it comes from.
- On a tablet each level is a table, as in the Chart of Accounts.
- The form has **Warehouse Name**, **Parent Warehouse**, **Account**, **Is Group** and **Disabled**.

### 2) Feature Purpose

- A warehouse is a place where stock is kept. A sale takes stock from a warehouse.
- Its account receives the value of the stock when Perpetual Inventory is on.

### 3) Feature Expectations

1. Open **Setup**. Open the group. Tap **New Warehouse**.
2. Type the name. Keep **Account** at None to use the parent's account.
3. Tap **Save**.

Rules:

- A warehouse used by a brand, an item group or Stock Settings cannot be deleted.

### 4) Feature Visibilty

- **Item, POS Profile and stock documents**: they choose a warehouse.

## 2) UOMs

### 1) Feature Itself

- A list and a form: **Setup > Stock > UOMs**.
- A new store has 13 units: Box, Centimeter, Gram, Hour, Kg, Litre, Meter, Millilitre, Nos, Pack, Pair, Set and Unit.
- Each row says **Whole numbers only** or **Fractions allowed**.
- The form has **UOM Name**, **Must Be Whole Number** and **Enabled**.

### 2) Feature Purpose

- A unit tells how an item is counted or sold.

### 3) Feature Expectations

1. Open **Setup**. Tap **New UOM**.
2. Type the name. Turn on **Must Be Whole Number** if fractions are not allowed.
3. Tap **Save**.

### 4) Feature Visibilty

- **Item**: its stock unit and sales units.
- **UOM Conversion Factors**: they relate two units.

## 3) UOM Conversion Factors

### 1) Feature Itself

- A list and a form: **Setup > Stock > UOM Conversion Factors**.
- Each row reads as a sentence. A new store has **1 Kg = 1000 Gram**, **1 Litre = 1000 Millilitre** and **1 Meter = 100 Centimeter**.
- The form has **From UOM**, **To UOM** and **Value**.

### 2) Feature Purpose

- A conversion lets an item be bought or kept in one unit and sold in another.

### 3) Feature Expectations

1. Open **Setup**. Tap **New Conversion**.
2. Choose the two units and the value. Tap **Save**.

Rules:

- The two units must differ. The value must be above zero.

### 4) Feature Visibilty

- **Item sales**: a sale in another unit converts the quantity.

## 4) Price Lists

### 1) Feature Itself

- A list and a form: **Setup > Stock > Price Lists**.
- A new store has one list: **Standard Selling**, currency PHP, enabled.
- The form has **Price List Name**, **Currency**, **Enabled** and **Price Not UOM Dependent**.

### 2) Feature Purpose

- A price list is a named set of selling prices. A sale takes its prices from one list.

### 3) Feature Expectations

1. Open **Setup**. Tap **New Price List**.
2. Type the name. Tap **Save**.

### 4) Feature Visibilty

- **Item Prices**, **Selling Settings**, **Brands** and **Item Groups**: each uses a price list.

## 5) Brands

### 1) Feature Itself

- A list and a form: **Setup > Stock > Brands**. A new store has no brands. The page shows "No brands yet."
- The form has **Brand Name**, **Description** and three defaults: **Default Warehouse**, **Default Price List** and **Default Income Account**.

### 2) Feature Purpose

- A brand is an optional trade name. Its defaults fill the item's defaults.

### 3) Feature Expectations

1. Open **Setup**. Tap **New Brand**. Type the name.
2. Choose the defaults you want. Tap **Save**.

### 4) Feature Visibilty

- **Item**: its **Brand** field.

## 6) Item Groups

### 1) Feature Itself

- A tree of folders and forms: **Setup > Stock > Item Groups**.
- The root is **All Item Groups**. A new store has **Products** and **Services**.
- A group page has **Item Group Name**, **Parent Item Group**, **Is Group**, four defaults (**Default Price List**, **Default Warehouse**, **Default Income Account**, **Default Expense Account**) and an **Item Tax** list.
- On a tablet each level is a table, as in the Chart of Accounts.

### 2) Feature Purpose

- An item group classifies items. Its defaults and item tax rows apply to its items.

### 3) Feature Expectations

1. Open **Setup**. Open the group. Tap **New Item Group**.
2. Type the name. Choose the defaults. Tap **Add Item Tax** if needed.
3. Tap **Save**.

Rules:

- A group used by a tax rule or Stock Settings cannot be deleted.

### 4) Feature Visibilty

- **Item**: the **ITEM GROUP** field. **Stock Settings**: the default group.

## 7) Stock Settings

### 1) Feature Itself

- The feature is one page: **Setup > Stock > Stock Settings**.
- Five fields: **ITEM NAMING BY** (Item Code), **DEFAULT ITEM GROUP** (Products), **DEFAULT STOCK UOM** (Nos), **DEFAULT WAREHOUSE** (Stores) and **DEFAULT VALUATION METHOD** (FIFO).
- Two switches: **ALLOW NEGATIVE STOCK** (off) and **AUTO INSERT PRICE LIST RATE IF MISSING** (off).
- A block shows the FIFO and Moving Average example, with the chosen method marked.

### 2) Feature Purpose

- The page sets the defaults of a new item and the valuation method.

### 3) Feature Expectations

1. Open **Setup**. Tap **Stock Settings**.
2. Choose the defaults. Read the example. Change the switches if needed.
3. Tap **Save**.

Rules:

- The valuation method changes only from FIFO to Moving Average once stock exists.

### 4) Feature Visibilty

- **Item**: a new item starts with these defaults.
- **Stock valuation**: the method sets the cost of each sale (see 13) Sell).

# 8) Setup > Selling

## 1) Selling Settings

### 1) Feature Itself

- The feature is one page: **Setup > Selling > Selling Settings**.
- One field: **DEFAULT PRICE LIST** (Standard Selling).
- Three switches: **USE PRICES FROM THE DEFAULT PRICE LIST AS FALLBACK** (off), **ALLOW EDITING THE PRICE LIST RATE** (off) and **VALIDATE SELLING PRICE** (off).

### 2) Feature Purpose

- The page sets where a sale gets its prices and how far a cashier may change them.

### 3) Feature Expectations

1. Open **Setup**. Tap **Selling Settings**.
2. Choose the price list. Change the switches.
3. Tap **Save**.

### 4) Feature Visibilty

- **Sale**: the Register uses this list (see 13) Sell).

## 2) Pricing Rules

### 1) Feature Itself

- A list and a form: **Setup > Selling > Pricing Rules**.
- A new store has no rules. The page shows "No pricing rules yet."
- The form has **TITLE**, **APPLY ON** (Item Code, Item Group or Brand), **PRIORITY** (1 is the highest), a list of **Items** to apply on, and the conditions **MIN QTY**, **MAX QTY**, **MIN AMT** and **MAX AMT**.

### 2) Feature Purpose

- A pricing rule gives an automatic discount to an item, an item group or a brand.

### 3) Feature Expectations

1. Open **Setup**. Tap **Pricing Rules**. Tap **New Pricing Rule**.
2. Type the title. Choose **APPLY ON** and add the items.
3. Type the priority and the conditions. Tap **Save**.

Rules:

- An item's own rule wins over its group's rule, then over its brand's rule.

### 4) Feature Visibilty

- **Register**: the rule applies to a cart line (see 13) Sell).

# 9) Setup > Point of Sale

## 1) POS Profiles

### 1) Feature Itself

- A list and a full page: **Setup > Point of Sale > POS Profiles**.
- The list shows the count. A new store has none: "No POS Profiles yet."
- The page has **POS PROFILE NAME**, **WAREHOUSE** (required), **PRICE LIST**, **TAXES AND CHARGES**, **TAX CATEGORY**, **PRINT FORMAT** and **LETTER HEAD**.
- **Applicable for Users**: add users. With one listed, only that user may use the register.
- **Payment Methods**: each row has **MODE OF PAYMENT**, **DEFAULT** and **ALLOW IN RETURNS**. At least one row is required.
- **Item Groups**: the groups the register lists. None listed means every item.
- **Accounting**: **ACCOUNT FOR CHANGE AMOUNT**, **WRITE OFF ACCOUNT**, **WRITE OFF LIMIT**, **INCOME ACCOUNT**, **EXPENSE ACCOUNT** and **DISCOUNT ACCOUNT**.

### 2) Feature Purpose

- A POS profile is one register: its warehouse, its payment methods, its users and its accounts.

### 3) Feature Expectations

1. Open **Setup**. Tap **POS Profiles**. Tap **New POS Profile**.
2. Type the name. Choose the warehouse.
3. Tap **Add Payment Method**. Choose the mode. Turn on **DEFAULT** and **ALLOW IN RETURNS** as needed.
4. Tap **Save**.

Rules:

- A payment method with no account cannot be saved.
- The profile must have exactly one default payment method.

### 4) Feature Visibilty

- **Sell**: the session opens on a profile (see 13) Sell).

# 10) Employees (side-menu destination, owner only)

## 1) Employees

### 1) Feature Itself

- A side-menu destination: **Employees**, after **Accounts**. Only the owner sees it.
- The first row is the owner, on a grey ground. It reads **YOU · OWNER · EVERY PERMISSION**.
- Each other row is a person let in with an access code (see 17) Access Codes): their name, their email and a tag with their role, or **No role**.
- Above the list: a search box (**Search by name or email**) and chips: **All**, one per role, and **No role**.
- A **Roles** button under the title. On a tablet, the list is a table (Employee, Contact, Role, Edit) and a **Permissions** button sits beside **Roles**.

### 2) Feature Purpose

- The owner sees who works in the store and what role each person holds.

### 3) Feature Expectations

1. Let the person in with an access code (see 17) Access Codes). They appear here with **No role**.
2. Tap their row to give them a role and permissions (see 2) An employee's Permissions).

Rules:

- A person let in has no role until the owner gives one. With no role they see **Home** only, and Home tells them why.
- To remove a person, use **Access Codes > Members > Revoke**. There is no Disable: a person kept but idle is one with no role.

### 4) Feature Visibilty

- **Access Codes > Members**: the same people, across every store the owner has.
- **POS Profiles**: the **Users** rows pick from these people.

## 2) An employee's Permissions

### 1) Feature Itself

- A page: tap a person on **Employees**. On a tablet, it opens beside the list.
- **ROLE**: a searchable list — **No role**, then each role with its number of permissions.
- A grey note under it: everything comes from the role, or how many permissions differ from the role.
- **Use the role's permissions** (red text) while some differ.
- Every permission as a switch, grouped: **SALES & POS**, **PAYMENT & CASH**, **INVENTORY**, **ACCOUNTING**, **SETUP**, with a search box. A switch that differs from the role shows a small tag: **ROLE: ON** or **ROLE: OFF**.
- **Save Changes** at the bottom, greyed out while nothing changed.

### 2) Feature Purpose

- The owner picks the person's role, and may turn a permission on or off for this person alone. The person's own setting wins over the role.

### 3) Feature Expectations

1. Open **Employees**. Tap the person.
2. Pick a role. Turn switches on or off if needed.
3. Tap **Save Changes**.

Rules:

- A permission that needs another brings it along: **Process Sales** and **Process Refunds** need **Open/Close Register**; **Apply Discounts** needs **Process Sales**. Turning one off turns off what needs it.
- Another role keeps the person's own exceptions.
- The person is told with one **Access changed** notification, and their open app follows within a minute.

### 4) Feature Visibilty

- **The person's side menu**: a destination shows when a permission reaches it (see 16) Side menu).
- **Sell, Register, Orders, Dashboard, Stock, Accounts, Setup**: each button and row follows the permissions.

## 3) Roles

### 1) Feature Itself

- A page: **Employees > Roles**. Each role has a coloured dot, its name, and "n employees · n permissions". A **New Role** button.
- Every store starts with three roles: **Cashier** (green: Process Sales, Open/Close Register), **Stock Clerk** (orange: View Stock Levels, Receive Shipments) and **Store Manager** (dark red: every permission).
- A role's page has three tabs: **General** (Role Name, Description, Colour — 13 colours), **Permissions** (the switches) and **Members** (a box per person: tick to give them this role; "Currently: …" under each).
- A red **Delete** at the top of a saved role. On a tablet, the roles are listed on the left and the role's page is on the right, with **Delete Role**, **Discard Changes** and **Save Changes** at the bottom.

### 2) Feature Purpose

- A role is a named set of permissions. You give a role to people, then make exceptions per person when needed.

### 3) Feature Expectations

1. Open **Employees**. Tap **Roles**. Tap **New Role**.
2. Type the name, pick a colour, turn on its permissions, tick its members.
3. Tap **Save Changes**.

Rules:

- A role needs a name, unique in the store, up to 60 letters.
- Each person holds one role. Ticking someone moves them from their old role.
- Deleting a role leaves its people with no role. They stay in the store and see Home only.
- If the role was **ROLE ALLOWED PAST THE FROZEN DATE** in **Accounts Settings**, that field becomes None.

### 4) Feature Visibilty

- **Employees**: each person's role tag and the role chips.
- **Accounts Settings**: the **ROLE ALLOWED PAST THE FROZEN DATE** list.

## 4) The permissions

### 1) Feature Itself

- Twenty permissions, the same in every store:
  - **SALES & POS**: Process Sales, Apply Discounts, Process Refunds, Void Transactions, View Sales.
  - **PAYMENT & CASH**: Open/Close Register, View Shift Totals, Close Any Register.
  - **INVENTORY**: View Stock Levels, Manage Items, Receive Shipments, Adjust Inventory.
  - **ACCOUNTING**: View General Ledger.
  - **SETUP**: Store & Calendar, Accounting & Payments, Taxes, Stock Setup, Selling & Pricing, POS Profiles, Naming & Printing.

### 2) Feature Purpose

- Each permission opens one part of the app: the rows, pages and buttons it needs.

### 3) Feature Expectations

- **Process Sales**: open the Register and complete a sale. **Apply Discounts**: change a price or give a discount, where the POS Profile allows it. **Process Refunds**: the **Return** button on a sale. **Void Transactions**: **Cancel** on a sale. **View Sales**: **Orders**, and sales on the Dashboard.
- **Open/Close Register**: open and close one's own session. **View Shift Totals**: the sessions and closings lists, and open registers on the Dashboard. **Close Any Register**: close a session someone else left open.
- **View Stock Levels**: Items, Stock Balance, Stock Ledger, low stock on the Dashboard. **Manage Items**: Items, Item Prices, Import Items (no opening stock), **Scan Product** on an item. **Receive Shipments**: Stock Entries, submit but not cancel. **Adjust Inventory**: Stock Reconciliations, and cancel a stock entry.
- **View General Ledger**: Accounts > General Ledger.
- Each **SETUP** permission opens its own part of Setup.

Rules:

- The owner has every permission. Employees, roles and access codes are the owner's alone; no permission reaches them.
- The database checks every permission, not only the app.

### 4) Feature Visibilty

- **Employees**: the switches on a role's page and on a person's page.

# 11) Setup > Naming & Printing

## 1) Document Naming Settings

### 1) Feature Itself

- A list: **Setup > Naming & Printing > Document Naming Settings**.
- Each row shows a document, its series and the next name. The documents are **Item**, **POS Closing Entry**, **POS Invoice**, **POS Opening Entry**, **Sales Invoice**, **Stock Entry** and **Stock Reconciliation**.
- **Update Series** sets a counter for a series.

### 2) Feature Purpose

- A naming series gives each document a unique number, with the year in it.

### 3) Feature Expectations

1. Open **Setup**. Tap **Document Naming Settings**.
2. Tap a row to change its series, one per line. Tap **Save**.
3. To change a counter, tap **Update Series**, choose the series and type the value.

### 4) Feature Visibilty

- **Each document**: its number comes from its series.

## 2) Print Formats

### 1) Feature Itself

- A list and a page: **Setup > Naming & Printing > Print Formats**. The default is **POS Receipt** (80mm).
- The page has **NAME**, **PAPER** (58mm, 80mm or A4), **PRINT HEADING**, **SHOW ITEM CODE**, **FOOTER NOTE**, **DEFAULT** and **DISABLED**.
- **Sample receipt** shows a made-up sale in the format.

### 2) Feature Purpose

- A print format sets the layout of a receipt.

### 3) Feature Expectations

1. Open **Setup**. Tap **POS Receipt**.
2. Change the paper, the heading or the footer. Read the sample.
3. Tap **Save**.

### 4) Feature Visibilty

- **Receipt**: the sale receipt uses the format of its profile or the default.

## 3) Letter Heads

### 1) Feature Itself

- A list and a form: **Setup > Naming & Printing > Letter Heads**. A new store has **Sample Cafe**, as the default.
- The form has **Name**, **Header** (several lines), **Footer**, **Default Letter Head** and **Disabled**.

### 2) Feature Purpose

- A letter head is the block at the top and bottom of a receipt.

### 3) Feature Expectations

1. Open **Setup**. Tap **New Letter Head**. Type the header and footer.
2. Turn on **Default Letter Head** if receipts must use it. Tap **Save**.

### 4) Feature Visibilty

- **Print Settings and receipts**: the default letter head prints when Print with Letterhead is on.

## 4) Print Settings

### 1) Feature Itself

- One page: **Setup > Naming & Printing > Print Settings**.
- Three switches: **PRINT WITH LETTERHEAD** (on), **COMPACT ITEM PRINT** (on) and **PRINT TAXES WITH ZERO AMOUNT** (off).

### 2) Feature Purpose

- The page sets what every printed receipt contains.

### 3) Feature Expectations

1. Open **Setup**. Tap **Print Settings**. Change a switch. Tap **Save**.

### 4) Feature Visibilty

- **Receipts**: the switches apply to each receipt.

# 12) Stock (side-menu destination)

## 1) Items

### 1) Feature Itself

- A list and a full page: **Stock > Items & Pricing > Items**.
- The list has a search box for code, name or barcode.
- The item page has **ITEM CODE**, **BARCODE**, **ITEM NAME**, **ITEM GROUP**, **DEFAULT UNIT OF MEASURE**, **BRAND**, **DESCRIPTION**, **MAINTAIN STOCK**, **STANDARD SELLING RATE** and **OPENING STOCK** (new items). It also has the sections **Inventory**, **Stock Levels**, **Units of Measure**, **Defaults**, **Discounts** and **Item Tax**.
- Which of them show depends on the store's level (see 20) Store Levels). At Level 1 a new item shows only **Scan Product**,
  **BARCODE**, **ITEM NAME (REQUIRED)**, **SELLING PRICE**, **STOCK ON HAND** and **COST PER UNIT**. Level 2 adds **ITEM
  GROUP**, the unit, **DESCRIPTION**, **MAINTAIN STOCK**, **DISABLED** and **RE-ORDER LEVEL**. Level 3 adds **ITEM CODE**,
  **BRAND**, **Units of Measure** and the rest of **Inventory**. Level 4 and 5 show everything. Levels 1 and 2 call the price,
  the stock and the cost **SELLING PRICE**, **STOCK ON HAND** and **COST PER UNIT**; Level 3 up uses **STANDARD SELLING RATE**,
  **OPENING STOCK** and **VALUATION RATE**.
- A **Scan Product** button is at the top of the page. It fills the fields from the product (see 18) Product Scan).

### 2) Feature Purpose

- An item is a product or service the shop sells.
- The barcode is the code printed on the product. The Register's scan finds the item by it.

### 3) Feature Expectations

1. Open **Stock**. Tap **Items**. Tap **New Item**.
2. Tap **Scan Product** to fill the fields from the product, if you want.
3. Type the code and the name. Choose the group and the unit.
4. Type the **STANDARD SELLING RATE** and an **OPENING STOCK** with its **VALUATION RATE**.
5. Tap **Save**.

Rules:

- The code cannot change after save. The barcode can.
- A field the level hides is still filled: the item group, the unit and the warehouse from Stock Settings, the code from the
  Item series (for example **STO-ITEM-2026-00001**). A field the app cannot fill shows at any level.
- Where the code is hidden, **ITEM NAME** is required: **Enter a name.**
- **BARCODE** is optional. It has no spaces, and up to 64 characters.
- One barcode belongs to one item in a store. A second item with it is refused: **Another item already has this barcode.**

### 4) Feature Visibilty

- **Register**: items the profile offers. Its scan reads the barcode (see 18) Product Scan). **Stock Balance**: the stock of the item.

## 2) Item Prices

### 1) Feature Itself

- A list and a form: **Stock > Items & Pricing > Item Prices**.
- Each row shows the item, the rate, the price list and the dates.
- The form has **ITEM**, **PRICE LIST**, **UOM**, **RATE**, **VALID FROM** and **VALID UPTO**.

### 2) Feature Purpose

- An item price is the rate of one item in one price list for one unit.

### 3) Feature Expectations

1. Open **Stock**. Tap **Item Prices**. Tap **New Item Price**.
2. Choose the item, the list, the unit and type the rate. Tap **Save**.

### 4) Feature Visibilty

- **Register**: the price of each line.

## 3) Import Items

### 1) Feature Itself

- A page: **Stock > Items & Pricing > Import Items**.
- It has **Download Template**, **Choose File** and a table of the columns: Item Code, Item Name, Item Group and Default Unit of Measure, Description, Brand, Disabled and Maintain Stock, Standard Selling Rate, and more.

### 2) Feature Purpose

- The page adds many items from one spreadsheet file. Nothing is imported until every row is right.

### 3) Feature Expectations

1. Open **Stock**. Tap **Import Items**.
2. Tap **Download Template**. Choose a folder.
3. Fill in the rows in a spreadsheet. Save it as CSV.
4. Tap **Choose File**. Read the mistakes, if any. Tap **Import**.

Rules:

- Up to 500 items for each file.
- The file has no Barcode column. Add a barcode on the item page.

### 4) Feature Visibilty

- **Items list**: the imported items appear after the import.

## 4) Stock Entries

### 1) Feature Itself

- A list and a document page: **Stock > Stock Transactions > Stock Entries**.
- The form has **PURPOSE** (Material Receipt is the default), **POSTING DATE**, **TARGET WAREHOUSE** and **Items** rows: **ITEM**, **QUANTITY** and **BASIC RATE**.

### 2) Feature Purpose

- A stock entry moves stock in, out or between warehouses.

### 3) Feature Expectations

1. Open **Stock**. Tap **Stock Entries**. Tap **New Stock Entry**.
2. Choose the purpose and the warehouse. Add the rows.
3. Tap **Save**. Then submit the document.

Rules:

- A submitted document cannot change.

### 4) Feature Visibilty

- **Stock Ledger** and **General Ledger**: each submitted entry posts there.

## 5) Stock Reconciliations

### 1) Feature Itself

- A list and a document page: **Stock > Stock Transactions > Stock Reconciliations**.
- The form has **PURPOSE** (Opening Stock or A count against the books), **POSTING DATE** and **Items** rows: **ITEM**, **WAREHOUSE**, **QUANTITY** and **VALUATION RATE**.

### 2) Feature Purpose

- The page sets the first stock of a store (Opening Stock) or corrects it to a count.

### 3) Feature Expectations

1. Open **Stock**. Tap **Stock Reconciliations**. Tap **New Stock Reconciliation**.
2. Choose the purpose. Add the rows. Tap **Save**, then submit.

### 4) Feature Visibilty

- **Stock Balance** and **Stock Ledger**: they show the result.

## 6) Stock Ledger

### 1) Feature Itself

- A report: **Stock > Reports > Stock Ledger**.
- Each row is one movement: the date, the warehouse, the document, the quantity, the rate, the balance, the valuation and the value.
- **Filters** narrows the report.

### 2) Feature Purpose

- The report lists every stock movement behind the balance.

### 3) Feature Expectations

1. Open **Stock**. Tap **Stock Ledger**. Tap a row to open its document.

### 4) Feature Visibilty

- **Documents**: each sale, return and stock document.

## 7) Stock Balance

### 1) Feature Itself

- A report: **Stock > Reports > Stock Balance**.
- Each row shows an item in a warehouse, its quantity, its valuation and its value. The total shows at the top.

### 2) Feature Purpose

- The report shows what is on hand and what it is worth.

### 3) Feature Expectations

1. Open **Stock**. Tap **Stock Balance**. Tap a row to see its movements.

### 4) Feature Visibilty

- **Item page**: **Stock Levels** shows the same figures.

# 13) Sell

## 1) Sell index and session

### 1) Feature Itself

- The Sell index shows the session box. It says "No session is open" or the open session with its register and date.
- Buttons: **Open Session** (when no session is open) or **Register** and **Close Session** (when one is open).
- Below: **Orders**, **POS Opening Entries** and **POS Closing Entries**.

### 2) Feature Purpose

- A session is one cashier's shift on one POS profile. Sales are rung up inside it.

### 3) Feature Expectations

1. Open **Sell**. Tap **Open Session**.
2. Choose the **POS PROFILE** and type the opening amount for each payment method.
3. Tap **Open Session**.

Rules:

- A sale can be rung only in an open session.
- A store made at Levels 1 to 4 has a register from the start: **Main Register**. With one register, **Open Session** has it
  picked already. It prints a receipt after each sale and allows a discount in the Cart (see 20) Store Levels).

### 4) Feature Visibilty

- **Sell** is a side-menu destination.

## 2) Open Session and Close Session

### 1) Feature Itself

- **Open Session**: the profile (for example Front Counter) and an **Opening amount** per payment method (for example CASH).
- **Close Session**: for each payment method, a **Counted** field. The closing entry then shows the opening, expected and closing amounts, the difference and the totals.

### 2) Feature Purpose

- The session records the cash in the drawer at the start and the end.

### 3) Feature Expectations

1. Open **Sell**. Tap **Open Session**. Type 500 in the cash field. Tap the bottom **Open Session** button.
2. Later, tap **Close Session**. Type the counted cash. Tap the bottom **Close Session** button.

Rules:

- Expected cash equals the opening amount plus the session's payments, less change given.

### 4) Feature Visibilty

- **POS Opening Entries** and **POS Closing Entries** lists.

## 3) Register

### 1) Feature Itself

- The item list of the session's profile. A search field searches by name or code.
- A scan button (a barcode icon) is beside the search field. It opens **Scan to Sell** (see 18) Product Scan).
- Each row shows the name, the code, the price and the stock on hand. A tap adds one unit.
- On a phone, a bar at the bottom shows **Cart · n items · total** and opens the Cart page.
- On a tablet (sideways or upright), there is no bar: the page splits in two under the **Register** title. The items are on the left, the Cart on the right (two parts to three, a thin line between), headed **Cart** with its line count (**Nothing yet** when empty). A tap shows in the cart at once.

### 2) Feature Purpose

- The Register is where a cashier chooses the items of a sale.

### 3) Feature Expectations

1. Open **Sell**. Tap **Register**.
2. Tap the search box and type a name or code, if needed.
3. Tap an item to add one. Or tap the scan button and point the camera at the product's barcode.
4. Tap the bar to open the Cart.

### 4) Feature Visibilty

- **Sell**: the session box opens the Register.

## 4) Cart and payment

### 1) Feature Itself

- The Cart shows each line: its quantity, unit and rate.
- The totals: **Net Total**, **Grand Total** and **Rounded Total**.
- **Payment**: one amount for each payment method. Cash is filled with the total.
- **Change** shows the money to return.
- The button is **Complete Order**.
- On a phone the Cart is its own page. On a tablet it is the right side of the Register: after **Complete Order** the page stays, the cart empties and the payment amounts go back to their defaults, ready for the next sale. Where the POS Profile prints a receipt, the receipt opens over the Register; Back returns to it.
- An empty cart says **The cart is empty. Tap an item to add it.** on a tablet, and **…Go back to the Register and add an item.** on a phone.

### 2) Feature Purpose

- The Cart completes a sale. It posts stock and the books at once.

### 3) Feature Expectations

1. In the Cart, check the quantity and the amount.
2. Check the payment. Tap **Complete Order**.

Rules:

- The sale stops with a message when the stock on hand is not enough.

### 4) Feature Visibilty

- **Register**: the Cart bar.

## 5) Orders and the sale page

### 1) Feature Itself

- **Orders** lists every sale, newest first. Each row shows the number, the date, the amount and the status (SUBMITTED).
- A sale page shows the status, the buttons **Return**, **Cancel**, **Stock Ledger** and **General Ledger**, and the receipt: the shop name, the date, the lines, the totals, the amount in words and the payment method.

### 2) Feature Purpose

- The page lets a manager review a sale and reopen its receipt.

### 3) Feature Expectations

1. Open **Sell**. Tap **Orders**. Tap a sale.
2. Read the receipt on the screen.

### 4) Feature Visibilty

- **Sell** and **Stock**: the sale page is also reachable from the General Ledger.

## 6) Return

### 1) Feature Itself

- The Return page is opened from a sale with **Return**.
- It shows the sold and returnable quantity, the **QUANTITY TO RETURN** field, the **Refund** totals and **Handed Back** for each allowed payment method.
- The button is **Complete Return**.

### 2) Feature Purpose

- A return takes back goods and pays the customer back.

### 3) Feature Expectations

1. Open the sale. Tap **Return**.
2. Check the quantity. Check the refund amount.
3. Tap **Complete Return**. The return receipt opens.

Rules:

- A return needs an open session of the same cashier.
- The refund uses only the payment methods that allow returns.

### 4) Feature Visibilty

- **Orders**: a return shows **Return against** the sale.

## 7) POS Opening Entries and POS Closing Entries

### 1) Feature Itself

- **POS Opening Entries** lists each session: its profile, date and opening amount, with its status (OPEN or CLOSED).
- **POS Closing Entries** lists each closed session: the number, the date and the amount sold.

### 2) Feature Purpose

- The lists show each shift and its result.

### 3) Feature Expectations

1. Open **Sell**. Tap a list. Tap a row to read it.

### 4) Feature Visibilty

- **Sell index**: the two entries below the box.

# 14) Dashboard

## 1) Dashboard

### 1) Feature Itself

- A side-menu destination with one screen.
- Period buttons: **Today**, **Last 7 Days** and **This Month**.
- Number cards: **SALES** (with the invoice count), **GROSS PROFIT**, **OPEN REGISTERS** (with the cash expected) and **LOW STOCK**.
- **Sales per Day**: a bar chart with the dates.
- **Top-Selling Items**: by quantity or amount, by item or item group. It excludes returns.
- **Stock Alerts**: items at or below their re-order level.
- On a tablet the period buttons sit beside the **Dashboard** title, the four number cards fill one row, and the three blocks go two to a row where they fit (sideways) or one under another (upright). The period buttons read in full at any text size.

### 2) Feature Purpose

- The Dashboard gives a quick view of sales, registers and stock.

### 3) Feature Expectations

1. Open **Dashboard**. Tap a period button.
2. Read the cards. Scroll down for the chart and the lists.

Rules:

- Each figure counts only the rows the signed-in person may read.
- Sales are the net total. A return reduces them.

### 4) Feature Visibilty

- **Side menu**: the Dashboard row appears for the owner, and for people with View Sales, View Shift Totals, Close Any Register or View Stock Levels. Each block shows only with its permission.

# 15) Accounts

## 1) General Ledger

### 1) Feature Itself

- A report: **Accounts > Reports > General Ledger**.
- Each row shows an account, the date, the voucher, and the debit or credit.
- **Filters** opens a panel with **FROM DATE**, **TO DATE**, **ACCOUNT** and **VOUCHER NO.**. **Clear all** and **Done** close it.

### 2) Feature Purpose

- The report lists every debit and credit of the books.

### 3) Feature Expectations

1. Open **Accounts**. Tap **General Ledger**.
2. Tap **Filters** to narrow the list. Tap a row to open its document.

### 4) Feature Visibilty

- **Sale and return**: each posts four entries (cash, sales, stock in hand and cost of goods sold).

# 16) Side menu and Home

## 1) Side menu

### 1) Feature Itself

- A menu on the left. On a phone it opens from the **Menu** button in the header. On a tablet, sideways or upright (600 dp wide and up), it is always showing as a rail.
- It shows the store name and its initials, then **Home**, **Dashboard**, **Sell**, **Stock**, **Accounts**, **Employees**, **Setup** and **Features**.
- The owner sees every row. An employee sees **Home** and **Features**, and each other row only when one of their permissions reaches it (see 10) Employees). **Employees** is the owner's alone.
- A screen the person hid on **Features** (see 19) Features) is not in their menu. **Home** and **Features** are never hidden.
- Until a person saves their own choices, their menu is the store level's (see 20) Store Levels). At Level 1 it is **Home**,
  **Dashboard**, **Sell** (the session, the Register and **Orders**), **Stock** and **Features**.

### 2) Feature Purpose

- The side menu moves the user between the destinations of one store.

### 3) Feature Expectations

1. Tap **Menu**. Tap a destination.
2. Tap **Your stores** in the header to leave the store.

### 4) Feature Visibilty

- **All pages of a store**: the header shows the menu.

## 2) Home

### 1) Feature Itself

- The **Home** destination of a store is empty for whoever has work in it.
- An employee with no role reads **You're in. The owner hasn't given you a role yet.** and a line saying the menu fills once they get one.

### 2) Feature Purpose

- Home stays empty by design. Business work is on the other destinations.

### 3) Feature Expectations

- None.

### 4) Feature Visibilty

- **Side menu**: Home is the first row.

# 17) Access Codes and Notifications

## 1) Access Codes

### 1) Feature Itself

- A tab at the bottom: **Access Codes** (the key), between **Home** and **Account**. On a tablet, the key at the top right of **Home**.
- Three parts: **Codes**, **Requests** and **Members**.
- **Codes**: a **Create Code** button, a search box, and the chips **All**, **Active**, **Claimed**, **Used** and **Expired**. Each row shows the label (or the code), the code like `A4F-7K2`, the store, and its status, time left and uses.
- **Create Code** opens **Generate Staff Access Code**: **Label**, **Store**, **Quantity** (1 to 20), **Expires** (**5 min**, **30 min**, **1 hour**, **Custom** — a last day — or **Never**) and **Uses per Code** (**1 person** or **Many people**). The made codes come with a share button each, and **Share All**.
- A code's page shows its status, expiry, uses, the people who used it, **Share** and a red **Delete**.
- **Requests**: the chips **Pending · n**, **Approved**, **Declined** and **All**. A request's page shows the person (photo, name, email), the store, the code and the time, with **Approve** and a red **Decline**.
- **Members**: everyone let in, with the code they used, the store and the date joined, and a red **REVOKE**.
- Someone who owns no store sees **You don't own a store** and an **Enter Access Code** button.

### 2) Feature Purpose

- An access code is the one way into someone else's store. Only the owner makes codes and lets people in.
- The owner sends a code outside the app (a message, an email). The person types it in, and waits for the owner.

### 3) Feature Expectations

1. Open **Access Codes**. Tap **Create Code**.
2. Choose the store, how many codes, when they expire and how many people each may let in. Tap **Create Code**.
3. Tap a share button. Send the code.
4. When the person uses it, open **Requests**. Tap their row. Tap **Approve** or **Decline**.
5. To take someone's access away, open **Members**, tap their row and tap **Revoke**.

Rules:

- A code is six letters and numbers. It has no 0, O, 1 or I.
- **Active**: the code still works. **Claimed**: a request waits for every use left. **Used**: every use is approved. **Expired**: its time is up.
- A declined request frees its use for someone else, not for the person declined.
- A custom expiry ends at midnight after the chosen day, in the store's time zone. A day in the past is refused.
- A code cannot be changed. Delete it and make another. Deleting it keeps the people it let in.

### 4) Feature Visibilty

- **Home tab**: the person's **Waiting for approval** box, then the store under **Active Stores** once approved.
- **Notifications**: the owner is told when a code is used; the person, when they are approved, declined or removed.
- **Employees**: the people let in, each with their role.

## 2) Enter Access Code

### 1) Feature Itself

- An icon in the **Home** header (a key with dots), at both widths. It has no card of its own.
- The page is titled **Employee Access Code**: a shield, "Use a code your admin sent to you.", six boxes and **Use Code**.

### 2) Feature Purpose

- The person uses the code an owner sent them, to ask to join that store.

### 3) Feature Expectations

1. Tap the **Enter Access Code** icon in the **Home** header.
2. Type the six characters. The dash, spaces and small letters are fine.
3. Tap **Use Code**. The page says **Request sent** and names the store.

Rules:

- A wrong code says it does not exist, has expired, or was already used. It never names the store.
- Ten wrong codes in 15 minutes stop the person for 15 minutes.
- The owner cannot use their own code. A person already in, or already waiting, is told so.

### 4) Feature Visibilty

- **Home tab**: the **Waiting for approval** box until the owner decides.

## 3) Notifications

### 1) Feature Itself

- A page opened from the bell: in the **Home** header at both widths, and in a store's header. A red number on the bell
  shows how many are unread. The page has a back arrow.
- Each row has an icon, a title, a line and the time. An unread row is grey with a red dot. **Mark all as read** is above the list.
- On a tablet the list is a readable column on the left, not rows across the whole screen.

### 2) Feature Purpose

- The owner learns a code was used. The person learns they were approved, declined or removed.

### 3) Feature Expectations

1. Tap the bell.
2. Tap a row. **Access code used** opens **Access Codes > Requests**. **Request approved** opens the store.

Rules:

- Nothing pops up on the lock screen yet. The app checks every minute while it is open, and when it is opened again.
- A store that is approved appears on **Home** within a minute. A store that is revoked leaves within a minute, even while the person is inside it.

### 4) Feature Visibilty

- **Home header**: the bell and its number.
- **Header inside a store**: the bell and its number. Tapping it opens **Notifications**; back returns to the store.

# 18) Product Scan

## 1) Scan Product (Items)

### 1) Feature Itself

- A full page. Its title is **Scan Product**. Tap **Scan Product** at the top of an item's page to open it.
- The back camera fills the page. It reads a barcode as soon as one is in view: EAN-13, EAN-8, UPC-A, UPC-E or Code 128.
- A line under the camera says what to do: **Point at the barcode, then read the label.** After a barcode: **Barcode 4800016644214. Now read the label, or tap Done.**
- Three buttons: **Read Label** (takes a picture with the camera), **Choose Photo** (picks a picture on the phone) and **Done**.
- The first time, the phone asks to allow the camera. Not allowed: the page says **The camera reads the barcode on a product.** and shows **Allow Camera**. Refused for good: **The camera is off for Mobile Merchant. Turn it on in the phone's Settings, under Permissions.** and **Open Settings**. The camera starts when the person comes back.

### 2) Feature Purpose

- The scan fills the item's fields from the product, so the person types less.
- Everything runs on the phone (Google ML Kit). It works with no internet and costs nothing per scan.
- What it fills:
  - **BARCODE**: the barcode read.
  - **ITEM CODE**: the same barcode, on a new item whose code is still empty and typed by hand (not from a naming series).
  - **ITEM NAME**: the largest print on the label.
  - **BRAND**: a brand already in the store that the label names. It never makes a new brand.
  - **DESCRIPTION**: up to four other lines of the label.
  - **STANDARD SELLING RATE**: the first price marked ₱, PHP or P. Only on a new item, for a person who may set prices.
- It never fills the item group, the unit, the warehouse, the accounts or the taxes.

### 3) Feature Expectations

1. Open **Stock**. Tap **Items**. Tap **New Item**, or open an item.
2. Tap **Scan Product**. Allow the camera the first time.
3. Point the camera at the barcode. The line shows the barcode.
4. Point at the label with the name and price. Tap **Read Label**. Or tap **Choose Photo** and pick a picture of the label. The page closes and the fields are filled.
5. Or tap **Done** to keep only the barcode.
6. Check the fields. Choose the group and the unit. Tap **Save**.

Rules:

- A scan fills only empty fields. What the person typed stays. The barcode is the exception: a new scan replaces it.
- A barcode counts only when the camera reads the same code three frames in a row.
- Lines of only digits and separators (the numbers under a barcode, a date, a time) are never read as a field.
- A picture with nothing usable keeps the page open: **No print found. Hold the label closer, in good light.**
- **Choose Photo** works with the camera refused. **Read Label** does not.
- Nothing is saved until **Save**. A barcode another item has is refused then.
- Only a person who may change the item sees **Scan Product**: the owner, or **Manage Items**.
- The camera and the text reading are inside the app. An app built before 2026-10-15 does not have them.

### 4) Feature Visibilty

- **Item page**: the filled fields and **BARCODE**.
- **Items list**: the search finds an item by its barcode.
- **Register**: **Scan to Sell** finds the item by this barcode.

## 2) Scan to Sell (Register)

### 1) Feature Itself

- A full page. Its title is **Scan to Sell**. Tap the scan button beside the Register's search field to open it.
- The back camera, the line **Point at a barcode to add it to the cart.**, and one button: **Done**. It has no **Read Label**.
- After each barcode, the line answers: **Added Classic Instant Coffee · 1 in the cart**.

### 2) Feature Purpose

- The cashier rings up a product by its barcode instead of searching for it.

### 3) Feature Expectations

1. Open **Sell**. Tap **Register**.
2. Tap the scan button beside the search field.
3. Point the camera at a product's barcode. The line names the product and how many are in the cart.
4. Scan the next product. To add the same product again, take it out of view for two seconds, then show it again.
5. Tap **Done**. The Cart bar shows the items.

Rules:

- The scan looks for an item with the barcode first, then for an item code equal to it.
- It adds one, in the unit the item sells in, as a tap on its row does.
- Holding a product in view adds it once.
- A barcode no item has: **No item has the barcode 4806502164532.**
- An item this register does not offer: **Coffee isn't sold at this register.** That is an item outside the POS Profile's item groups, a disabled item, or an item out of stock when the profile hides those.
- It works with no internet. It looks among the items the Register has already loaded.
- It finds only the items of the open store.

### 4) Feature Visibilty

- **Register**: the quantity on the item's row and the Cart bar.
- **Cart**: each scanned item is a line, like a tapped one.

# 19) Features

## 1) Features

### 1) Feature Itself

- **Features**, the last row of a store's side menu (a sliders icon), there for everyone. It opens where the other screens open — beside the rail on a tablet — titled **Features** under the store's name, with no back arrow, and the line "Hide the screens and pages you don't use in this store. Only your own menu changes."
- **The list** opens with **STORE LEVEL**: a box with the store's level (**Level 1 · Just Sell** …) and its line. The owner
  has **Change Level** under it (see 20) Store Levels). Anyone whose choices differ from the level's menu also has a red
  **Use Level n's menu**: it puts the level's menu back as an unsaved change. Then **ALWAYS VISIBLE** — **Home** and **Features**, each with a padlock, no switch. **SCREENS** — a row for each screen the person may open: its icon, its name, **Shown**, **Some pages hidden** or **Hidden** (**Shown · Owner** on Employees), how many of its pages show (**3/4**), and a dot while its choices are not saved.
- **A screen**: a top box with its icon, name and status word, one line on what it is, an **i** button and its switch, and notes: "This screen is a single page, so this switch is all there is." (Dashboard, Employees); "Every page here stands on its own. Turning off every page turns Setup off; turning Setup on again shows all its pages." (Setup, Accounts); "Hiding only removes it from the menu. Nothing is deleted or disabled." (all).
- Under it: **CORE · ALWAYS ON WITH SELL / STOCK** — the core page with a padlock **Always on** tag, no switch — then one box per section of the screen's index, headed by the section's name with **Hide all** (**Show all** once a page in it is hidden; only with two pages or more). Each page row: its name, the short line its index shows, an **i** button and a switch.
- The **i** button opens **About**: "Screen" or "Page of Setup", the name, **PURPOSE** and **USE-CASE**, and **Close**. A box over the page on a tablet, a panel from the bottom on a phone.
- On a tablet the list sits on the left (two parts in five) and the open screen on the right. On a phone the list fills the page and a tap opens the screen on its own page; its back arrow returns to the list with nothing lost.
- While a choice differs from the saved one, a bar at the bottom reads **n unsaved changes** with **Reset** and **Save**. Opening another screen from the side menu keeps the unsaved choices for when the person comes back. Android's back on the list asks **Discard your changes?** first; **Discard** drops them and goes to **Home**.

### 2) Feature Purpose

- Each person tidies a store for themselves: they hide the screens and pages they don't use. Every row says what it is for and when to use it.
- Hidden is not turned off. Only the person's menu and the rows of an index change.

### 3) Feature Expectations

1. Inside a store, tap **Features** in the side menu.
2. Tap a screen in the list. Turn off the screen, a page, or a section with **Hide all**.
3. Tap **Save**. The page stays open and says "Saved. Your menu now shows only what you chose."
4. To bring it back, turn it on again and tap **Save**. **Reset** drops what is not saved; Android's back with changes asks first.

Rules:

- What can be hidden:

| Screen | Core (always on with the screen) | Pages that can be hidden |
| --- | --- | --- |
| Home | never hidden | — |
| Dashboard, Employees | one switch for the screen | — |
| Sell | **Sessions & Register** (open a session, sell, pay, close) | Orders, POS Opening Entries, POS Closing Entries |
| Stock | **Items** | Item Prices, Import Items, Stock Entries, Stock Reconciliations, Stock Balance, Stock Ledger |
| Accounts | none | General Ledger. Hiding it hides Accounts |
| Setup | none | all 26 pages. Hiding the last one hides Setup |

- A core page goes only with its screen. It counts as core only for a person who may open it: for someone who cannot open a session, Sell's pages each stand alone.
- A screen with no core: turning off its last page turns the screen off, and a message says "Every page of Accounts is off, so Accounts is now hidden too." Turning the screen on shows every page again.
- A screen that is off locks its pages: they turn grey and their switches can't move. A screen with a core keeps its pages' choices and shows them again when it is turned back on.
- A hidden page still opens from elsewhere, for example a ledger row or a link. Permissions decide everything, as before.
- The choices are saved per person, per store, on the server. They stay after a reinstall and follow the person to another phone. They go with the account or the store. Nobody else in the store is affected.
- The page asks the server again when it first opens in a store, so it never overwrites a change made on another phone. Offline, it opens from the last copy and **Save** waits for the connection.
- **Features** itself is never hidden, so anything hidden can be shown again.
- Until the person saves, their choices are the store level's menu. A change of level takes everyone's choices in the store
  back to the new level's.

### 4) Feature Visibilty

- **Side menu**: a hidden screen is gone.
- **Sell, Stock, Accounts and Setup**: a hidden page is gone from the index. A section with nothing left is gone too.

# 20) Store Levels

## 1) Store Levels

### 1) Feature Itself

- Every store has a level, from 1 to 5. The owner picks it on **Create New Store**'s second step, and changes it on
  **Features**.
- The five levels:
  - **Level 1 · Just Sell** — add items, sell at the register with discounts and a receipt for every sale, look past
    orders up, check the Dashboard.
  - **Level 2 · Sell & Restock** — Level 1, plus deliveries, prices and stock on hand.
  - **Level 3 · Staff & Stock Control** — Level 2, plus employees, stock counts, imports, shift records and the basic settings.
  - **Level 4 · Full Store** — Level 3, plus the books, taxes, pricing rules and the stock and selling settings.
  - **Level 5 · Everything, by Hand** — every screen and field. Every store made before levels is Level 5.
- **Change Level** on **Features** opens **Store Level** — a box over the page on a tablet, a page on a phone: a note on what
  changes, the five levels, **Cancel** and **Save**. Only the owner has it.

### 2) Feature Purpose

- Most shops only add items, sell and look at the Dashboard. A level shows a store only what it uses, and sets up for it
  what it would otherwise do by hand. Nothing is turned off: a hidden screen or page still opens from a link, and
  permissions decide everything as before.

### 3) Feature Expectations

1. On **Create New Store**, fill the store's details and tap **Next**.
2. Tap a level. Tap **Create Store**.
3. Later, open **Features**. Tap **Change Level**, tap another level, and tap **Save**.

Rules:

- What each level shows in the menu (until the person saves their own choices on **Features**):

| Level | The menu (Home and Features always) |
| --- | --- |
| 1 | **Dashboard**, **Sell** (the session, the Register and **Orders**), **Stock** (**Items**) |
| 2 | + **Item Prices**, **Stock Entries**, **Stock Balance** |
| 3 | + **Employees**, **POS Opening Entries**, **POS Closing Entries**, **Import Items**, **Stock Reconciliations**, **Stock Ledger**; **Setup** with **Store**, **Modes of Payment**, **UOMs**, **Price Lists**, **Brands**, **Item Groups**, **POS Profiles**, **Print Formats**, **Letter Heads**, **Print Settings** |
| 4 | + **Accounts** (**General Ledger**); **Setup** adds **Currency**, both tax templates, **Warehouses**, **Stock Settings**, **Selling Settings**, **Pricing Rules** |
| 5 | + **Setup**'s **Fiscal Years**, **Global Defaults**, **System Settings**, **Chart of Accounts**, **Accounts Settings**, **Tax Categories**, **Tax Rules**, **UOM Conversion Factors**, **Document Naming Settings** |

- What each level sets up, when the store is made or the level changes. It only adds; it never deletes.
  - Levels 1 to 4: a register, **Main Register** (warehouse **Stores**, **Cash** as the default payment and for returns), when
    the store has none. It has **PRINT RECEIPT ON ORDER COMPLETE** and **ALLOW USER TO EDIT DISCOUNT** on: after
    **Complete Order** the receipt opens by itself, and the Cart has **DISCOUNT (%)** and **DISCOUNT AMOUNT** on each line
    and an **Additional Discount** for the whole sale. Who may type a discount is still the **Apply Discounts** permission
    (the owner always); a **Cashier** sees no discount fields. A store already at Level 1 or 2 got both switches turned on
    on its **Main Register** on 2026-10-22. A store moved to Level 1 that already has its own register keeps its switches
    as they are.
  - Levels 1 and 2: item codes from the Item series (Stock Settings' **ITEM NAMING BY** is **Naming Series**).
  - Level 1: a sale past the stock on hand is not refused (Stock Settings' **ALLOW NEGATIVE STOCK** is on).
- The New Item page shows the level's fields (see 12) Stock, Items).
- A change of level takes everyone's menu in the store back to the new level's. Each person can change their own again.
- Only the owner changes the level. Offline, **Save** waits for the connection.

### 4) Feature Visibilty

- **Create New Store**: step 2.
- **Features**: the **STORE LEVEL** box.
- **Side menu**, **Sell**, **Stock**, **Accounts** and **Setup**: what shows.
- **Cart** and the sale's page: the discount fields and the receipt after **Complete Order** (Levels 1 to 4's **Main
  Register**).
- **Stock > Items > New Item**: which fields show.
- **Sell > Open Session**: **Main Register**, picked already.

# 21) Store Guide

## 1) Store Guide

### 1) Feature Itself

- A page, **Learn a role**, opened from the **Store Guide** icon (a question mark) in the **Home** header, at both
  widths. It starts with a dark box: what a role is, three labels (**Nothing is saved**, **Works offline**, **Leaving
  resets it**) and a red **Choose a Role** button. Opening the page pops up **Pick a role to practise** — a sheet from
  the bottom on a phone, a box over the page on a tablet — closed by the **X** at its top right; **Choose a Role**
  brings it back.
- In the list, **Search roles** keeps the roles whose name or line holds what is typed (**No role matches.** when none
  do). Each role is a card: its name, its kind, what it does, and a bar of how many of the 20 permissions it holds
  ("2 of 20 permissions").
- The roles, by work area:
  - **Selling & Cash**: Cashier, All-around Helper, Senior / Head Cashier, Returns / Customer Service Desk, Shift
    Supervisor, Cash Custodian / Cash Office.
  - **Stock**: Receiving / Stock Clerk, Inventory Controller / Stock Auditor, Product Encoder / Merchandiser, Pricing /
    Promo Officer.
  - **Books & Setup**: Bookkeeper / Accountant, External Auditor / Silent Partner, System / Setup Admin.
  - **Running the store**: Assistant Manager, Store Manager, Owner.
  - **Not working yet**: Seasonal / On-leave Staff (no role).
  Each shows its kind (Built-in, Custom, Owner, No role), how many of the 20 permissions it has, and what it does.
- The page also shows the 20 permissions as a card per area, and six numbered cards on what roles cannot do today —
  one card a row on a phone; on a tablet two a row, three permission cards a row when held sideways.
- Tapping a role opens a **practice store**, **Sample Cafe**: the store's header, its side menu with only that role's
  screens, pages that look like the real ones with sample items, sales and sessions, and a **Tasks** button.
- Each role has guided tasks (open a session, ring up a sale, scan to sell, give a discount, take a return, void a sale,
  check shift totals, close a register left open, log a delivery, count stock, cancel a wrong entry, add an item with
  the scanner, set a price, import items, read the General Ledger, one per Setup permission, and for the owner: give a
  role, make an access code, change the store level). A task shows what you'll do, then a box under the page walks you
  through it step by step, ringing the control to tap, and ends with what a real store would also do.

### 2) Feature Purpose

- An owner sees what each role can do before giving it; a new employee practises their work without touching a real
  store.

### 3) Feature Expectations

1. On **Home**, tap the **Store Guide** icon in the header. The role list pops up.
2. Tap a role. The practice store opens with its tasks.
3. Tap a task, then **Start**, and follow the box at the bottom. Or tap **Explore on My Own** and tap around.
4. Tap the **X** at the top right to leave.

Rules:

- Nothing in the practice store is saved, and it uses no internet. Leaving resets it.
- A step moves on only when its own control is used; a step on another page says so. **Start Again** and **Stop Task**
  are always in the box.
- The practice store refuses what the real one refuses (a sale with a return cannot be voided; a Stock Clerk cannot
  cancel a delivery).
- The phone's back button goes back one practice page at a time, then leaves.

### 4) Feature Visibilty

- **Home header**: the **Store Guide** icon, for everyone signed in.
- **Learn a role**: the role list, the permissions, the notes.
- **Practice store**: per role, its own menu and tasks.

# 22) Home, Account and Sign-in

## 1) Home (the stores list)

### 1) Feature Itself

- The first tab. Header: the logo, **Merchant**, then **Enter Access Code**, **Store Guide** and the bell. On a tablet also
  **Access Codes** and **Account** (the bottom bar is hidden there).
- The bottom bar on a phone: **Home**, **Access Codes**, **Account**.
- **Create New Store** is the first card, then one card per store. On a phone the cards are rows; on a tablet, a grid.
- The owner's card has a red delete icon. A long press on an owned card selects it; taps then select more. The header
  becomes **n selected** with **Select all** and a red delete. Back, or the X, ends the selection.

### 2) Feature Purpose

- Every store the person owns or was let into, and the ways to make, join or remove one.

### 3) Feature Expectations

1. To remove one store: tap its delete icon, type its name, tap **Delete**.
2. To remove several: long-press one, tap the others, tap the red delete, type **DELETE**, tap **Delete**.

Rules:

- Only the owner removes a store. A store someone else owns cannot be selected.
- Removing deletes everything kept in the store, and cannot be undone.

### 4) Feature Visibilty

- **Home tab**: the cards and the header icons.

## 2) Account

### 1) Feature Itself

- The **Account** tab on a phone, the account icon on a tablet: the same page at both widths.
- The photo, name and email; **Account** (Account Information, Your Businesses); **Security & Privacy** (Privacy Policy,
  Terms of Service); **Preferences** (**Dark Mode**, a switch; **Themes**, which does nothing yet); **Sign Out**;
  **Delete account**.

### 2) Feature Purpose

- The person's own settings, the app's legal documents, and signing out.

### 3) Feature Expectations

1. Tap **Dark Mode** to switch the whole app between dark and light.
2. Tap **Privacy Policy** or **Terms of Service** to read them. Back returns to Account.

### 4) Feature Visibilty

- **Account tab** (phone) or the account icon on **Home** (tablet).

## 3) Sign-in and the legal pages

### 1) Feature Itself

- The sign-in page: **Merchant**, **Welcome** and a line, **Continue with Google**, **Continue with Facebook**, and
  "By continuing, you agree to our Terms of Service and Privacy Policy." with both names as links.
- **Privacy Policy** and **Terms of Service**: each a page with the date it was last updated and its sections.
  `[Developer name]` and `[contact email]` are placeholders the publisher fills in.

### 2) Feature Purpose

- The person knows what they agree to before signing in, and can read it again from Account.

### 3) Feature Expectations

1. On the sign-in page, tap **Terms of Service** or **Privacy Policy**. Read. Tap back.
2. Tap **Continue with Google** or **Continue with Facebook**.

### 4) Feature Visibilty

- **Sign-in page** and **Account**: both open the same two pages, signed in or not.
