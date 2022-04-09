my_list = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
     new_list = []
     for x in range(1,len(data)-1):
         if data[x+1]<data[x]>data[x-1]:
             new_list.append(x)
     return new_list

print(peaks(my_list))

def valleys(data):
     updated_list = []
     for x in range(1,len(data)-1):
         if data[x+1]>data[x]<data[x-1]:
             updated_list.append(x)
     return updated_list

print(valleys(my_list))

def peaks_and_valleys(data):
     list_one = peaks(data)
     list_two = valleys(data)
     list_three = list_one+list_two
     list_three.sort()
     return list_three
print(peaks_and_valleys(my_list))   