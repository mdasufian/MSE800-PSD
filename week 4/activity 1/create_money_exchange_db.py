#!/usr/bin/env python3
"""
Create the Finance Money Exchange SQLite database from the week 4 ER diagram.

Deletes any existing DB file at the default path then creates tables, indexes,
and optional demo rows (skipped if CREATE_ONLY=1 in environment).
"""

from __future__ import annotations

import os
import sqlite3
from pathlib import Path

DATABASE_NAME = "money_exchange.sqlite"


SCHEMA_SQL = """
-- Reference: CUSTOMER ↔ CURRENCY M:N realised as ACCOUNT (per ER note)

CREATE TABLE customer (
    customer_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    referred_by_customer_id INTEGER REFERENCES customer (customer_id),
    full_name             TEXT NOT NULL,
    email                 TEXT NOT NULL UNIQUE,
    phone                 TEXT,
    kyc_status            TEXT NOT NULL DEFAULT 'pending'
        CHECK (kyc_status IN ('pending', 'verified', 'rejected', 'suspended'))
);

CREATE TABLE currency (
    currency_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    pegged_to_currency_id INTEGER REFERENCES currency (currency_id),
    iso_code              TEXT NOT NULL UNIQUE,
    name                  TEXT NOT NULL,
    decimal_places        INTEGER NOT NULL DEFAULT 2 CHECK (decimal_places BETWEEN 0 AND 18)
);

CREATE TABLE account (
    account_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id     INTEGER NOT NULL REFERENCES customer (customer_id),
    currency_id     INTEGER NOT NULL REFERENCES currency (currency_id),
    balance         REAL NOT NULL DEFAULT 0 CHECK (balance >= 0),
    status          TEXT NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'frozen', 'closed')),
    opened_at       TEXT NOT NULL DEFAULT (datetime('now')),
    UNIQUE (customer_id, currency_id)
);

CREATE TABLE exchange_rate (
    rate_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    from_currency_id  INTEGER NOT NULL REFERENCES currency (currency_id),
    to_currency_id    INTEGER NOT NULL REFERENCES currency (currency_id),
    mid_rate          REAL NOT NULL CHECK (mid_rate > 0),
    valid_from        TEXT NOT NULL DEFAULT (datetime('now')),
    spread_bps        INTEGER NOT NULL DEFAULT 0 CHECK (spread_bps >= 0 AND spread_bps <= 10000),
    CHECK (from_currency_id <> to_currency_id),
    UNIQUE (from_currency_id, to_currency_id, valid_from)
);

CREATE TABLE fx_transaction (
    transaction_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    from_account_id   INTEGER NOT NULL REFERENCES account (account_id),
    to_account_id     INTEGER NOT NULL REFERENCES account (account_id),
    exchange_rate_id  INTEGER NOT NULL REFERENCES exchange_rate (rate_id),
    amount_sold       REAL NOT NULL CHECK (amount_sold > 0),
    status            TEXT NOT NULL DEFAULT 'completed'
        CHECK (status IN ('pending', 'completed', 'failed', 'reversed')),
    CHECK (from_account_id <> to_account_id)
);

CREATE INDEX idx_account_customer ON account (customer_id);
CREATE INDEX idx_account_currency ON account (currency_id);
CREATE INDEX idx_rate_from_currency ON exchange_rate (from_currency_id);
CREATE INDEX idx_rate_to_currency ON exchange_rate (to_currency_id);
CREATE INDEX idx_txn_from_account ON fx_transaction (from_account_id);
CREATE INDEX idx_txn_to_account ON fx_transaction (to_account_id);
CREATE INDEX idx_txn_rate ON fx_transaction (exchange_rate_id);
"""

DEMO_INSERTS = """
INSERT INTO customer (full_name, email, phone, kyc_status) VALUES
  ('Ada Lovelace', 'ada@example.com', '+64-555-0100', 'verified'),
  ('Alan Turing', 'alan@example.com', '+44-555-0200', 'verified');

UPDATE customer SET referred_by_customer_id = 1 WHERE customer_id = 2;

INSERT INTO currency (iso_code, name, decimal_places) VALUES
  ('NZD', 'New Zealand Dollar', 2),
  ('USD', 'US Dollar', 2),
  ('EUR', 'Euro', 2);

INSERT INTO currency (iso_code, name, decimal_places, pegged_to_currency_id) VALUES
  ('XXX', 'Demo Pegged Unit', 2, 2);

INSERT INTO account (customer_id, currency_id, balance, status) VALUES
  (1, 1, 5000.00, 'active'),
  (1, 2, 1200.50, 'active'),
  (2, 2, 300.00, 'active');

INSERT INTO exchange_rate (from_currency_id, to_currency_id, mid_rate, spread_bps)
VALUES (1, 2, 0.58, 25), (2, 1, 1.724, 25);

INSERT INTO fx_transaction (
    from_account_id, to_account_id, exchange_rate_id, amount_sold, status
) VALUES (1, 2, 1, 100.00, 'completed');
"""


def main() -> None:
    base = Path(__file__).resolve().parent
    db_path = base / DATABASE_NAME

    if db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(SCHEMA_SQL)

    create_only = os.environ.get("CREATE_ONLY", "").strip() in ("1", "true", "yes")
    if not create_only:
        conn.executescript(DEMO_INSERTS)

    conn.commit()
    conn.close()
    action = "schema only" if create_only else "schema + demo data"
    print(f"Created {db_path} ({action}).")


if __name__ == "__main__":
    main()
