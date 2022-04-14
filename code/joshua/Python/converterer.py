
def distance_converter():
    unit = {'ft': 0.3048, 'mi': 1609.34, 'km': 1000, 'm': 1}
    unit_output = {'ft': 0.3048, 'mi': 1609.34, 'km': 1000, 'm': 1}
    thing = True
    thing2 = True
    
    
    while True:
        dist = input('What is the distance?\n')
        if dist.isdigit():
            dist = int(dist)
            break
        # elif float(dist) == True:
        #     dist = float(dist)
        #     break
        else:
            print(f'This is not a valid input:{dist}\n')
        
    while thing == True:
        user_unit = input('What are the input units?\n')
        for key, values  in unit.items():
            if key == user_unit:
                user_value = values
                thing = False
                break
            else:
                continue

    # while True:
    #     user_unit = input('What are the input units?\n')
    #     for key, values  in unit.items():
    #         if key == user_unit:
    #             user_value = values
    #             break
    #         else:
    #             continue
    #     break
   
    while thing2 == True:
        other_unit = input('What are the output units?\n')
        for key1, values2  in unit_output.items():
            if key1 == other_unit:
                other_value = values2
                thing2 = False
                break
            else:
                continue


    for a, b in unit.items():
        if a == 'm':
            meter = b
    
    
    meter = (dist * user_value * meter)
    final_value = meter / other_value
    print(f'{dist} {user_unit} is {final_value} {other_unit}')
        
        

                
    
    # for a, b in unit.items():
    #     print(f'{(a * dist)} ft is {(b * dist)} m')
    













distance_converter()