# Chan Saechao

# Given test conditions
test_condition1 = 'I love arrays they are my favorite'
test_condition2 = 'I love days off'
test_condition3 = 'my favorite season is'

# Split and turn into List
testListOne = test_condition1.split(" ")
testListTwo = test_condition2.split(" ")
testListThree = test_condition3.split(" ")

# Prints the statements of all 3 lists
print(testListOne)
print(testListTwo)
print(testListThree)

stringList  =  input("Which test condition do you want to convert? Type in 1, 2, or 3 for the test condition to convert or type something:  ")

if stringList ==  "1":
    testListOne = test_condition1.split(" ")
    print(testListOne)

elif stringList == "2":
    testListTwo = test_condition2.split(" ")
    print(testListTwo)
elif stringList == "3":
    testListThree = test_condition3.split(" ")
    print(testListThree)
else:
    myList = stringList.split()
    print(myList)