def what_number(number: str) -> None:
    """This is function to check number's type in string"""
    if number.isdigit():
        print(f'Вы ввели положительное целое число: {number}')
    elif '-' in number and '.' in number and number.count('-') == 1 \
            and number.count('.') == 1:
        new_str = number.replace('-', '')
        new_str = new_str.replace('.', '')
        if new_str.isdigit():
            print(f'Вы ввели отрицательное дробное число: {float(number)}')
        else:
            print(f'Вы ввели некорректное число: {number}')
    elif '-' in number and number.count('-') == 1:
        new_str = number.replace('-', '')
        if new_str.isdigit():
            print(f'Вы ввели отрицательное целое: {int(number)}')
        else:
            print(f'Вы ввели некорректное число: {number}')
    elif '.' in number and number.count('.') == 1:
        new_str = number.replace('.', '')
        if new_str.isdigit():
            print(f'Вы ввели положительное дробное число: {float(number)}')
        else:
            print(f'Вы ввели некорректное число: {number}')

    else:
        print(f'Вы ввели некорректное число: {number}')


what_number('-6.7')
what_number('5')
what_number('5.4r')
what_number('-.777')
