from api_connector import WeatherAPIConnector
from weather_table import WeatherTable


def get_weather() -> None:
    connector = WeatherAPIConnector()
    weather_table = WeatherTable()


    intro = ('Enter the name of the city. If you have finished '
            'entering or want to exit the program, enter "stop".')


    print(intro)

    while True:
        city_name = input('Enter: ')
        if city_name == 'stop':
            break

        try:
            data = connector.get(param=city_name)
            weather_table.add_row(data=data)
        except Exception:
            print('You have entered a nonexistent city or made some mistake. '
                'Please try again.')
            continue

    weather_table.table_read()
