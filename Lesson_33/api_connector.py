import requests
from decouple import config

from dto import WeatherDTO


class WeatherAPIConnector:
    def __init__(self) -> None:
        self._APPID = config('APPID')
        self._session = requests.Session()
        self._session.params.update({
            'appid': self._APPID,
            'units': 'metric'
        })

    def get(self, param: str) -> WeatherDTO:
        request = self._session.get(
            'https://api.openweathermap.org/data/2.5/weather',
            params={'q': param}
        )
        data = request.json()

        return WeatherDTO(
            city=data['name'],
            temp=data['main']['temp'],
            desctription=data['weather'][0]['description'],
            humidity=data['main']['humidity']
        )
