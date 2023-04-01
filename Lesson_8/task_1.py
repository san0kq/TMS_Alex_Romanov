"""
1. Декодировать в строку байтовое значение: b'r\xc3\xa9sum\xc3\xa9'. Затем
результат преобразовать в байтовый вид в кодировке ‘Latin1’ и затем результат
снова декодировать в строку (результаты всех преобразований выводить на экран).

"""

string: bytes = b'r\xc3\xa9sum\xc3\xa9'
print(string)
string2: str = string.decode('utf-8')
print(string2)
string3: bytes = string2.encode('Latin1')
print(string3)
string4: str = string3.decode('Latin1')
print(string4)
