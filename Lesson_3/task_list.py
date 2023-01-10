list_1 = [1, 2, 3, 4, 5]
list_2 = list('new_list')
list_3 = 'List 3'.split()

print(list_1)
print(list_2)
print(list_3)

list_1.append(6)
list_2.sort()
list_3[1] = 'List'
list_2.append(list_1.pop())
list_3.extend(list_2)

print(list_1)
print(list_2)
print(list_3)
