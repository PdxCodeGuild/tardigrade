## Eberhardt

## https://github.com/PdxCodeGuild/hydra/blob/master/1%20Python/labs/07%20Peaks%20and%20Valleys.md

##Define the following functions:

# peaks(data):
# Returns the indices of peaks. 
# A peak has a lower number on both the left and the right.

# valleys(data):
# Returns the indices of 'valleys'. 
# A valley is a number with a higher number on both the left and the right.

# peaks_and_valleys(data):
# Uses the above two functions to compile a single list of the peaks and valleys, 
# in order of appearance in the original data.

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peaks = []
    for i in range(1, len(data)- 1):
        if data[i-1] < data[i] > data[i+1]:
            peaks.append(i)
    print("Indices of Peaks: ", peaks)

peaks(data)       

def valleys(data):
    valleys = []
    for i in range(1, len(data)-1):
        if data[i-1] > data[i] < data[i+1]:
            valleys.append(i)
    print("Indices of Valleys: ", valleys)

valleys(data)

def peaks_and_valleys(data):
    peaks_valleys = []
    for i in range(1, len(data)- 1):
        if data[i-1] < data[i] > data[i+1]:
            peaks_valleys.append(i)
        elif data[i-1] > data[i] < data[i+1]:
            peaks_valleys.append(i)
    print("Indices of Peaks and Valleys: ", peaks_valleys)

peaks_and_valleys(data)
