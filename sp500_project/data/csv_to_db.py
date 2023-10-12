import sqlite3
import csv

connector = sqlite3.connect('sp500.db')
cursor = connector.cursor()

cursor.execute('PRAGMA foreign_keys = ON;')
cursor.execute('CREATE TABLE sectors(name TEXT PRIMARY KEY);')
cursor.execute("""
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
""")

with open('sp500.csv') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        try:
            cursor.execute('INSERT INTO sectors(name) VALUES(?);',
                            (row['Sector'], ))
        except sqlite3.IntegrityError:
            continue

with open('sp500.csv') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        cursor.execute('INSERT INTO companies('
                       'symbol,'
                       'name,'
                       'sector,'
                       'price,'
                       'price_earnings,'
                       'dividend_yield,'
                       'earnings_share,'
                       'week_low,'
                       'week_high,'
                       'market_cap,'
                       'ebitda,'
                       'price_sales,'
                       'price_book,'
                       'sec_filings) '
                       'VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);',
                       (row['Symbol'], row['Name'], row['Sector'],
                        row['Price'], row['Price/Earnings'],
                        row['Dividend Yield'], row['Earnings/Share'],
                        row['52 Week Low'], row['52 Week High'],
                        row['Market Cap'], row['EBITDA'], row['Price/Sales'],
                        row['Price/Book'], row['SEC Filings'],
                        ))
connector.commit()
connector.close()
