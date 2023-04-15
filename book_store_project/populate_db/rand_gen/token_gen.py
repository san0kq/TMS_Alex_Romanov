from typing import TypeVar, Type, Optional

from .providers import RandFirstName, RandLastName, RandEmail, RandWord

Providers = TypeVar(
    'Providers',
    RandFirstName,
    RandLastName,
    RandEmail,
    RandWord,
)


class RandGen:
    def __init__(self, provider: Type[Providers]) -> None:
        if not isinstance(provider, (
                type(RandFirstName),
                type(RandLastName),
                type(RandEmail),
                type(RandWord)
        )):
            raise ValueError('Provider should only be a class'
                             ' (RandFirstName, RandLastName, RandEmail,'
                             ' RandWord)')
        self.provider: Providers = provider()

    def generate(self, lenght: Optional[int] = None) -> str:
        if lenght or lenght == 0:
            return self.provider.generate(lenght=lenght)
        return self.provider.generate()
