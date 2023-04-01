import json
from typing import Generator, Optional, Any, TypeVar

from .errors import ProductExistsError

GeneratorTypes = TypeVar('GeneratorTypes', tuple[str, dict[str, Any]], Any)


def db_provider(data_name: str, data_type: str) -> 'JSONDatabase':
    return JSONDatabase(data_name=data_name, data_type=data_type)


class Database:
    def __init__(self, data_name: str, data_type: str) -> None:
        self.data_name = data_name
        self.data_type = data_type
        self.database = data_name + data_type

    def read(self) -> Generator[GeneratorTypes, None, None]:
        with open(self.database) as file:
            if self.data_name == 'data/products':
                for product_id, params in json.load(file)['Goods'].items():
                    yield product_id, params
            else:
                for record in json.load(file):
                    yield record

    def read_all(self) -> dict[str, Any]:
        with open(self.database) as file:
            return dict(json.load(file))


class JSONDatabase(Database):
    def create(self, record: dict[str, Any]) -> None:
        json_data = self.read_all()
        if self.data_name == 'data/products':
            if len(json_data['Goods']) == 0:
                record_id = '0'
            else:
                record_id = str(int(list(json_data['Goods'].keys())[-1]) + 1)
            json_data['Goods'][record_id] = record

        elif self.data_name == 'data/orders':
            if len(json_data) == 0:
                record_id = '0'
            else:
                record_id = str(int(list(json_data.keys())[-1]) + 1)
            json_data[record_id] = record
        else:
            json_data.update(record)

        with open(self.database, 'w') as file:
            json.dump(json_data, file, indent=2)

    def id_exists_to_update(self, record: dict[str, Any]) -> Optional[str]:
        for product_id, product in self.read_all()['Goods'].items():
            for key, value in record.items():
                if key in ('quantity', 'created_at', 'updated_at'):
                    continue
                elif value != product[key]:
                    break
            else:
                return str(product_id)
        return None

    def update(self, product_id: str, record: dict[str, Any]) -> None:
        json_data = self.read_all()
        json_data['Goods'][product_id]['quantity'] = record['quantity']
        json_data['Goods'][product_id]['updated_at'] = record['updated_at']
        with open(self.database, 'w') as file:
            json.dump(json_data, file, indent=2)

    def delete(self, product_id: str) -> None:
        json_data = self.read_all()
        json_data['Goods'].pop(product_id)
        with open(self.database, 'w') as file:
            json.dump(json_data, file, indent=2)

    def validate_product_exists(self, product_id: str) -> None:
        json_data = self.read_all()
        if product_id not in json_data['Goods']:
            raise ProductExistsError(f'The product with ID {product_id} does '
                                     f'not exist.')
