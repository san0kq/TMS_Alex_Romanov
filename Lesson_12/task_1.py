"""
Создать класс Vector, который при инициализации принимает два значения-кортежа:
(point_x1, point_y1) и (point_x2, point_y2), которые можно ассоциировать с
координатами точек, которые образуют отрезок (вектор)
У класса реализовать метод length(self) - возвращает длину ветора (число)
А также между объектами этого класса должны поддерживаться операции
>, <, >=, <=, ==, !=
"""
from typing import Any


class Vector:
    def __init__(self,
                 point_1: tuple[int, int],
                 point_2: tuple[int, int]) -> None:
        self.point_x1 = point_1[0]
        self.point_y1 = point_1[1]
        self.point_x2 = point_2[0]
        self.point_y2 = point_2[1]

    def length(self) -> float:
        result = round(((self.point_x2 - self.point_x1)**2
                       + (self.point_y2 - self.point_y1)**2)**0.5, 2)
        return result

    def __gt__(self, other: Any) -> bool:
        return self.length() > other

    def __lt__(self, other: Any) -> bool:
        return self.length() < other

    def __ge__(self, other: Any) -> bool:
        return self.length() >= other

    def __le__(self, other: Any) -> bool:
        return self.length() <= other

    def __eq__(self, other: Any) -> bool:
        return self.length() == other

    def __ne__(self, other: Any) -> bool:
        return self.length() != other


vector_1 = Vector((1, 1), (3, 2))
vector_2 = Vector((1, 1), (2, 2))

print(vector_1.length(), vector_2.length())
print(vector_1 > vector_2)
print(vector_1 < vector_2)
print(vector_1 >= vector_2)
print(vector_1 <= vector_2)
print(vector_1 == vector_2)
print(vector_1 != vector_2)
