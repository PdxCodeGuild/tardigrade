# import random


    
# def pick6():
#     winning_numbers = []

#     while len(winning_numbers) != 6:
#         x = random.choice(range(0,100))
#         winning_numbers.append(x)
#     return winning_numbers

# winning = pick6()
# ticket = pick6()
# print(winning)
# print(ticket)


# def nums_matches():

#     matching_number = []
#     a = 0
#     for winning[a] in winning:
#         if winning[a] == ticket[a]:
#             matching_number.append(winning[a])
#             a+=1
#         else:
#             a+=1
#     return matching_number

# matched_number = nums_matches()
# print(matched_number)
    
# def ammount_won():   
#     zebra = 0
#     total = 0
    
#     length = len(matched_number)
#     if length == 6:
#         zebra = 25000000
#     elif length == 5:
#         zebra = 1000000
#     elif length == 4:
#         zebra = 50000
#     elif length == 3:
#         zebra = 100
#     elif length == 2:
#         zebra = 7
#     elif length == 1:
#         zebra = 4
#     else: 
#         zebra = 0
#     total = -2 + zebra
#     return total

# total_won = ammount_won()



# def final_balance():
#     looped_total = []
#     while len(looped_total) != 10:
        
#         looped_total.append(total_won)
#     return(sum(looped_total))


# print(final_balance())


import random

def final_balance():
    looped_total = []
    while len(looped_total) != 100000:
        def pick6():
            winning_numbers = []

            while len(winning_numbers) != 6:
                x = random.choice(range(1,99))
                winning_numbers.append(x)
            return winning_numbers

        winning = pick6()
        ticket = pick6()

        def nums_matches():

            matching_number = []
            a = 0
            for winning[a] in winning:
                if winning[a] == ticket[a]:
                    matching_number.append(winning[a])
                    a+=1
                else:
                    a+=1
            return matching_number

        matched_number = nums_matches()
            
        def ammount_won():   
            zebra = 0
            total = 0
            
            length = len(matched_number)
            if length == 0:
                zebra = 0
            elif length == 1:
                zebra = 4
            elif length == 2:
                zebra = 7
            elif length == 3:
                zebra = 100
            elif length == 4:
                zebra = 50000
            elif length == 5:
                zebra = 1000000
            else: 
                zebra = 25000000
            total = -2 + zebra
            return total

        total_won = ammount_won()


        
        looped_total.append(total_won)
    return(sum(looped_total))


total_won_loss = (final_balance())
    

#ROI

R_O_I = total_won_loss/200000  
print(f"Total earings is {total_won_loss} and the ROI is {R_O_I}") 

