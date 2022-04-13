# Chan Saechao
# Peaks and Valleys

"""
    1.  peaks(data) - Returns the indices of peaks. A peak has a lower number on both the left and the right.
    2.  valleys(data) - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
    3.  peaks_and_valleys(data) - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

"""

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peaks_list = []
    count = 0
    for index in range(len(data)-1):
        count_minus_1 = count - 1
        count_plus_1 = count + 1
        # print(f'index: {index}, data-1: {data[count_minus_1]}, data: {data[index]},  data+1: {data[count_plus_1]}')
        if data[count_minus_1] < data[index] and data[count_plus_1] < data[index]:
            peaks_list.append(index)
        # print(f'data: {data[index]}')
        count += 1
    # print(peak_list)
    return peaks_list

peaks(data)
print(f'peaks: {peaks(data)}')

def valleys(data):
    valleys_list = []
    for index in range(len(data)-1):
        # print('index: {index}, data-1: {data[index - 1]}, data: {data[index]},  data+1: {data[count_plus_1]}')
        # print("index", data[index - 1])
        if data[index - 1] and data[index + 1]:
            if data[index] > data[index + 1] and data[index + 2] > data[index + 1]:
                valleys_list.append(index + 1)
        # print(f'data: {data[index]}')
    # print(peak_list)
    return valleys_list

valleys(data)
print(f'valleys: {valleys(data)}')

def peaks_and_valleys(peaks, valleys):
    peaks_and_valleys_list = peaks + valleys
    return peaks_and_valleys_list

print('My peaks and valleys: ', peaks_and_valleys(peaks(data), valleys(data)))

# Version 2