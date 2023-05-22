import socket

HOST = ('localhost', 5000)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(HOST)
server_socket.listen()


while True:
    conn, addr = server_socket.accept()  
    print(f'Connected: {addr[0]}:{addr[1]}')
    while True:
        data = conn.recv(1024) 
        if not data:
            print(f'Connection closed.')
            break
        conn.send(data)      
