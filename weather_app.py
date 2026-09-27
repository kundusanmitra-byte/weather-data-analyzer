import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")


def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"{city}: {temp}°C, {description}")
        return temp
    else:
        print(f"Could not fetch weather for '{city}'. Error code: {response.status_code}")
        return None


cities_input = input("Enter city names separated by commas: ")

raw_cities = cities_input.split(",")
cities = []
for city in raw_cities:
    cities.append(city.strip())


temps = {}
for city in cities:
    temp = get_weather(city, api_key)
    if temp is not None:
        temps[city] = temp


if temps:
    hottest_city = max(temps, key=temps.get)
    coldest_city = min(temps, key=temps.get)
    print(f"\nHottest city: {hottest_city} ({temps[hottest_city]}°C)")
    print(f"Coldest city: {coldest_city} ({temps[coldest_city]}°C)")
else:
    print("No valid data to compare.")
