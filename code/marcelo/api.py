import requests

# #getting an input from the user. and use that input in the API call
# city= input('choose a city to get a weather report: ') 
# city= city.lower()

# # https api call. using the user input
# response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=884cfd64f3a52a3354c76c381207cf1e")    
# data = response.json() # allows use to have a readable human format

# #printing weather data. but grabbing object and keys
# print (f" the weather: {data ['weather'][0]['description'] } \n tempature: {data ['main']['temp']} \n and the wind speed: {data ['wind']['speed']}" )

# response_2 = ("http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=60.99&lon=30.9&dt=1586468027&appid=884cfd64f3a52a3354c76c381207cf1e")
# data_2 = response_2.json()

while True:
    user_response= input('do you want an hourly or the current forcast of any city?. choose \'hourly\' or \'city\'. or \'stop\' to exit: ')
    user_response= user_response.lower()
    
    if user_response == 'city':
        city= input(f'choose a city to get a weather report: ') 
        city= city.lower()
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=884cfd64f3a52a3354c76c381207cf1e")    
        data = response.json()
        print (f" the weather: {data ['weather'][0]['description'] } \n tempature: {data ['main']['temp']} \n and the wind speed: {data ['wind']['speed']}")
    if user_response == 'hourly':
        city= input(f'choose a city to get a weather report: ') 
        city= city.lower()
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&exclude=hourly,daily&appid=884cfd64f3a52a3354c76c381207cf1e")    
        data = response.json()
        print(f"\n it feels like: {data}")
    if user_response=='stop':
        break
    # else:
    #     print (f" the weather: {data ['weather'][0]['description'] } \n tempature: {data ['main']['temp']} \n and the wind speed: {data ['wind']['speed']}")