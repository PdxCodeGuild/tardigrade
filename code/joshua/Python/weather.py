
import requests
import json
API_key = '35b725d260988e4245ae3e67ec6b8f3d'

# user_zip = input('What is your zip code?\n')
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={11413}&appid={API_key}&units=imperial")

data = response.json()

# print(data)
# def temp(data):
#     for item in data[]

# print(data['main']['temp'])
# print(data['name'])

user_return = f"""
Your location is {data['name']}
{data['name']}'s temp: {data['main']['temp']} in F
{data['name']}'s outside condition: {data['weather'][0]['description']}
                        """
# print(user_return)
print(json.dumps(data,indent = 2))