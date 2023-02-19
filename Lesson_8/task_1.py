"""
1. Декодировать в строку байтовое значение: b'r\xc3\xa9sum\xc3\xa9'. Затем
результат преобразовать в байтовый вид в кодировке ‘Latin1’ и затем результат
снова декодировать в строку (результаты всех преобразований выводить на экран).

"""

string = b'r\xc3\xa9sum\xc3\xa9'
print(string)
string = string.decode('utf-8')
print(string)
string = string.encode('Latin1')
print(string)
string = string.decode('Latin1')
print(string)
