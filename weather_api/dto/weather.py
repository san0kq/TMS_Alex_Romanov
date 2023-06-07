from dataclasses import dataclass


@dataclass
class WeatherDTO:
    city: str
    temp: float
    desctription: str
    humidity: int
