# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks(data):
    peaks_list = []
    for item in range(len(data)-1):
        before = data[item - 1]
        middle = data[item]
        after = data[item + 1]
        # print(before , middle , after)
        if before < middle and after < middle:
            peaks_list.append(item)
    return peaks_list



def valleys(data):
    valley_list = []
    for item in range(1,len(data)-1):
        before = data[item - 1]
        middle = data[item]
        after = data[item + 1]
        # print(before , middle , after)
        if before > middle and after > middle:
            valley_list.append(item)
    # print(valley_list)
    return valley_list


def peaks_and_valleys():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    peak = peaks(data)
    valley = valleys(data)
    print(f'The indecies for the peaks are {peak}\nThe indecies for the valleys are {valley}')
    x=0
    for item in data:            
        print(x,'x' * item)
        x +=1
        
    

peaks_and_valleys()
