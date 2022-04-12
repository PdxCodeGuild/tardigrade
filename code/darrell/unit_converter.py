distance_in_meters = {"ft": 0.3048,
                      "mi": 1609.34,
                      "m": 1,
                      "km": 1000}

input_distance = input("Please enter distance in feet to convert: ")

distance_meters = int(input_distance) * 0.3048

print(f"{input_distance} ft is {distance_meters}m.")
