units = {
    'feet': 0.3048,
    'miles': 1609.34,
    'meters': 1,
    'kilometers': 1000, 
    'inches': .0254,
    'yards': .9144
}


user_input = input('Enter a number to be converted to meters: ')
user_input2 = input('Enter a unit of measurement: feet, miles, meters, kilometers, inches, yards:   ')

user_input = int(user_input) * units[user_input2]

print(user_input)