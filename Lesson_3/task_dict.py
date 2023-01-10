dict_1 = {'first_name': 'Alexander', 'last_name': 'Romanov', 'age': 28}
dict_2 = dict(email='admin@gmail.com', password='qwerty')
dict_3 = dict([('apple', 'red'), ('banana', 'yellow')])
dict_4 = dict.fromkeys(['key1', 'key2'], 'some_value')

print(dict_1)
print(dict_2)
print(dict_3)
print(dict_4)

dict_1['profession'] = 'Junior Python Developer'
print(dict_1)
print(dict_2.items())
print(dict_3.get('banana'))
print(dict_4.keys())
print(dict_2.pop('password'))
print(dict_2)
