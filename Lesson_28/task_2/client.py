import socket

HOST = ('localhost', 5000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(HOST)

text = input('Enter your text: ')

client.sendall(text.encode())
client.shutdown(socket.SHUT_WR)
result = ''
while True:
    message = client.recv(1024)
    if not message:
        break
    result += message.decode()

client.close()
print(result)
