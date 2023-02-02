"""
5. Прочитать сохранённый csv-файл и сохранить данные в excel-файл, кроме возраста - столбец с этими данными
не нужен.
"""

import openpyxl
import csv
import string
from random import randint

with open('task_4.csv') as csv_file:
    wb = openpyxl.Workbook()                   # открыли новую таблицу
    wb.create_sheet('Page 1', 0)               # создаём в таблице новую страницу
    ws = wb['Page 1']                          # переключаемся на страницу для работы с ней
    col = string.ascii_uppercase               # список нужных столбцов, в которые будет вести запись ниже
    counter = 2                                # счетчик для движения по столбцу, используется ниже
    letter = 0                                 # счетчик для движения по строке, то есть по буквам в списке выше

    for row in csv.reader(csv_file, delimiter=','):
        for value in row:
            if value == 'age':                 # не добавляет название столбца age, как сказано в условии
                continue
            elif len(value) != 6 and value.isdigit():  # Если значение является возрастом, меняем его на случайный тел.
                ws[col[letter]+str(counter)] = f'{randint(100, 999)}-{randint(10, 99)}-{randint(10, 99)}'
                counter += 1
            else:
                ws[col[letter]+str(counter)] = value
                counter += 1
        letter += 1                           # добавляем 1 для перехода на следующий столбец, то есть на букву в спике
        counter = 2                           # возвращаем значение к изначальному для движения по другому столбцу вниз

    for index in range(1, letter):            # цикл для добавления в первую строку значений Person
        ws[col[index]+'1'] = f'Person {index}'

    wb.save('task_5.xlsx')                    # сохраняем документ
