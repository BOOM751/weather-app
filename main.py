import requests

city = input("Введите город: ")

url = "https://geocoding-api.open-meteo.com/v1/search"
params = {
    "name": city,
    "count": 1
}

response = requests.get(url, params=params)
data = response.json()

latitude = data["results"][0]["latitude"]
longitude = data["results"][0]["longitude"]
country = data["results"][0]["country"]

weather_url = "https://api.open-meteo.com/v1/forecast"
weather_params = {
    "latitude": latitude,
    "longitude": longitude,
    "current_weather": True
}

weather_response = requests.get(weather_url, params=weather_params)
weather_data = weather_response.json()

print("Страна:", country)
print("Широта:", latitude)
print("Долгота:", longitude)
print("Температура:", weather_data["current_weather"]["temperature"], "°C")
print("Скорость ветра:", weather_data["current_weather"]["windspeed"], "км/ч")