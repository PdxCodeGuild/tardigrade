

#                                                   X                 X
#                                                X  X  X           X  X
#                           X                 X  X  X  X  X     X  X  X
#                        X  X  X           X  X  X  X  X  X  X  X  X  X
#                     X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
#                  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#               X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#            X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#         X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
# # index 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# peaks(data) # [6, 14]
# valleys(data) # [9, 17]
# peaks_and_valleys(data) # [6, 9, 14, 17]

index_data= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peak_dict = {}
dict_added = 0

peaks = [ ]
valley = [ ]

pointer_a = 0
pointer_b = 2
pointer_dict = 1



while len(peak_dict) < len(index_data):
    peak_dict.update({index_data[dict_added]: data[dict_added]})
    dict_added+=1
    
while pointer_a != index_data[-2]:    
    if data[pointer_a] < peak_dict.get(pointer_dict) > data[pointer_b]:
        peaks.append(pointer_dict)
        pointer_a+=1
        pointer_b+=1
        pointer_dict+=1
    elif data[pointer_a] > peak_dict.get(pointer_dict) < data[pointer_b]:
        valley.append(pointer_dict)
        pointer_a+=1
        pointer_b+=1
        pointer_dict+=1
    else:
        pointer_a+=1
        pointer_b+=1
        pointer_dict+=1
        

p_and_v_combined = (peaks + valley)
p_and_v_combined.sort()
print(p_and_v_combined)
