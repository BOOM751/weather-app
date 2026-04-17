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

print("Город:", city)
print("Широта:", latitude)
print("Долгота:", longitude)