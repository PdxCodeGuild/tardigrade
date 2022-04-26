from re import L
import requests
API_key = '35b725d260988e4245ae3e67ec6b8f3d'

user_zip = input('What is your zip code?\n')
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={user_zip}&appid={API_key}&units=imperial")

data = response.json() 

# def temp(data):
#     for item in data[]

# print(data['main']['temp'])
# print(data['name'])

user_return = f"""
Your location is {data['name']}
{data['name']}'s temp: {data['main']['temp']} in F
                        """
print(user_return)