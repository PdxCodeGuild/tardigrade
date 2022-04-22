
# Practice 5: Lists
# Copy and paste this file into your own "05_lists.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 05_lists.py"


# Even Even
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.
"""
first I need to iterate through the list containing integers
then i Need to use Modulo % 2 to find out if the number is even 
then I need to return true?


"""


# def even_even(nums):
#     even_nums = 0
    
#     for num in range(len(nums)):
#         if nums[num] % 2 == 0:
#             even_nums = even_nums + 1
#     if even_nums % 2 == 0:
#         return True
#     else: 
#         return False

#     print(even_nums)
            

# def test_even_even():
#     assert even_even([5, 6, 2]) == True
#     assert even_even([5, 5, 2]) == False

 

# Reverse
# Write a function that takes a list and returns a new list with the elements in reverse order

# def reverse(nums):
#     nums.reverse()
#     return nums


# def test_reverse():
#     assert reverse([1, 2, 3]) == [3, 2, 1]


# Common Elements
# Write a function to find all common elements between two lists.


# def common_elements(nums1, nums2):
#     # new_list = list(set(nums1).intersection(nums2))
#     # return new_list


    
        
    



# def test_common_elements():
#     assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]


# Combine
# Write a function to combine two lists of equal length into one, alternating elements.


# def combine(nums1, nums2):
#     new_list = []   ### this gives me an empty list to add values into
#     for char in range(len(nums1)):  ### I could nest this loop because the I knew the list were the same length, thanks for that tip Alex!
#         new_list.append(nums1[char])  ### within my for loop the empty list is being appended from the first list at the index of char which is loopin "a" "b" "c"
#         new_list.append(nums2[char])  ### doing the same thing with the other list
#     return new_list  ### returning my new list, test didn't work until you did this Keith!!


# def test_combine():
#     assert combine(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]


# Find Pair
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number. Optional: return a list of all pairs of numbers that sum to a target value.


# def find_pair(nums, target):
#     final_list = []
    
#     for i in range(len(nums)-1):   ##### this once again loops over my list
#        for k in range(i+1, len(nums)):   #### this is another for loop inside of loop that is checking for the next index position
#            if nums[i] + nums[k] == target:
#                final_list.append(nums[i])
#                final_list.append(nums[k])
#     return final_list


    


# def test_find_pair():
#     assert find_pair([5, 6, 2, 3], 7) == [5, 2]


# Average
# Write a function to find the average of a list of numbers


# def average(nums):
#     average = sum(nums) / len(nums)
#     return average

    


# def test_average():
#     assert average([1, 2, 3, 4, 5]) == 3


# Remove Empty
# Write a function to remove all empty strings from a list.


# def remove_empty(mylist):
#     new_list = []
#     for char in mylist:
#         if char.strip() != '':
#             new_list.append(char)
#     return new_list

   


# def test_remove_empty():
#     assert remove_empty(['a', 'b', '', 'c', '', 'd']) == ['a', 'b', 'c', 'd']


# Merge
# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.




# def merge(nums1, nums2):
#     final_list = []
#     for num in range(len(nums1)):
#         print(nums1[num])
#         print(nums2[num])
#         final_list.append([nums1[num], nums2[num]])
        
#     return final_list
    
# def test_merge():
#     assert merge([5, 2, 1], [6, 8, 2]) == [[5, 6], [2, 8], [1, 2]]


# Combine All
# Write a function `combine_all` that takes a list of lists, and returns a list containing each element from each of the lists.


# def combine_all(nums):
#     new_list = nums[0] + nums[1] + nums[2]
#     return new_list


# def test_combine_all():
#     assert combine_all([[5, 2, 3], [4, 5, 1], [7, 6, 3]]) == [5, 2, 3, 4, 5, 1, 7, 6, 3]


# Fibonacci
# # Write a function that takes `n` as a parameter, and returns a list containing the first `n` [Fibonacci Numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + (n-1)
    
 


def test_fibonacci():
    assert fibonacci(8) == [1, 1, 2, 3, 5, 8, 13, 21]

# Factorial
# Write a function that takes `n` as a parameter and returns `n` factorial.


# def factorial(n):
#     fact = 1
#     for num in range(2, n + 1):
#         fact *= num
#     return fact
    


# def test_factorial():
#     assert factorial(5) == 120


# Find Unique
# Write a function which takes a list as a parameter and returns a new list with any duplicates removed.


# def find_unique(nums):
#     new_list = []
#     for num in nums:
#         if num not in new_list:
#             new_list.append(num)
#     return new_list


# def test_find_unique():
#     nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
#     assert find_unique(nums) == [12, 24, 35, 88, 120, 155]