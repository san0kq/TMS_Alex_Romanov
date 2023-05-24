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
    
    elif page == 'edit':
        with open('templates/edit.html') as file:
            html = file.read()
        
        return html.encode()


    elif page == 'delete':
        with open('templates/delete.html') as file:
            html = file.read()
        
        return html.encode()

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
              <h2>{data[0][1]}</h2>
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
