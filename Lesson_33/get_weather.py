import requests
from prettytable import PrettyTable
from decouple import config


weather_table = PrettyTable()
weather_table.field_names = ['city', 'temp', 'description', 'humidity']


APPID = config('APPID')
intro = ('Enter the name of the city. If you have finished '
         'entering or want to exit the program, enter "stop".')

print(intro)

while True:
    city_name = input('Enter: ')
    if city_name == 'stop':
        break

    params = {
        'q': city_name,
        'appid': APPID,
        'units': 'metric'
    }
    try:
        r = requests.get('https://api.openweathermap.org/data/2.5/weather', 
                        params=params)
        if r.status_code != 200:
            print('You have entered a nonexistent city or made some mistake. '
                  'Please try again.')
            continue
        r = r.json()
        weather_table.add_row([
            r['name'],
            r['main']['temp'],
            r['weather'][0]['description'],
            r['main']['humidity']
        ])
    except Exception:
        print('Connection error.')
        continue

print(weather_table)
