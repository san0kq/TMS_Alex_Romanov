from typing import Optional

from .tokens import words_tokens
from .rand_base import AbstractBase


class RandWord(AbstractBase):
    def __init__(self) -> None:
        self._tokens = words_tokens.tokens

    def generate(self, length: Optional[int]) -> str:
        return self._result(length=length)
