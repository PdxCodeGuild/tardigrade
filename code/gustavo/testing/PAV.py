from cmath import sin


data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]
sing_ls = []
peak_ls = []
vall_ls = []
index_ls = [len(data)]

def peaks(data):
    for num in range(len(data)-1):
        back_number = data[num-1]
        central_number = data[num] 
        forward_number = data[num+1]
        if back_number < central_number > forward_number:
            peak_ls.append(central_number)
    return central_number
print(peaks(data))

def valleys(data):
    for num in range(len(data)-1):
        back_number = data[num-1]
        central_number = data[num] 
        forward_number = data[num+1]
        if back_number > central_number < forward_number:
            vall_ls.append(central_number) 
    return central_number
print(valleys(data))

sing_ls.append(peak_ls[0])
sing_ls.append(vall_ls[0])
sing_ls.append(peak_ls[1])
sing_ls.append(vall_ls[1])
print(sing_ls)
