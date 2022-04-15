import requests


usr_pick = input('Would you like to know the past (type p) or the future (type f)? ')
if usr_pick == 'f':
    response = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=32.7157&lon=-117.1610&units=imperial&appid=884cfd64f3a52a3354c76c381207cf1e')
else:
    response = requests.get('https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=32.7157&lon=117.1610&units=imperial&dt=1649585130&appid=884cfd64f3a52a3354c76c381207cf1e')
    print(response)
data = response.json()
print('Far  UV H')
print(data["hourly"][2]['temp'], data["hourly"][2]['uvi'], data["hourly"][2]['humidity'])

# ['"1649584800"']['"temp", "feels_like", "humidity", "uvi"']