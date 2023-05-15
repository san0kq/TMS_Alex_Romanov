from dataclasses import dataclass


@dataclass
class AdressDTO:
    country: str
    city: str
    street: str
    house_number: int
    postcode: int
    user_id: int
