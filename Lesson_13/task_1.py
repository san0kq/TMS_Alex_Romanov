"""
Создать класс Alphabet, в который в инициализаторе будут передаваться
параметры: end - str и lower - bool (по дефолту True)
Объекты класса должны быть итерабельными и на каждой итерации возвращать букву
из латинского алфавита до тех пор, пока не будет достигнута буква, которая
передана в инициализатор в атрибуте end. Если атрибут lower=True, то возвращаем
 буквы в маленьком регистре, если False, то в большом
"""

from string import ascii_lowercase, ascii_uppercase
from typing import Iterator


class AlphabetIterator:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __next__(self) -> str:
        if self.start > self.end:
            raise StopIteration
        self.start += 1
        return chr(self.start - 1)


class Alphabet:
    def __init__(self, end: str, lower: bool = True) -> None:
        self.end = end
        self.lower = lower

    def __iter__(self) -> AlphabetIterator:
        if self.lower:
            self.start = 97
            self.last = ord(self.end.lower())
        else:
            self.start = 65
            self.last = ord(self.end.upper())

        return AlphabetIterator(start=self.start, end=self.last)


# second solution
class Alphabet2:
    def __init__(self, end: str, lower: bool = True) -> None:
        self.end = end
        self.lower = lower

    def __iter__(self) -> Iterator[str]:
        index = ascii_lowercase.index(self.end.lower())
        if self.lower:
            return iter(ascii_lowercase[:index + 1])
        return iter(ascii_uppercase[:index + 1])
