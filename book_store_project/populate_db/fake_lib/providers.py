from random import randint, choice
from string import ascii_letters, digits, ascii_uppercase
from typing import ParamSpec, Any

from .markov_chains import markov_chains

P = ParamSpec('P')


class EmailProvider:
    def __call__(self, *args: Any, **kwargs: Any) -> str:
        mails = (
            '@gmail.com',
            '@mail.com',
            '@yandex.ru',
            '@ya.ru',
            '@rambler.ru',
        )

        email = choice(ascii_letters)
        for _ in range(randint(4, 10)):
            email += choice(markov_chains.emails_tokens[email[-1]])

        email += choice(mails)

        return email


class PhoneProvider:
    def __call__(self, *args: Any, **kwargs: Any) -> str:
        operators = (
            '+37533',
            '+37529',
            '+37544',
            '+37524',
            '+37525',
            '+37515',
            '+37516',
            '+37517',
            '+37521',
            '+37522',
            '+37523',
        )
        result = choice(operators)
        for _ in range(7):
            result += str(randint(0, 9))

        return result


class BankCardProvider:
    def __call__(self, *args: Any, **kwargs: Any) -> str:
        card_number = ''
        for _ in range(15):
            card_number += choice(digits)
        sum_of_digits = 0
        for index, number_str in enumerate(card_number):
            if index % 2 == 0:
                number = int(number_str) * 2
                if number > 9:
                    number -= 9
            sum_of_digits += int(number_str)

        if sum_of_digits % 10 == 0:  # add a check digit
            card_number += '0'
        else:
            card_number += str(10 - sum_of_digits % 10)

        return card_number


class NameProvider:
    def __call__(self, *args: Any, **kwargs: Any) -> str:
        first_name = choice(ascii_uppercase)
        last_name = choice(ascii_uppercase)
        for _ in range(randint(3, 10)):
            first_name += choice(
                markov_chains.first_names_tokens[first_name[-1]]
            )
        for _ in range(randint(3, 15)):
            last_name += choice(
                markov_chains.last_names_tokens[last_name[-1]]
            )

        return f'{first_name} {last_name}'
