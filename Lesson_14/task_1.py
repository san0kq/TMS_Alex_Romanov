"""
Создать класс Contact, у которого должны быть атрибуты email, phone,
first_name, last_name. Сделать валидации, что email - строка, содержащая символ
@ и правая часть находится в списке из: gmail.com, yandex.ru, ya.ru, yahoo.com

phone - номер телефона начинается с символа +, код страны находится в списке
375, 48, 374

first_name, last_name - строки, начинающиеся с большой буквы и длиной от 5 до
15  символов

Все проверки реализовать через property
"""


class Contact:
    def __init__(
            self,
            email: str,
            phone: str,
            first_name: str,
            last_name: str
    ) -> None:
        self.email = email
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def _validation_email(value: str) -> None:
        if len(value.split('@')) != 2:
            raise ValueError('Email must contains only one @.')
        if value.split('@')[1] not in ('gmail.com', 'yandex.ru',
                                       'ya.ru', 'yahoo.com'):
            raise ValueError('This email is not supported.')

    @staticmethod
    def _validation_phone(value: str) -> None:
        if value[0:4] not in ('+375', '+374') and value[1:3] != '+48':
            raise ValueError('The phone number must start with a plus sign'
                             ' and the code 375, 374 or 48.')
        if not value[1::].isdigit():
            raise ValueError('The phone number must be digital.')

    @staticmethod
    def _validation_name(value: str) -> None:
        if not value.istitle():
            raise ValueError('The first letter of the first name or last name'
                             ' must be capitalized.')
        if not 5 <= len(value) <= 15:
            raise ValueError('The length of the first name or last name should'
                             ' be between 5 and 15 characters.')

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._validation_email(value=value)
        self._email = value

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:
        self._validation_phone(value=value)
        self._phone = value

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        self._validation_name(value=value)
        self._first_name = value

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        self._validation_name(value=value)
        self._last_name = value
