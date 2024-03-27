#pip install requests
import requests
import json

API_KEY = ""
city_name = input('City name: ')
URL = f"http://maps.openweathermap.org/maps/2.0/weather/?appid={API_KEY}&units=metric"

res = requests.get(URL)
json_date = json.loads(res.text)
weather = json_date["weather"][0]["description"]
temprature = json_date["main"]["temp"]
humidity = json_date["main"]["humidity"]
wind_speed = json_date["wind"]["speed"]

print(f"Weather:{weather}")
print(f"Temprature:{temprature}")
print(f"Humidity:{humidity}")
print(f"Wind Speed:{wind_speed}")
