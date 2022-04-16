
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid={API key}

import requests
# from datetime import datetime, timezone
# print(datetime.now())              # timezone
# print(datetime.now(timezone.utc))  # coordinated universal time 

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Portland&appid=884cfd64f3a52a3354c76c381207cf1e")

data = response.json()

print(data["weather"][0]['description'])
print(data['name'])

#  (K − 273.15) × 9/5 + 32 
# Function: Converts kelvin to fahrenheit
def kelvin_to_fahrenheit(num):
    fahrenheit = (num - 273.15) * (9/5) + 32
    return fahrenheit

# Gets temperature and convert min, max, and current temp into fahrenheit
min = data['main']['temp_min']
max = data['main']['temp_max']
temp = data['main']['temp']
converted_min = int(kelvin_to_fahrenheit(min))
converted_max = int(kelvin_to_fahrenheit(max))
converted_temp = int(kelvin_to_fahrenheit(temp))
print(converted_min)
print(converted_max)
print(converted_temp)


print('Welcome to PDX Code Guild in Portlan, Oregon')
user_choice = input("Would you like to know the weather today(yes/no)? ")
user_choice = user_choice.lower()

if user_choice == "y" or "yes":
    print(f"""Good day from {data['name']}.  Today's weather forecast is {data['weather'][0]['description']} and the current temperature is {converted_temp} degrees fahrenheit, 
    with temperature high's at {converted_max} degrees and low's at {converted_min} degrees.""")
    