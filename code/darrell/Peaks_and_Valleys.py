# Define the following functions:
# peaks(data) - Returns the indices of peaks. A peak has a lower number on both the left and the right.
# valleys(data) - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
# peaks_and_valleys(data) - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

peak_list = []
valley_list = []
pv_list = []


def peaks(data):
    x = 0
    peak_list = []
    while x < len(data)-1:
        if data[x] > data[x-1] and data[x] > data[x+1]:
            print(x)
            peak_list.append(x)
            print(peak_list)
        x += 1
    s = str(peak_list)
    print(s)
    return (s)


def valleys(data):
    x = 0
    valley_list = []
    while x < len(data)-1:
        if data[x] < data[x-1] and data[x] < data[x+1]:
            print(x)
            valley_list.append(x)
            print(valley_list)
        x += 1
    return (valley_list)


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks(data)
valleys(data)


def peaks_and_valleys(data):
    pv_list.append(peaks(data))
    pv_list.append(valleys(data))
    print(pv_list)
    return pv_list


peaks_and_valleys(data)
