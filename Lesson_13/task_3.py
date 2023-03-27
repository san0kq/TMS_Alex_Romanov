"""
Создать класс LinkedList, который будет являться структурой данных
"связанный список" У класса LinkedList должно быть свойство head
(при инициализации None), которое является ссылкой на первый объект в списке.
Также класс LinkedList должен иметь методы:
1. append(self, element) - добавляет новый элемент в LinkedList
2. reverse(self) - меняет порядок списка, то есть последний элемент текущего
списка должен стать первым элементом нового списка и так далее
3. println(self) - выводит на экран список из всех значений атрибута data для
каждого элемента в порядке того, как эти элименты стоят в списке

Также LinkedList должен поддерживать операции len(linked_lst) -
возвращать количество элементов в списке
for i in linked_lst:
    print(i) # на каждой итерации возвращать по одному элементу списка

Также создать класс Element, у которого должны быть два свойства next
(при инициализации None) и data, которое задаётся при инициализации и
хранит объект класса int. Атрибут data сделать ввиде метода-свойства, в котором
при инициализации проверять, что data находится в range(0, 10000), если нет, то
генерировать ошибку IncorrectDataError Также объекты класса должны поддерживать
операции ==, !=, >=, <=, >, < - сравнивать по атрибуту data
"""
import functools
from typing import Optional, Any


class IncorrectDataError(Exception):
    pass


class LinkedListIterator:
    def __init__(self, head: 'Element') -> None:
        self._head = head

    def __next__(self) -> Optional[int]:
        if not self._head:
            raise StopIteration
        current_element = self._head
        self._head = current_element.next
        return current_element.data


class LinkedList:
    def __init__(self) -> None:
        self._head = None

    def __len__(self) -> int:
        count = 0
        current_element = self._head
        while current_element:
            current_element = current_element.next
            count += 1
        return count

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(head=self._head)

    def append(self, data: int) -> None:
        new_element = Element(data=data)
        if not self._head:
            self._head = new_element
        else:
            current_element = self._head
            while current_element.next:
                current_element = current_element.next
            current_element.next = new_element

    def reverse(self) -> None:
        previous_element = None
        current_element = self._head
        while current_element:
            next_element = current_element.next
            current_element.next = previous_element
            previous_element = current_element
            current_element = next_element
        self._head = previous_element

    def println(self) -> list[int]:
        current_element = self._head
        result = []
        while current_element:
            result.append(current_element.data)
            current_element = current_element.next
        return result


@functools.total_ordering
class Element:
    def __init__(self, data: int) -> None:
        self._next = None
        self.data = data

    def __eq__(self, other: Any) -> bool:
        return self._data < other

    def __lt__(self, other: Any) -> bool:
        return self._data < other

    def __str__(self) -> str:
        return str(self.data)

    @property
    def data(self) -> int:
        return self._data

    @data.setter
    def data(self, data: int) -> None:
        if type(data) != int or not 0 <= data <= 1000:
            raise IncorrectDataError('Data must be a integer within the range '
                                     'of 1 to 1000')
        self._data = data

    @property
    def next(self) -> 'Element':
        return self._next

    @next.setter
    def next(self, element: 'Element') -> None:
        self._next = element


link_list = LinkedList()

link_list.append(1)
link_list.append(5)
link_list.append(2)
link_list.append(10)
print(link_list.println())
link_list.reverse()
print(link_list.println())

for element in link_list:
    print(element)
