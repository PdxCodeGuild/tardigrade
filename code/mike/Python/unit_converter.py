###### Version 1

unit_dict = {
    'feet': 0.3048,
    'meter': 1
}

    
distance = input("\nWhat is the distance in feet?: ")

distance = int(distance)

unit = unit_dict['feet']


total = distance * unit

print(total)

###### Version 2

unit_dict = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
}

    
distance = input("\nWhat is the distance?: ")

distance = int(distance)

unit = input("\nWhich unit of measure?: ")

unit_value = unit_dict[unit]

total = distance * unit_value


print(f'{distance} {unit} is {(total)}m')