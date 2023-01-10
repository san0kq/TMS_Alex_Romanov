bytes_1 = b'bytes'
bytes_2 = 'байты'.encode('utf-8')

print(bytes_1)
print(bytes_2)

print(b'\xd0\xb1\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'.decode('utf-8'))
