import socket
from views.get import get
from views.post import post


HOST = ('localhost', 5000)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(HOST)
server.listen()

def find_page(request_data: str) -> bytes:
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n '
    HDRS_404 = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=utf-8\r\n\r\n '
    try:
        page = request_data.split(' ')[1]
        return HDRS.encode() + get(page=page[1::])
    except IndexError:
        return (HDRS_404 + 'Sorry, no page...').encode()


while True:
    conn, addr = server.accept()
    request_data = conn.recv(4096).decode()
    print(request_data)
    if request_data.split(' ')[0] == 'POST':
        conn.send(post(request_data.split('\r\n\r\n')[-1]))
    else:
        conn.send(find_page(request_data=request_data))
