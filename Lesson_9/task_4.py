"""
Написать функцию, которая принимает n-ое количество координат точек. И в ответ
возвращает длину маршрута между ними. Каждая координата представлена
кортежем, состоящим из двух объектов типа int.
"""

from math import sqrt


def distance(*args: tuple[int, int]) -> float:
    result = 0
    for index in range(1, len(args)):
        length = sqrt((args[index][0] - args[index - 1][0])**2
                      + (args[index][1] - args[index - 1][1])**2)
        result += length
    return round(result, 2)


print(distance((1, 2), (2, 2), (3, 3), (5, 5), (8, 8)))
