"""
4. Прочитать сохранённый json-файл и записать данные на диск в csv-файл, первой
строкой которого озоглавив каждый столбец и добавив новый столбец "телефон".
"""

import json
import csv
from random import randint

with open('task_3.json') as json_file, open('task_4.csv', 'w') as csv_file:
    my_dict = json.load(json_file)
    csv_writer = csv.DictWriter(csv_file, delimiter=',',
                                fieldnames=['id', 'name', 'age', 'phone'])
    csv_writer.writeheader()
    for key, values in my_dict.items():
        csv_writer.writerow({'id': key,
                             'name': values[0],
                             'age': values[1],
                             'phone': f'{randint(100, 999)}-{randint(10, 99)}-'
                                      f'{randint(10, 99)}'
                             })
