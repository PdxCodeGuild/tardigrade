data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]
peak_list =[]
def peaks(data):
    num = 0
    test1=[]
    test2=[]
    for nums in range(len(data)):
        print(data[nums], end = '')
        print(data[nums + 1], end = '')
        # if data[i] > data[i+1] and data[i] > data[i-1]:
        #     print(data[i])
        #     num = (data[i])
        # peak_list.append(data)
        # print(peak_list)
        # num = peak_list[nums] > peak_list[nums+1] and peak_list[nums] > peak_list[nums-1]
            # return num
    return num
print(peaks(data))
        # if data[nums] > data[nums+1] and data[nums] > data[nums-1]:
        #     peak_list.append(data[nums])
        #     return peak_list
# print(peaks(data))
# for i in range(len(data)):
#     print(i, 'index')
#     print(data[i], 'item')









# def valleys(data):
