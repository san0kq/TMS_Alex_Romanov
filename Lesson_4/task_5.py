# Initialize two integers
number_1 = int(input('Введите первое целое число: '))
number_2 = int(input('Введите второе целое число: '))

if number_1 == number_2:
    print('Числа равны')
elif number_1 > number_2:
    print('Первое число больше второго')
else:
    print('Отработала секция else')
