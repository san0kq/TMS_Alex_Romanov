from dataclasses import dataclass


@dataclass
class ProfileDTO:
    first_name: str
    last_name: str
    age: int
    email: str
    phone: str


@dataclass
class BasketDTO:
    status: str


@dataclass
class BankCardDTO:
    number: int
    first_name: str
    last_name: str
    cvc: int
    period: str


@dataclass
class UserDTO:
    username: str
    password: str
    profile: ProfileDTO
    basket: BasketDTO
    bank_card: BankCardDTO
