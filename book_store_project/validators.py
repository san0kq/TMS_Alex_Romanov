from errors import UserChoiceError, EmailError, PhoneError, BookError


class ChoiceValidator:
    def __init__(self, choice: str) -> None:
        self.choice = choice

    @property
    def choice(self) -> str:
        return self._choice

    @choice.setter
    def choice(self, value: str) -> None:
        if not value.isdigit():
            raise UserChoiceError('Your choice should be an integer from '
                                  'the options provided in the menu.')
        self._choice = value

    def user_choice(self) -> None:
        if self.choice not in ('1', '2', '3', '4', '5'):
            raise UserChoiceError('Your choice should be within the range '
                                  'of 1 to 5')

    def book_choice(self) -> None:
        if self.choice not in ('1', '2', '3', '4'):
            raise UserChoiceError('Your choice should be within the range '
                                  'of 1 to 4')

    def author_choice(self) -> None:
        if self.choice not in ('1', '2'):
            raise UserChoiceError('Your choice should be within the range '
                                  'of 1 to 2')


def id_validator(value: str) -> None:
    if not value.isdigit():
        raise ValueError('ID should be a positive integer.')


def email_validator(value: str) -> None:
    email = value.split('@')
    if len(email) != 2:
        raise EmailError('Invalid email. Example: Ted1994@gmail.com')
    elif email[1] not in ('mail.ru', 'yandex.ru', 'ya.ru',
                          'gmail.com', 'rambler.ru'):
        raise EmailError('This provider is not supported. Supported providers:'
                         ' mail.ru, yandex.ru, ya.ru, gmail.com, rambler.ru')
    elif not 1 <= len(email[0]) <= 64:
        raise EmailError('The length of your email should be between 1 and 64 '
                         'characters.')


def phone_validator(value: str) -> None:
    phone = value.replace('+', '', 1)
    if not phone.isdigit():
        raise PhoneError('Invalid phone number. Example: +375336272837, '
                         '80212652632')
    elif not 10 <= len(phone) <= 12:
        raise PhoneError('Invalid phone number. The length of the number '
                         'should be between 10 and 12.')


def book_name_validator(value: str) -> None:
    if not 1 <= len(value) <= 256:
        raise BookError('The length of the book title should be between 1 and '
                        '256 characters.')
