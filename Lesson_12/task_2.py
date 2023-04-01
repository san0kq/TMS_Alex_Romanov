"""
Создать класс книга Book, который будет хранить следующую информацию о книге:
name - название
description - краткое описание
pages - количество страниц
author - автор
price - цена

Также у класса дожны быть методы:
to_dict(self) - возвращает информацию о книге в виде словаря
contains_word(self, word) - возвращает True, если в названии или описании есть
переданное слово
Также А также между объектами этого класса должны поддерживаться операции
>, <, >=, <=, которые сравнивают книги по количеству страниц
==, != - сравнивают совпадает ли вся информация у двух книг

Также создать класс Library, который будет иметь свойство books - при
инициализации пустой список.
Также добавить методы
add_book(self, book) # добавляет книгу в свойство books
get_books(self) # возвращает списко с информацией о всех книгах,
каждая информация о книге должна быть в виде словаря
remove_book(self, book) - удаляет книгу по значнию из свойства books
find_the_biggest_book(self) - возвращает книгу, в которой больше всего страниц,
если книг нет, то вызывает ошибку EmptyLibraryError
Также класс библиотека должен поддерживать метод len(), который будет
возвращать количество книг в библиотеке
"""

from re import search
from typing import Optional, TypeVar

from errors import EmptyLibraryError

OtherTypes = TypeVar('OtherTypes', 'Book', float, int)


class Book:
    def __init__(
            self,
            name: str,
            description: str,
            pages: int,
            author: str,
            price: float
    ) -> None:
        self.name = name
        self.description = description
        self.pages = pages
        self.author = author
        self.price = price

    def to_dict(self) -> dict[str, object]:
        result = {
            'name': self.name,
            'description': self.description,
            'pages': self.pages,
            'author': self.author,
            'price': self.price,
        }
        return result

    def contains_word(self, word: str) -> Optional[bool]:
        if search(rf'\b{word}\b', self.name + ' ' + self.description):
            return True
        else:
            return None

    def __gt__(self, other: OtherTypes) -> bool:
        return self.pages > other

    def __lt__(self, other: OtherTypes) -> bool:
        return self.pages < other

    def __ge__(self, other: OtherTypes) -> bool:
        return self.pages >= other

    def __le__(self, other: OtherTypes) -> bool:
        return self.pages <= other

    def __eq__(self, other: object) -> bool:
        return self.to_dict() == other

    def __ne__(self, other: object) -> bool:
        return self.to_dict() != other


class Library:
    def __init__(self) -> None:
        self.books: list['Book'] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def get_books(self) -> list[dict[str, object]]:
        return [book.to_dict() for book in self.books]

    def remove_book(self, book: Book) -> None:
        self.books.remove(book)

    def find_the_biggest_book(self) -> Optional[Book]:
        if len(self.books) != 0:
            return sorted(self.books)[-1]
        else:
            raise EmptyLibraryError('No books in the library')

    def __len__(self) -> int:
        return len(self.books)


book1 = Book(
    'Grokking Algorithms',
    'An illustrated guide for programmers and other curious people',
    256, 'Aditya Bhargava',
    33
)
book2 = Book(
    "Learn Python",
    "This book will teach you how to learn python",
    1000,
    "Luhts",
    49
)
book3 = Book(
    'Design Patterns',
    'Elements of Reusable Object-Oriented Software',
    288,
    'Gangs of four',
    132
)


print(book2.contains_word('Learn'))

lib = Library()
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)

print(len(lib))
biggest_book = lib.find_the_biggest_book()
print(biggest_book)
if biggest_book is not None:
    print(biggest_book.to_dict())
print(lib.get_books())
print(book3 < book2)
