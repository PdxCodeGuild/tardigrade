import requests
import json

response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=32.7&lon=117.6&appid=884cfd64f3a52a3354c76c381207cf1e")

# print(response.url)
# print(response.status_code)
# print(response.json())
data = response.json()

# print(data)

print("Choices: temperature, coordinates, cloud")
user_input = input("Would you like to the view San Diego's temperature, coordinates or cloud cover?: ").lower()
if user_input == 'temperature':
    temp = data['main']['temp']
    temp = (temp-273.15)*9/5+32
    print(f"The temperature is {temp}f")
elif user_input == 'coordinates':
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    print(f"San Diego's coordinates are {latitude}N and {longitude}W")
elif user_input == 'cloud':
    cloud = data['weather']
    cloud = cloud[0]['description']
    print(f"San Diego's cloud cover is {cloud}")
else:
    print('Invalid Entry. Please try again')