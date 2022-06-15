import requests


response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Ashland&appid=884cfd64f3a52a3354c76c381207cf1e")


data = response.json()
# print(data)





#### get lat long
####  add those variables to the string 
#### output just certain data maybe three properties
#### since the readouts are in Kelvin I'm going to define a function using (K − 273.15) × 9/5 + 32 = °F to convert. 
#### K in the case above would the number (perameter) im running through the function

print("Welcome to Ashland Oregon!!!")
user_input = input('Would you like to know the weather forecast for here today? (yes/no): ')

def kelvin_to_fahrenheit(num):
    fahrenheit = (num - 273.15) * (9/5) + 32
    return fahrenheit


humidity = data['main']['humidity']  ### this grabs info from the list I named "data" at the index positions of main and humidity
maximum = data['main']['temp_max']  ### and so on
minimum = data['main']['temp_min']    ### and so on



con_max = int(kelvin_to_fahrenheit(maximum))   ### this calls the function of the formuala i looked up to convert kelvin to fahrenheit
con_min = int(kelvin_to_fahrenheit(minimum))   ### and so on

if user_input == "yes":
    print(f"""Today in Ashland the humidity is {humidity}%, the high temp will be {con_max} fahrenheit and the low will 
    be {con_min} fahrenheit.""")


