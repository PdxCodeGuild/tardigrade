unit_conversation_meter={
    '1_ft': .3048
}

user = input(' what is the distance in feet: ')
user= int(user)

total= user * unit_conversation_meter['1_ft']

print (f' {user} ft is equal to {total} m')