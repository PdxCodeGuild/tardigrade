from ast import NameConstant


def narcissistic(num):
    exp = len(str(num))
    sum = 0
    numbers = str(num)
    for nums in numbers:
        sum += pow(int(nums), exp)
        if sum == num:
            nar = True
        else:
            nar = False
    return nar

print(narcissistic(153))


