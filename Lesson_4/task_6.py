# Initialize two integers
number_1 = int(input('Введите первое целое число: '))
number_2 = int(input('Введите второе целое число: '))

if number_1 > 10 and number_2 > 10:
    print('Оба числа больше 10')
elif number_1 > 10 or number_2 > 10:
    print('Одно из чисел больше 10')
elif not bool(number_1):  # if number_1 not False
    print('Условие с помощью преобразования типов')
