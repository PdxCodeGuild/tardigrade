units = {
    'ft'    : 0.3048,
    'm'     : 1,
    'mi'    : 1609.34,
    'km'    : 1000,
}
usr_meas = int(input('Please enter the distance you wish to convert: '))
usr_unit = input('Please enter the unit of measurement you wish to convert from (ft, m, mi or km): ')
print(f"That is equal to: {units[usr_unit] * usr_meas} meters")

