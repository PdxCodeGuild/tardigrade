# Version One

meters = {'m': 0.3048}

distance_input = int(input("What is the distance in feet?: "))
distance = meters.get('m')
total = distance*distance_input
print(f"{distance_input}ft is {total}m")

# Version Two

my_dict = {"ft": .3048, "mi": 1609.34, "m": 1, "km": 1000}

distance_input = int(input("What is the distance?: "))
unit_input = input("What are the units? (ft, mi, m, km): ")
units = my_dict.get(unit_input)
total = units*distance_input
print(f"{distance_input}{unit_input} is {total}m")

# Version Three

my_dict = {"ft": .3048, "mi": 1609.34, "m": 1, "km": 1000, "yd": .9144, "in": .0254}

distance_input = int(input("What is the distance?: "))
unit_input = input("What are the units? (ft, mi, m, km, yd, in): ")
units = my_dict.get(unit_input)
total = units*distance_input
print(f"{distance_input}{unit_input} is {total}m")

# Version Four

my_dict = {"ft": .3048, "mi": 1609.34, "m": 1, "km": 1000, "yd": .9144, "in": .0254}

distance_input = int(input("What is the distance?: "))
unit_input = input("What are the units? (ft, mi, m, km, yd, in): ")
output_input = input("What are the output units? (ft, mi, m, km, yd, in): ")
units = my_dict.get(unit_input)
out_units = my_dict.get(output_input)
total = units*distance_input/out_units
print(f"{distance_input}{unit_input} is {total}{output_input}")