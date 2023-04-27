from dataclasses import dataclass
from datetime import date


@dataclass
class AuthorDTO:
    first_name: str
    last_name: str
    birth_date: date
    death_date: date
    information: str
