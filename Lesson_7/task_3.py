words = ('hello', 'dog', 'level', 'computer', 'madam', 'noon')

print(list(filter(lambda x: x == x[::-1], words)))
