tc1 = []
tc2 = []
tc3 = []
test_condition1 = 'I love arrays they are my favorite'
test_condition2 = 'I love days off'
test_condition3 = 'my favorite season is'
tc1 = test_condition1.split()
tc2 = test_condition2.split()
tc3 = test_condition3.split()


def div_array(param1, param2):
    tc1 = param1.split() + param2.split()
    return  print(tc1)

div_array(test_condition1, test_condition2)