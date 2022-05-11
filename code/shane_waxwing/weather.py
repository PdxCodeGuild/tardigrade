import requests

city = input("Enter a city: ")
c_response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid=0e9058793eaded984375570b053e1006")
c_data = c_response.json()
latitude = c_data[2]['lat']
longitude = c_data[2]['lon']

w_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=0e9058793eaded984375570b053e1006")
w_data = w_response.json()
weather = w_data['weather'][0]['description']

ktemp = w_data['main']['temp']
ftemp = (ktemp - 273.15) * 9/5 + 32 




print(f"{city} Latitude: {latitude} Longitude: {longitude} ")
print(weather.title())
print(ftemp)

