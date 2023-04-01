from typing import Type, TypeVar, Any

from .providers import (
    EmailProvider,
    PhoneProvider,
    BankCardProvider,
    NameProvider
)

Providers = TypeVar(
    'Providers',
    EmailProvider,
    PhoneProvider,
    BankCardProvider,
    NameProvider)


class FakeFactoryIterator:
    def __init__(
            self,
            provider: Type[Providers],
            counter: int,
            count: int
    ) -> None:
        self.provider: Any = provider
        self.counter = counter
        self.count = count

    def __next__(self) -> Any:
        if self.counter == self.count:
            raise StopIteration
        self.counter += 1
        return self.provider()


class FakeFactory:
    def __init__(self, provider: Type[Providers], count: int) -> None:
        self.provider: Any = provider()
        self.count = count

    def generate(self) -> Any:
        return self.provider()

    def __iter__(self) -> FakeFactoryIterator:
        counter = 0
        return FakeFactoryIterator(self.provider, counter, self.count)
