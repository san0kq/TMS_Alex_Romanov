set_1 = set('Hello World')
set_2 = {1, 2, 3, 3, 4, 5, 6}

print(set_1)
print(set_2)

set_1.add(1)
print(set_1)

set_3 = set.union(set_1, set_2)
set_4 = set.intersection(set_1, set_3)
set_5 = set.difference(set_2, set_1)
set_6 = set.difference(set_1, set_2)

print(set_1)
print(set_2)
print(set_3)
print(set_4)
print(set_5)
print(set_6)
