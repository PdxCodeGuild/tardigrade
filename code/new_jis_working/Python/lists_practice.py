

# Practice 5: Lists
# Copy and paste this file into your own "05_lists.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 05_lists.py"


# Even Even
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.




def even_even(nums):
    even_list = [ ]
    odd_list = [ ]

    for x in nums:
        if x%2 == 0:
            even_list.append(x)
        else:
            odd_list.append(x)
    
    if len(even_list)%2 == 0:
        return True
    else:
        return False




def test_even_even():
    assert even_even([5, 6, 2]) == True
    assert even_even([5, 5, 2]) == False

#Passed#####################################################################################################PASSED

# Reverse
# Write a function that takes a list and returns a new list with the elements in reverse order

def reverse(nums):
    nums.reverse()
    return nums


def test_reverse():
    assert reverse([1, 2, 3]) == [3, 2, 1]

#Passed#####################################################################################################PASSED


# Common Elements
# Write a function to find all common elements between two lists.


def common_elements(nums1, nums2):
    alike_list = [ ]
    for x in set(nums1):
        for y in set(nums2):
            if x == y:
                alike_list.append(x)
            continue
    return alike_list

def test_common_elements():
    assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]

#Passed#####################################################################################################PASSED


# Combine
# Write a function to combine two lists of equal length into one, alternating elements.


def combine(nums1, nums2):
    combined_list= [ ]
    if len(nums1) == len(nums2):
        for x in nums1:
            combined_list.append(x)
            for y in nums2:
                combined_list.append(y)
                break
            del nums2[0]
        return combined_list
    else:
        return("These lists are not equal in length")





def test_combine():
    assert combine(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]

#Passed#####################################################################################################PASSED

# Find Pair
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number. 
# Optional: return a list of all pairs of numbers that sum to a target value.


def find_pair(nums1, nums2):
    combined_list = [ ]
    z= 0
    
    while len(combined_list) != 2:
        for x in nums1:
            
            y = nums1[z]
            x + y
            
            if x+y == nums2:
               combined_list.append(x)
               combined_list.append(y)
               continue 
        z += 1
            
    return combined_list



def test_find_pair():
    assert find_pair([2, 6, 5, 3], 7) == [5, 2]

#Passed#####################################################################################################PASSED

# Average
# Write a function to find the average of a list of numbers


def average(nums):
    
    x = sum(nums)/len(nums)
    return x



def test_average():
    assert average([1, 2, 3, 4, 5]) == 3

#Passed#####################################################################################################PASSED

# Remove Empty
# Write a function to remove all empty strings from a list.


def remove_empty(mylist):
    for x in mylist:
        if x == '':
            mylist.remove('')
    return mylist


def test_remove_empty():
    assert remove_empty(['a', 'b', '', 'c', '', 'd']) == ['a', 'b', 'c', 'd']

#Passed#####################################################################################################PASSED

# Merge
# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.

def merge(nums1, nums2):
    
    merged_list = [ ]
    stopper = len(nums1+nums2)
    
    while len(nums2) != 0:
        x = nums1[0]
        y = nums2[0]
        temp_list= [ ]
    
        temp_list.append(x)
        temp_list.append(y)
        merged_list.append(temp_list)
        #print(merged_list)
        del nums1[0] 
        del nums2[0]
        #print(merged_list)
        continue
    
    return merged_list



def test_merge():
    assert merge([5, 2, 1], [6, 8, 2]) == [[5, 6], [2, 8], [1, 2]]

#Passed#####################################################################################################PASSED

# # Combine All
# # Write a function `combine_all` that takes a list of lists, and returns a list containing each element from each of the lists.

def combine_all(nums):
    new_list = [ ]
    for x in nums:
        for y in x:
            new_list.append(y)
    return new_list
    


def test_combine_all():
    assert combine_all([[5, 2, 3], [4, 5, 1], [7, 6, 3]]) == [5, 2, 3, 4, 5, 1, 7, 6, 3]

#Passed#####################################################################################################PASSED


# Fibonacci
# Write a function that takes `n` as a parameter, and returns a list containing the first `n` [Fibonacci Numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

def fibonacci(n):
    new_list = [1,1 ]
    y = 0
    z = 1
        
    for x in range(2,n):
        fib_number = new_list[y] + new_list[z]
        y+=1
        z+=1
        new_list.append(fib_number)
    return new_list 

    

def test_fibonacci():
    assert fibonacci(8) == [1, 1, 2, 3, 5, 8, 13, 21]

#Passed#####################################################################################################PASSED


# Factorial
# Write a function that takes `n` as a parameter and returns `n` factorial.


def factorial(n): 
    fact = 1
      
    for i in range(1,n+1):
        fact = fact * i
        print(fact)
    return (fact)

        


def test_factorial():
    assert factorial(5) == 120

#Passed#####################################################################################################PASSED


# Find Unique
# Write a function which takes a list as a parameter and returns a new list with any duplicates removed.

#note by jis turn the list into a set and then turn it back into a list easy peasy 

def find_unique(nums):
    nums = set(nums)
    nums = list(nums)
    nums.sort()
    return nums


def test_find_unique():
    nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
    assert find_unique(nums) == [12, 24, 35, 88, 120, 155]

    #Passed#####################################################################################################PASSED