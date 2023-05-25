import sqlite3


def get(page: str) -> bytes:
    connector = sqlite3.connect('sp500.db')
    cursor = connector.cursor()

    if not page or page == 'main':
        data = cursor.execute('SELECT symbol, name FROM companies;')
        with open('templates/main/main_1.html') as file:
            html_1 = file.read()
            for company in data.fetchall():
                html_1 += f"""
                <div class="company">
                    <a href="/{company[0]}">{company[1]}</a>
                    | {company[0]}
                </div>
            """
        with open('templates/main/main_2.html') as file:
            html_2 = file.read()
        html = html_1 + html_2
        connector.close()
        return html.encode()
    
    elif len(page.split('/')) == 2:
        with open('templates/company_update/company_update_1.html') as file:
            html_1 = file.read()
        with open('templates/company_update/company_update_2.html') as file:
            html_2 = file.read()
        data = cursor.execute('SELECT * FROM companies WHERE symbol = ?;',
                              (page.split('/')[1], ))
        data = data.fetchall()
        sectors = cursor.execute('SELECT * FROM sectors WHERE name != ?;',
                                 (data[0][2], ))
        sectors = sectors.fetchall()
        html_1 += f"""
        <label for="symbol">Symbol:</label>
        <input type="text" id="symbol" name="symbol" value="{data[0][0]}">

        <label for="name">Company name:</label>
        <input type="text" id="name" name="name" value="{data[0][1]}">


        <label for="sector">Sector:</label>

        <select id="sector" name="sector" value="">
          <option>{data[0][2]}</option>
          <option>{sectors[0][0]}</option>
          <option>{sectors[1][0]}</option>
          <option>{sectors[2][0]}</option>
          <option>{sectors[3][0]}</option>
          <option>{sectors[4][0]}</option>
          <option>{sectors[5][0]}</option>
          <option>{sectors[6][0]}</option>
          <option>{sectors[7][0]}</option>
          <option>{sectors[8][0]}</option>
          <option>{sectors[9][0]}</option>
        </select>

        <label for="price">Price:</label>
        <input type="text" id="price" name="price" value="{data[0][3]}">


        <label for="price_earnings">Price earnings:</label>
        <input type="text" id="price_earnings" name="price_earnings" value="{data[0][4]}">


        <label for="dividend_yield">Dividend yield:</label>
        <input type="text" id="dividend_yield" name="dividend_yield" value="{data[0][5]}">
        
        
        <label for="earnings_share">Earnings share:</label>
        <input type="text" id="earnings_share" name="earnings_share" value="{data[0][6]}">
        
        
        <label for="week_low">Week low:</label>
        <input type="text" id="week_low" name="week_low" value="{data[0][7]}">
        
        
        <label for="week_high">Week high:</label>
        <input type="text" id="week_high" name="week_high" value="{data[0][8]}">
        
        
        <label for="market_cap">Market cap:</label>
        <input type="text" id="market_cap" name="market_cap" value="{data[0][9]}">
        
        
        <label for="ebitda">EBITDA:</label>
        <input type="text" id="ebitda" name="ebitda" value="{data[0][10]}">
        
        
        <label for="price_sales">Price sales:</label>
        <input type="text" id="price_sales" name="price_sales" value="{data[0][11]}">
        
        
        <label for="price_book">Price book:</label>
        <input type="text" id="price_book" name="price_book" value="{data[0][12]}">
        
        
        <label for="sec_filings">SEC filings:</label>
        <input type="text" id="sec_filings" name="sec_filings" value="{data[0][13]}">
        """

        return (html_1 + html_2).encode()


    elif page == 'delete':
        with open('templates/delete.html') as file:
            html = file.read()
        
        return html.encode()

    elif page == 'add':
        with open('templates/company_create/company_create_1.html') as file:
            html_1 = file.read()

        with open('templates/company_create/company_create_2.html') as file:
            html_2 = file.read()
        
        sectors = cursor.execute('SELECT * FROM sectors;')
        sectors = sectors.fetchall()

        html_1 += f"""
        <select id="sector" name="sector" value="">
          <option>{sectors[0][0]}</option>
          <option>{sectors[1][0]}</option>
          <option>{sectors[2][0]}</option>
          <option>{sectors[3][0]}</option>
          <option>{sectors[4][0]}</option>
          <option>{sectors[5][0]}</option>
          <option>{sectors[6][0]}</option>
          <option>{sectors[7][0]}</option>
          <option>{sectors[8][0]}</option>
          <option>{sectors[9][0]}</option>
          <option>{sectors[10][0]}</option>
        </select>
        """
        return (html_1 + html_2).encode()

    else:
        data = cursor.execute('SELECT * FROM companies WHERE symbol = ?;', 
                              (page, ))
        data = data.fetchall()
        connector.close()

        with open('templates/company/company_1.html') as file:
            html_1 = file.read()
            html_1 += f"<title>{data[0][1]}</title>"
        
        with open('templates/company/style.html') as file:
            style = file.read()

        html_2 = f"""
          <div id="company-info">
            <table>
                <tr>
                    <td>
                        <h2>{data[0][1]}</h2>
                    </td>
                    <td>
                        <h2><a href="/update/{data[0][0]}">Edit company</a></h2>
                    </td>
                </tr>
            </table>
          <table>
              <tr>
                  <th>SEC Filings:</th>
                  <td><a href="{data[0][13]}">{data[0][13]}</a></td>
              </tr>
              <tr>
                  <th>Sector:</th>
                  <td>{data[0][2]}</td>
              </tr>
              <tr>
                  <th>Price:</th>
                  <td>{data[0][3]}</td>
              </tr>
              <tr>
                  <th>Price earnings:</th>
                  <td>{data[0][4]}</td>
              </tr>
              <tr>
                  <th>Dividend yield:</th>
                  <td>{data[0][5]}</td>
              </tr>
              <tr>
                  <th>Earnings share:</th>
                  <td>{data[0][6]}</td>
              </tr>
              <tr>
                  <th>Week low:</th>
                  <td>{data[0][7]}</td>
              </tr>
              <tr>
                  <th>Week high:</th>
                  <td>{data[0][8]}</td>
              </tr>
              <tr>
                  <th>Market cap:</th>
                  <td>{data[0][9]}</td>
              </tr>
              <tr>
                  <th>EBITDA:</th>
                  <td>{data[0][10]}</td>
              </tr>
              <tr>
                  <th>Price sales:</th>
                  <td>{data[0][11]}</td>
              </tr>
              <tr>
                  <th>Price book:</th>
                  <td>{data[0][12]}</td>
              </tr>
          </table>
          <p><a href="/main">All companies</a></p>
      </div>
      </body>
      </html>
      """
        return (html_1 + style + html_2).encode()
