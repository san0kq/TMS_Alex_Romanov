import socket
from collections import Counter
import re

HOST = ('localhost', 5000)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(HOST)
server_socket.listen()

def most_popular_word(text: str) -> str:
    if not text:
        return 'Your request is empty.'
    else:
        words = re.sub(r"[^\w\s-]", "", text)
        words = words.split()
        word_counts = Counter(words)
        return word_counts.most_common(1)[0][0]

while True:
    conn, addr = server_socket.accept()
    print(f'Connected: {addr[0]}:{addr[1]}')
    result = b''
    while True:
        data = conn.recv(1024)
        if data.decode()[-1] == '#':
            result += data[:-1]
            print(f'Connection closed: {addr[0]}:{addr[1]}')
            break
        result += data

    word = most_popular_word(text=result.decode())
    conn.send(word.encode())
    conn.close()
