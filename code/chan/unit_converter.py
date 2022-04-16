# Chan Saechao
# Unit Converter


# Dictionary unit converter: feet to meters / mi to m / m to m / km to m
unit_converter = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000
}

unit_converter.update({"yard": 0.9144})
unit_converter.update({"inch": 0.0254})

# Convert input to a number
distance = input(f'What is the distance? ')
distance = float(distance)

# Ask for unit being used
units = input(f'What are the units? ')
units = units.lower()

# Gets the values from unit key
conversion = unit_converter.get(units)

# Multiplys the distance with unit
converted_units = distance * conversion

# Print statement for the conversion
print(f'{distance} {units} is {converted_units} m')