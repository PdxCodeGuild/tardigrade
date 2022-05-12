data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peaks = []
    for index in range(1, len(data)-1):
        if data[index - 1] < data[index] and data[index + 1] < data[index]:
            peaks.append(index)
    return peaks



def valleys(data):
    valleys = []
    for index in range(1, len(data)-1):
        if data[index -1] > data[index] and data[index +1] > data[index]:
            valleys.append(index)
    return valleys 





def peaks_and_valleys(data):
    poi = []
    peaks_list = peaks(data)
    valleys_list = valleys(data)
    
    for num in valleys_list:
        poi.append(num)
    
    for num in peaks_list:
        poi.append(num)

    poi.sort()

    return poi

print(peaks_and_valleys(data))



