unit_conversation_2meter={
    'feet': .3048,
    'mile' : 1609.34,
    'm' : 1, 
    'km': 1000,
    'yard': .9144, 
    'inch': .0254
}

print('you will be choosing 2 units to convert')
distance= float(input('what is the distance: '))
convert_from= input("what are the units.'feet, mile, m, km, yard, inch': ") #divide
convert_to= input("what is the 2nd unit.'feet, mile, m, km, yard, inch': ") # multi

distance= int(distance)

unit_from= distance * unit_conversation_2meter[convert_from]
print(unit_from)

unit_to= unit_from / unit_conversation_2meter[convert_to]
print(unit_to)

# user_measurement= unit_conversation_2meter[unit]
# user_measurement2= unit_conversation_2meter[unit_2]

# total= user_measurement * user_measurement2


print (f'{distance} {convert_from} is {unit_to} {convert_to}')