distance_in_meters = {"ft": 0.3048,
                      "mi": 1609.34,
                      "m": 1,
                      "km": 1000,
                      "yd": 0.9144,
                      "in": 0.0254}

input_distance = input("Please enter distance to be converted: ")

input_unit = input("Please enter the unit of measurement (ft/mi/m/km/yd/in): ")

distance_meters = int(input_distance) * distance_in_meters[input_unit]

print(f"{input_distance} {input_unit} is {distance_meters}m.")
