## Eberhardt

## https://github.com/PdxCodeGuild/hydra/blob/master/1%20Python/labs/12%20Unit%20Converter.md

## VERSION 1 - COMPLETE

## Ask the user for the number of feet, and print out the equivalent distance in meters. 
## Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input 
# distance by 0.3048. Below is some sample input/output.

## > what is the distance in feet? 12
## > 12 ft is 3.6576 m

meters_per_foot = (0.3048) 

dist_in_feet = int(input("\nUNIT CONVERTER - V.1\n\nWhat is the distance in feet? "))
print(f"{dist_in_feet} feet is {meters_per_foot * dist_in_feet} meter(s).\n")

# # ## VERSION 2 - COMPLETE

# ## Allow the user to also enter the units. Then depending on the units, 
# ## convert the distance into meters. The units we'll allow are feet, miles, 
# ## meters, and kilometers.

# ## 1 ft is 0.3048 m
# ## 1 mi is 1609.34 m
# ## 1 m is 1 m
# ## 1 km is 1000 m
# ## Below is some sample input/output:

# ## > what is the distance? 100
# ## > what are the units? mi
# ## > 100 mi is 160934 m

conversions = {'ft': 0.3048, 'mi': 1609.34, 'm': 1, 'km': 1000}

distance = int(input("\nUnit Converter V.2\n\nWhat is the distance? "))
unit = input("Are the units ft, mi, m, or km? ")

for key in conversions.keys():
    if key == unit:
        calculation = conversions[key] * distance
        # print("calculation", calculation) ## TEST STATEMENT
        print(f"\n{distance} {unit} is {calculation} meter(s).")

# Version 3 - COMPLETE
# Add support for yards, and inches.

# 1 yard is 0.9144 m
# 1 inch is 0.0254 m

# > 100 mi is 160934 m

conversions = {'ft': 0.3048, 'mi': 1609.34, 'm': 1, 'km': 1000, 'yard': 0.9144, 'inch': 0.0254}

distance = int(input("\nUnit Converter V.3\n\nWhat is the distance? "))
unit = input("Choose a unit > ft, mi, m, km, yard, or inch: ")

for key in conversions.keys():
    if key == unit:
        calculation = conversions[key] * distance
        # print("calculation", calculation) ## TEST STATEMENT
        print(f"\n{distance} {unit} is {calculation} meter(s).")

## Version 4 - COMPLETE
## Now we'll ask the user for the distance, the starting units, and the units to convert to.

conversions = {'ft': 0.3048, 'mi': 1609.34, 'm': 1, 'km': 1000, 'yard': 0.9144, 'inch': 0.0254}

distance = int(input("\nUnit Converter V.4\n\nWhat is the distance? "))
unit_input = input("What are the input units? > ft, mi, m, km, yard, or inch: ")
unit_output = input("What are the output units? > ft, mi, m, km, yard, or inch: ")
calculation_list = []

for key in conversions.keys():
    if key == unit_input:
        calculation = conversions[key] * distance
        calculation_list.append(calculation)

for key in conversions.keys():
    if key == unit_output:
        calculation2 = calculation_list[0] / conversions[key]

print(f"\n{distance} {unit_input}(s) is {calculation2} {unit_output}(s) meter(s).")