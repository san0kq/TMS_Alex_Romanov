from random import choice
from abc import ABC, abstractmethod
import json
import os

PACKAGE_DIRECTORY = os.path.dirname(__file__)


class AbstractBase(ABC):
    @abstractmethod
    def __init__(self, tokens_file: str) -> None:
        with open(PACKAGE_DIRECTORY + tokens_file) as file:
            self.tokens = json.load(file)

    def _first_token(self) -> str:
        return choice(list(filter(lambda x: x[0].isupper(),
                                  self.tokens.keys())))

    def generate(self, lenght: int = 7) -> str:
        if not isinstance(lenght, int) or not 0 < lenght <= 20:
            raise ValueError('Lenght should be a integer in range (1, 20).')
        random_value = self._first_token()
        while len(random_value) < lenght:
            random_token = choice(list(filter(lambda x: x[1] != ' ',
                                              self.tokens[random_value[-2:]])))
            if len(random_value) == lenght - 1 and lenght % 2 != 0:
                if any(x[1] == ' ' for x in self.tokens[random_value[-2:]]):
                    random_token = choice(list(filter(lambda x: x[1] == ' ',
                                                      self.tokens[
                                                          random_value[-2:]]
                                                      )))

            random_value += random_token
        return random_value[:lenght]


class RandFirstName(AbstractBase):
    def __init__(self) -> None:
        super().__init__(tokens_file='/tokens/names_tokens.json')


class RandLastName(AbstractBase):
    def __init__(self) -> None:
        super().__init__(tokens_file='/tokens/lastnames_tokens.json')


class RandEmail(AbstractBase):
    def __init__(self) -> None:
        super().__init__(tokens_file='/tokens/emails_tokens.json')

    def _first_token(self) -> str:
        return choice(list(self.tokens.keys()))


class RandWord(AbstractBase):
    def __init__(self) -> None:
        super().__init__(tokens_file='/tokens/words_tokens.json')
