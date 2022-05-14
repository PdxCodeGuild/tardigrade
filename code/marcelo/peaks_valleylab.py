def peaks(data):
    peak = []
    for item in range(1, len(data)-1):
        left = data[item-1]
        middle = data[item]
        right = data[item+1]
        if left < middle and right < middle:
            peak.append(item)
    return peak

def valleys(data):
    valley = []
    for item in range(1, len(data)-1):
        left = data[item-1]
        middle = data[item]
        right = data[item+1]
        if left > middle and right > middle:
            valley.append(item)
    return valley

def peaks_valley(data):
    peaks_valley_list=[]
    peaks_valley_list.append(valleys(data))
    peaks_valley_list.append(peaks(data))
    return peaks_valley_list

def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    print(peaks(data))
    print(valleys(data))
    print(peaks_valley(data))
main()
