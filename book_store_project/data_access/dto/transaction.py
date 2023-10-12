from dataclasses import dataclass


@dataclass
class TransactionDTO:
    basket_id: int
    card_id: int
    price: float
    adress_id: int
