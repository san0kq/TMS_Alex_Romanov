while True:
    name = input('Введите ваше имя: ')
    age = input('Введите ваш возраст '
                '(введите STOP, чтобы остановить программу): ')

    if age == 'STOP':  # Stopping code execution
        break

    try:
        age = int(age)
        if age <= 0:
            print('Ошибка, повторите ввод')
        elif age < 10:
            print(f'Привет, шкет {name}')
        elif age <= 18:
            print(f'Как жизнь, {name}?')
        elif age < 100:
            print(f'Что желаете, {name}?')
        else:
            print(f'{name}, вы лжёте - в наше время столько не живут...')
    except ValueError:
        print('Ошибка, повторите ввод')
