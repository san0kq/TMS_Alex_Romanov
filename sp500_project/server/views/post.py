from urllib.parse import parse_qs
import sqlite3

from .get import get


HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n '
HDRS_400 = 'HTTP/1.1 400 Bad Request\r\nContent-Type: text/html; charset=utf-8\r\n\r\n '


def post(data: str) -> bytes:
    connector = sqlite3.connect('sp500.db')
    cursor = connector.cursor()
    data = parse_qs(data)

    if len(data) == 1:
        try:
            cursor.execute('DELETE FROM companies WHERE symbol = ?;',
                           (data['symbol'][0], ))
            connector.commit()
            connector.close()
            return HDRS.encode() + get(page='main') 
        except Exception:
            return (HDRS_400 + 'Database operation error').encode()
    else:
        if data['action'][0] == 'update':
            
            try:
                cursor.execute('UPDATE companies SET '
                            'name = ?, '
                            'sector = ?, '
                            'price = ?, '
                            'price_earnings = ?, '
                            'dividend_yield = ?, '
                            'earnings_share = ?, '
                            'week_low = ?, '
                            'week_high = ?, '
                            'market_cap = ?, '
                            'ebitda = ?, '
                            'price_sales = ?, '
                            'price_book = ?, '
                            'sec_filings = ? '
                            'WHERE symbol = ?;',
                            (data['name'][0], data['sector'][0],
                             data['price'][0], data['price_earnings'][0],
                             data['dividend_yield'][0], 
                             data['earnings_share'][0],
                             data['week_low'][0], data['week_high'][0],
                             data['market_cap'][0], data['ebitda'][0],
                             data['price_sales'][0], data['price_book'][0],
                             data['sec_filings'][0], data['symbol'][0]))
                connector.commit()
                connector.close()
                return HDRS.encode() + get(page='main') 
            except Exception:
                return (HDRS_400 + 'Database operation error').encode()

        elif data['action'][0] == 'create':
            try:
                cursor.execute('INSERT INTO companies ('
                               'name, symbol, sector, price, price_earnings, '
                               'dividend_yield, earnings_share, week_low, '
                               'week_high, market_cap, ebitda, price_sales, '
                               'price_book, sec_filings) VALUES '
                               '(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);',
                               (data['name'][0], data['symbol'][0],
                                data['sector'][0], data['price'][0], 
                                data['price_earnings'][0],
                                data['dividend_yield'][0], 
                                data['earnings_share'][0],
                                data['week_low'][0], data['week_high'][0],
                                data['market_cap'][0], data['ebitda'][0],
                                data['price_sales'][0], data['price_book'][0],
                                data['sec_filings'][0]))    
                connector.commit()
                connector.close()
                return HDRS.encode() + get(page='main')         
            except Exception:
                return (HDRS_400 + 'Database operation error').encode()
    