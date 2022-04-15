import requests


# city_data = requests.get("http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid=214e3e03f90584a403aac70e81b52198")

user_choice = input("Would you like the current weather?: ")
user_city = input("Please enter a city: ")
user_state = input("Please enter a state (2-letters): ")
user_country = input("Please enter \"US\": ")

city_string = f"http://api.openweathermap.org/geo/1.0/direct?q={user_city},{user_state},{user_country}&limit=5&appid=214e3e03f90584a403aac70e81b52198"
city_data = requests.get(city_string)

city = city_data.json()
# data = response.json()
city_lat = city[0]['lat']
city_lon = city[0]['lon']
# print(city_lat)
# print(city_lon)

api_string = f"https://api.openweathermap.org/data/2.5/weather?lat={city_lat}&lon={city_lon}&appid=214e3e03f90584a403aac70e81b52198&units=imperial"

response = requests.get(api_string)

data = response.json()
# print(data)

print(
    f"Current weather for {user_city.title()}, {user_state.upper()}: Current Temp: {data['main']['temp']} F; Feels Like: {data['main']['feels_like']} F; Low: {data['main']['temp_min']} F; High: {data['main']['temp_max']} F; Pressure: {data['main']['pressure']}; Humidity: {data['main']['humidity']};")
