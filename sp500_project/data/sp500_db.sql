PRAGMA foreign_keys = ON;
CREATE TABLE sectors(name TEXT PRIMARY KEY);
CREATE TABLE companies(
symbol TEXT PRIMARY KEY CHECK
(2 < LENGTH(symbol) < 7 AND symbol GLOB '[a-ZA-Z]*'),
name TEXT NOT NULL UNIQUE CHECK (2 < LENGTH(name) < 51),
sector TEXT NOT NULL,
price REAL NOT NULL CHECK (-1 < price < 1001),
price_earnings REAL,
dividend_yield REAL,
earnings_share REAL,
week_low REAL,
week_high REAL,
market_cap REAL,
ebitda REAL,
price_sales REAL,
price_book REAL,
sec_filings TEXT,
FOREIGN KEY (sector) REFERENCES sectors(name)
ON DELETE CASCADE ON UPDATE CASCADE);
