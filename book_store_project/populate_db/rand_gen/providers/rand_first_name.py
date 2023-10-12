from typing import Optional

from .tokens import names_tokens
from .rand_base import AbstractBase


class RandFirstName(AbstractBase):
    def __init__(self) -> None:
        self._tokens = names_tokens.tokens

    def generate(self, length: Optional[int]) -> str:
        return self._result(length=length)
