units = {
    'feet': 0.3048,
    'miles': 1609.34,
    'meters': 1,
    'kilometers': 1000, 
    'inches': .0254,
    'yards': .9144
}


result = input('Enter a number to be converted to meters: ')
user_input2 = input('Enter a unit of measurement: feet, miles, meters, kilometers, inches, yards:   ')

result = int(result) * units[user_input2]

print(result)