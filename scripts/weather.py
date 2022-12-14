import requests
import os

API_KEY = os.environ['WEATHER_API_KEY']

city = input('Enter the city: ')
base_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + API_KEY

weather_data = requests.get(base_url).json()

print(weather_data)