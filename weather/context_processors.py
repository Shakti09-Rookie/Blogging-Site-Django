import requests
import os

def we(request):
    API_KEY = os.environ.get("wapi_key")
    city = "New Delhi"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    url = f"{BASE_URL}?appid={API_KEY}&q={city}"

    r = requests.get(url).json()
    weather_data =[]
    city_weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
    # weather_data.append(city_weather)
    print(city_weather)
    return {'weather_data' : city_weather}