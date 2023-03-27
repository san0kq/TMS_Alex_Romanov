"""
Создать класс Message, который принимает атрибут text, который является текстом
какого-то сообщения. Также в инициализаторе у класса задать атрибут created_at,
в который сохранить текущий timestamp (unix time)
Создать класс Song, который принимает два атрибута: name - название песни и
author - автор песни. Также в инициализаторе у класса задать атрибут
created_at, в который сохранить текущий timestamp (unix time)

Создать класс-дескриптор Censored, который будет валидировать поля name и text
у этих классов. Правило валидации: если в тексте сообщения или названии песни
найдётся слово fuck (в любом регистре), то перед присваиванием этого текста
атрибуту класса, дескриптор заменяет это слово на ****
"""

from time import time
import re
from typing import Optional, Any


class Censored:
    def __set_name__(self, owner: type, name: str) -> None:
        self.name = '_' + name

    def __get__(self,
                instance: Optional[object],
                owner: Optional[type]) -> Any:
        return getattr(instance, self.name)

    def __set__(self, instance: Optional[object], value: str) -> None:
        censored_value = re.sub(r'\b[fF][uU][cC][kK]\b', '****', value)
        setattr(instance, self.name, censored_value)


class Message:
    text = Censored()

    def __init__(self, text: str) -> None:
        self.text = text
        self.created_at = time()


class Song:
    name = Censored()

    def __init__(self, name: str, author: str) -> None:
        self.name = name
        self.author = author
        self.created_at = time()
