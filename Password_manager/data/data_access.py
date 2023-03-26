import json
from typing import Generator, Optional

from .errors import IdentifierExistsError


def db_provider(data_name: str, data_type: str) -> Optional['PassDB']:
    if data_type == '.json':
        return PassDB(data_name=data_name, data_type=data_type)
    else:
        return None


class PassDB:
    def __init__(self, data_name: str, data_type: str) -> None:
        self.data_name = data_name
        self.data_type = data_type
        self.database = data_name + data_type

    def create(self, record: dict[str, str]) -> None:
        json_load = self.read()
        with open(self.database, 'w') as file:
            json_load.update(record)
            json.dump(json_load, file, indent=2)

    def read(self) -> dict[str, str]:
        with open(self.database) as file:
            json_load = json.load(file)

            return dict(json_load)

    def list(self) -> Generator[tuple[str, str], None, None]:
        with open(self.database) as file:
            for identifier, password in json.load(file).items():
                yield identifier, password

    def delete(self, identifier: str) -> None:
        json_load = self.read()
        with open(self.database, 'w') as file:
            json_load.pop(identifier)
            json.dump(json_load, file, indent=2)

    def identifier_exists(self, identifier: str) -> None:
        json_load = self.read()
        if identifier not in json_load.keys():
            raise IdentifierExistsError(f'"{identifier}" does not exist.')
