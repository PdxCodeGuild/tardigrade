unit_conversation_2meter={
    'feet': .3048,
    'mile' : 1609.34,
    'm' : 1, 
    'km': 1000,
    'yard': .9144, 
    'inch': .0254
}

distance= input('what is the distance: ')
unit= input("what are the units.'feet, mile, m, km, yard, inch': ")

distance= int(distance)

user_measurement= unit_conversation_2meter[unit]

total= distance * user_measurement

print (f' {distance} {unit} is equal to {total} m')