# Finance Money Exchange — SQLite Database

This folder contains an **SQLite** implementation of the **Finance Money Exchange** ER model (`Finance Money Exchange - ER Diagram.drawio`). The physical schema mirrors the Chen-style entities, attributes, and relationships from that diagram.

## How many tables?

**Five tables** are created:

| # | Table | Role |
|---|--------|------|
| 1 | `customer` | Identity and compliance profile for exchange users |
| 2 | `currency` | Currencies offered (ISO codes, precision, optional peg reference) |
| 3 | `account` | Resolves **M:N between customer and currency** (wallet per currency per customer) |
| 4 | `exchange_rate` | Quoted conversion between two currencies (mid rate, spread, validity window) |
| 5 | `fx_transaction` | Individual FX legs: sell account, buy account, rate applied, amount sold |

### Why each table is necessary

1. **`customer`** — The application must store who is allowed to trade: contact details, KYC state, and optional **referral** (`referred_by_customer_id` self-FK from the ER). Without this table there is no stable subject for accounts or audit.

2. **`currency`** — FX is meaningless without a master list of instruments. Storing `iso_code`, display `name`, and `decimal_places` avoids hard-coding symbols in application logic. The optional **`pegged_to_currency_id`** self-FK matches the ER (e.g. synthetic or pegged units).

3. **`account`** — The ER states **M:N customer ↔ currency via account**. A single row represents one customer’s holdings in **one** currency (`balance`, `status`, `opened_at`). FKs to `customer` and `currency` encode the relationship cardinalities without duplicating customer or currency rows. A **`UNIQUE (customer_id, currency_id)`** constraint enforces at most one wallet per pair (typical for this domain).

4. **`exchange_rate`** — Trades depend on authoritative **quotes**: which pair (`from_currency_id`, `to_currency_id`), **`mid_rate`**, **`spread_bps`**, and **`valid_from`**. Separating rates from transactions lets you keep history, re-price, and satisfy **exchange_rate → fx_transaction** (1:N on the ER) by referencing `exchange_rate_id` per transaction.

5. **`fx_transaction`** — Persisted trades: **`from_account_id`** / **`to_account_id`** implement the ER’s dual **account → transaction** links (sell vs buy leg), **`exchange_rate_id`** ties the booked quote, and **`amount_sold`** / **`status`** capture the business fact. This table is not redundant with `account`: balances are snapshots; transactions are the immutable event log (simplified here without double-entry ledger tables).

## Creation script

- **File:** `create_money_exchange_db.py`
- **Output:** `money_exchange.sqlite` in this same directory (any existing file with that name is removed first).

The script:

- Enables SQLite **`PRAGMA foreign_keys = ON`** so all `REFERENCES` clauses are enforced.
- Creates secondary **indexes** on foreign-key columns used for joins and reporting.
- Adds **CHECK** constraints aligned with the model (e.g. rate pair not identical, positive amounts, allowed enum-like status values).
- Inserts **demo rows** by default (two customers, currencies, sample accounts, one rate pair, one completed transaction). To build an **empty** database (schema only), run with environment variable `CREATE_ONLY=1`.

### Run

```bash
cd "/home/abusufian/Peronal/workspace/repos/MSE800-PSD/week 4"
python3 create_money_exchange_db.py
```

Schema only:

```bash
CREATE_ONLY=1 python3 create_money_exchange_db.py
```

### Inspect

```bash
sqlite3 money_exchange.sqlite ".schema"
sqlite3 money_exchange.sqlite "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
```

## ER traceability

- **Self-FKs:** `customer.referred_by_customer_id → customer`; `currency.pegged_to_currency_id → currency`.
- **1:N:** customer → account, currency → account, currency → exchange_rate (two FKs), exchange_rate → fx_transaction, account → fx_transaction (twice — sell/buy accounts).

Design choices documented here (e.g. `UNIQUE` on email and on `(customer_id, currency_id)`) tighten integrity beyond the conceptual ER while staying consistent with it.
