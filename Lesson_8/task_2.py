"""
2. Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные. Создать
файл и записать в него первые 2 строки и закрыть файл. Затем открыть файл на
редактирование и дозаписать оставшиеся 2 строки. В итоговом файле должны быть 4
строки, каждая из которых должна начинаться с новой строки.

"""

string_1 = input()
string_2 = input()
string_3 = input()
string_4 = input()

with open('task_2.txt', 'w') as file:
    file.write(string_1 + '\n')
    file.write(string_2 + '\n')

with open('task_2.txt', 'a') as file:
    file.write(string_3 + '\n')
    file.write(string_4)
