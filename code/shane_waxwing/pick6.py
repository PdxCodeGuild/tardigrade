
# import random

# def pick6():
#     nums = []
#     while len(nums) < 6:
#         nums.append(random.randint(1, 99))
#     return nums
   
# def num_matches(l1, l2):
#     matches = 0
    
#     for index in range(len(l1)):
#         if l1[index] == l2[index]:
#             matches += 1
#     return matches
# #-------------------------------------------------------#





# winning_nums = pick6()
# balance = 0
# counter = 0

# while counter < 100000:
#     balance = balance - 2
#     ticket = pick6()
#     matches = num_matches(ticket, winning_nums)

#     if matches == 1:
#         balance = balance + 4
#     elif matches == 2:
#         balance = balance + 7
#     elif matches == 3:
#         balance == balance + 100
#     elif matches == 4:
#         balance = balance + 50000
#     elif matches == 5:
#         balance = balance + 1000000
#     elif matches == 6:
#         balance = balance + 25000000
#     counter = counter + 1

# print(balance)



import random

def pick6():
    nums = []
    while len(nums) < 6:
        nums.append(random.randint(1, 99))
    return nums
   
def num_matches(l1, l2):
    matches = 0
    
    for index in range(len(l1)):
        if l1[index] == l2[index]:
            matches += 1
    return matches
#-------------------------------------------------------#

winning_nums = pick6()
balance = 0
counter = 0

earnings = 0
expences = 0

while counter < 100000:
    balance -= 2
    expences += 2
    ticket = pick6()
    matches = num_matches(ticket, winning_nums)
    roi = (earnings - expences) / expences



    if matches == 1:
        balance += 4
        earnings += 4
    elif matches == 2:
        balance += 7
        earnings += 7
    elif matches == 3:
        balance += 100
        earnings += 100
    elif matches == 4:
        balance += 50000
        earnings += 50000
    elif matches == 5:
        balance += 1000000
        earnings += 1000000
    elif matches == 6:
        balance += 25000000
        earnings += 25000000
    counter += 1

print(f"Your balance is {balance}")
print(f"ROI: {roi}")



# ...whew