"""
Создать класс Stack, который будет соответствовать структуре данных стек
(LIFO - last in first out) У класса должны быть методы:
push(self, element) - добавляет элемент в стек
pop(self) - выдаёт последний элемент из стека и удаляет его в стеке.
Если стек пустой, то возвращает None
is_empty(self) - возвращает True, если стек пустой, False - если нет
peek(self) - возвращает верхушку стека (последний добавленный элемент),
в ином случае возвращает None

Использовать этот класс Stack для решения следующей задачи:
На вход даёт строка из скобок "[](){}"
Реализовать функцию (обычную, НЕ метод в классе), которая на вход принимает
строку из скобок И возвращает True, если все скобки закрыты, False - если нет
"""
from typing import Any, Optional


class Stack:
    def __init__(self) -> None:
        self._stack: list[Any] = []

    def push(self, element: Any) -> None:
        self._stack.append(element)

    def pop(self) -> Optional[Any]:
        if self._stack:
            return self._stack.pop()
        else:
            return None

    def is_empty(self) -> bool:
        return not bool(self._stack)

    def peek(self) -> Optional[Any]:
        if self._stack:
            return self._stack[-1]
        else:
            return None


def valid_parentheses(string: str) -> bool:
    if len(string) % 2 != 0:
        return False
    stack = Stack()
    for par in string:
        if par in '({[':
            stack.push(par)
        else:
            last_par = stack.pop()
            if last_par == '(' and par != ')':
                return False
            elif last_par == '{' and par != '}':
                return False
            elif last_par == '[' and par != ']':
                return False

    return stack.is_empty()


str1 = '{}[]()'
str2 = '{{}{}'
str3 = '(((()'
str4 = '())'
str5 = ']'
str6 = '){'
str7 = '{[()]{}}'

print(valid_parentheses(str1))
print(valid_parentheses(str2))
print(valid_parentheses(str3))
print(valid_parentheses(str4))
print(valid_parentheses(str5))
print(valid_parentheses(str6))
print(valid_parentheses(str7))
