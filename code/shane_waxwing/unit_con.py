
#------------Version 1--------------#

'''
meter = 0.3048
feet = int(input("Enter a number of feet: "))
conversion = meter * feet

print(f"{feet} feet is {conversion} meters.")
'''

#-----------------Version 2-------------------#
'''
metrics = {
    "ft" : 0.3048,
    "mi" : 1609.34,
    "m" : 1,
    "km" : 1000
}

unit = input("Please enter a unit to be converted to meters (ft, mi, m, km): ")
distance = int(input("What is the distance? "))

if unit == "ft":
    con = metrics["ft"] * distance
elif unit == "mi":
    con = metrics["mi"] * distance
elif unit == "m":
    con = metrics["m"] * distance
elif unit == "km":
    con = metrics["km"] * distance


print(f"{distance} {unit} is {con} meters.")

#-----------------------------------------------#
'''

#-----------------Verson 3----------------------#

'''
metrics = {
    "ft" : 0.3048,
    "mi" : 1609.34,
    "m" : 1,
    "km" : 1000,
    "yd" : 0.9144,
    "in" : 0.0254
}

unit = input("Please enter a unit to be converted to meters (ft, mi, m, km): ")
distance = int(input("What is the distance? "))

if unit == "ft":
    con = metrics["ft"] * distance
elif unit == "mi":
    con = metrics["mi"] * distance
elif unit == "m":
    con = metrics["m"] * distance
elif unit == "km":
    con = metrics["km"] * distance
elif unit == "yd":
    con = metrics["yd"] * distance
elif unit == "in":
    con = metrics["in"] * distance


print(f"{distance} {unit} is {con} meters.")
'''

#-------------------Version 4 ----------------------#

metrics = {
    "ft" : 0.3048,
    "mi" : 1609.34,
    "m" : 1,
    "km" : 1000,
    "yd" : 0.9144,
    "in" : 0.0254
}

UI = input("What units are we converting from? ft, mi, km, yd, in: ")
num = int(input(f"How many {UI}?"))
UO = input("What are we converting to? ")

meters = num * metrics[UI]
output = meters / metrics[UO]
print(output)
