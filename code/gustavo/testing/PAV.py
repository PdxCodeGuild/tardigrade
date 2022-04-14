data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]


# def peaks(data):
# for num in range(len(data)-1):
#     back_number = data[num-1]
#     central_number = data[num] 
#     forward_number = data[num+1]
#     if back_number < central_number > forward_number:
#         print(central_number)
        # return central_number
# print(peaks(data))

def peaks(data):
    for num in range(len(data)-1):
        back_number = data[num-1]
        central_number = data[num] 
        forward_number = data[num+1]
        if back_number > central_number < forward_number:
            print(central_number) 
    return central_number
print(peaks(data))
