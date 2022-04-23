'''
Version 1

'''
##################################################################################################################################
'''
file_1 = {
    'foot':1,
    'meter':0.3048
}

number_of_feet= input('What is the distance in feet? : ')

converted_to_meters = int(number_of_feet) * file_1['meter']

print(f"{number_of_feet} feet is equal to {converted_to_meters} meters.")
'''
##################################################################################################################################

'''
Version 2

'''
##################################################################################################################################
'''
file_2 = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm' : 1,
    'km': 1000
}

distance = input('What is the distance? : ')
unit = input('What is the unit? : ')

converted_to_meters = int(distance) * file_2[unit]

print(f"{distance} {unit} is equal to {converted_to_meters} meters.")
'''
##################################################################################################################################

'''
Version 3

'''
##################################################################################################################################
'''
file_2 = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm' : 1,
    'km': 1000
}

new_data = {
    'yd': 0.9144,
    'in': 0.254
}
file_2.update(new_data)

distance = input('What is the distance? : ')
unit = input('What is the unit? : ')

converted_to_meters = int(distance) * file_2[unit]

print(f"{distance} {unit} is equal to {converted_to_meters} meters.")

'''

'''
Version 4

'''

file_2 = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm' : 1,
    'km': 1000
}

new_data = {
    'yd': 0.9144,
    'in': 0.254
}
file_2.update(new_data)

distance = input('What is the distance? : ')
in_unit = input('What is the current unit? : ')
out_unit = input('What would you like it converted to?: ')

converted_to_meters = int(distance) * file_2[in_unit]
converted_to_output = converted_to_meters / file_2[out_unit]

print(f"{distance} {in_unit} is equal to {converted_to_output} {out_unit}.")