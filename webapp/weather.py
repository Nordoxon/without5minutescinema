from flask import current_app
import requests

def weather_by_city(city_name):
    weather_url = current_app.config['WEATHER_URL']
    params = {
        "appid": current_app.config['WEATHER_API_KEY'],
        "q": city_name,
        "units": "metric",
        "lang": "ru"
    }
    try:
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        weather = result.json()
        if 'main' in weather:
            try:
                return weather['main']
            except(IndexError, TypeError):
                return False
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
    return False

if __name__ == "__main__":
    w = weather_by_city("Kaluga,Russia")
    print(w)