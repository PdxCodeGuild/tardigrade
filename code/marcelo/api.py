import requests

city= input('choose a city to get a weather report: ')
city= city.lower()

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=884cfd64f3a52a3354c76c381207cf1e")    
data = response.json() 

print (f" the weather: {data ['weather'][0]['description'] } \n tempature: {data ['main']['temp']} \n and the wind speed: {data ['wind']['speed']}" )
