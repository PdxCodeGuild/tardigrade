units = {
    'feet': 0.3048,
    'miles': 1609.34,
    'meters': 1,
    'kilometers': 1000, 
    'inches': .0254,
    'yards': .9144
}

user_input1 = input('Enter a unit of measurement: feet, miles, meters, kilometers, inches, yards:   ')
user_input2 = input('Enter a number to be converted: ')
user_input3 = input('Enter a unit of measurment to convert too: ')


result = int(user_input2) * units[user_input1]

print(result)