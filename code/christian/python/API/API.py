## Eberhardt

## Assignment:

## Goal: Write a Python script that asks the user for the weather and prints out data. 
## You can print the current weather conditions, wind speed, etc. It’s up to you how much 
## output from the API you want to display.

## Version 2: To challenge yourself, use two different endpoints (your choice). 
## Ask the user if they want to quickly check the weather for a city, or get a 7 days forecast. 
## You could potentially add a while loop and break out of it if the user wants to stop.
 
## API KEY: 884cfd64f3a52a3354c76c381207cf1e
## The list of all endpoints is in the FREE column:
## https://openweathermap.org/price

import requests

zip_code = input("\nPlease enter a zip code: ")
country_code = input("Please enter a country code, (i.e. US): ")

API_key = '884cfd64f3a52a3354c76c381207cf1e'
response_1 = requests.get(f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={API_key}")

location_data = response_1.json()

lat = location_data['lat']
lon = location_data['lon']

response_2 = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}")
weather_data = response_2.json()

response_3 = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=hourly&appid={API_key}")
daily_weather_data = response_3.json()

current_weather = f'''
Here is the current weather for {location_data['name']}!

  Clouds: {weather_data['weather'][0]['description'].title()}
    Temp: {weather_data['main']['temp']}
Max Temp: {weather_data['main']['temp_max']}
'''

daily_weather_report = f'''
Here is the 7-day forecast for {location_data['name']}!

Day 1: {daily_weather_data['daily'][0]['temp']['day']}
Day 2: {daily_weather_data['daily'][1]['temp']['day']}
Day 3: {daily_weather_data['daily'][2]['temp']['day']}
Day 4: {daily_weather_data['daily'][3]['temp']['day']}
Day 5: {daily_weather_data['daily'][4]['temp']['day']}
Day 6: {daily_weather_data['daily'][5]['temp']['day']}
Day 7: {daily_weather_data['daily'][6]['temp']['day']}
'''

users_choice = input("\nPlease type your desired weather report.\n'Current' or '7 Day Forecast': ")

if users_choice.lower() == 'current':
    print(current_weather)
else:
    print(daily_weather_report)