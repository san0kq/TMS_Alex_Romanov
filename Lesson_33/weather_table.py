from __future__ import annotations
from prettytable import PrettyTable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dto import WeatherDTO


class WeatherTable:
    def __init__(self) -> None:
        self._weather_table = PrettyTable()
        self._set_columns()

    def _set_columns(self) -> None:
        self._weather_table.field_names = ['city', 'temp', 'description', 
                                           'humidity']
    
    def add_row(self, data: WeatherDTO) -> None:
        self._weather_table.add_row([data.city, data.temp,
                                     data.desctription, data.humidity])

    def table_read(self) -> None:
        print(self._weather_table)
