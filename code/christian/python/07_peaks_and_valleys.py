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

    previous_index = 0
    next_index = 2

    while True:

        for item in data:
            if item == data[0]:
                pass
            elif item == data[-1]:
                print("Bypassed last index", item)
                break
            elif item < data[previous_index]:
                print ("Current item:", item, "data previous index: ", data[previous_index])
                previous_index +=1
                next_index +=1
                continue
            elif data[previous_index] < item > data[next_index]:
                    peaks.append(item)
                    previous_index +=1
                    next_index +=1
            else:
                previous_index +=1
                next_index +=1
                continue

        print("peaks ",peaks)

peaks(data)


# def peaks(data):

#     peaks = []

#     previous_index = 0
#     next_index = 2

#     while True:

#         for item in data:
#             if item == data[0]:
#                 pass
#             elif item == data[-1]:
#                 print("Bypassed last index", item)
#                 break
#         if item < data[previous_index]:
#             print ("data previous index", data[previous_index])
#             previous_index +=1
#             next_index +=1
#             continue
#         elif item > data[previous_index]:
#             if item > data[next_index]:
#                 peaks.append(item)
#                 previous_index +=1
#                 next_index +=1
#             else:
#                 previous_index +=1
#                 next_index +=1
#                 continue

#         print("peaks ",peaks)

# peaks(data)

# ## NOTES - WORKS... PRINTS OUT EACH NUMBER WITH THE EXCEPTION OF 1
#     for num in data:
#         if num == data[0]:
#             pass
#         elif num != data[0]:
#             print("num", num)


## TEST TEST