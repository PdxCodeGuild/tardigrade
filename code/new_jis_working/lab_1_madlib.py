import random

x = input("Would you like to play the madlib? yes/no: ")


while x != 'no':

    a = input("Enter your name: ")
    a_1 = input("Enter three words to descrbe yourself (seperate them with a space): ")
    b = input("Enter a company: ")
    c = input("Enter a date: ")
    d = input("Enter three dream job (seperate them with a space): ")
    e = input("current state you live in: ")

    list_a_1 = a_1.split()
    a_1 = random.choice(list_a_1)

    list_d = d.split()
    d = random.choice(list_d)

    



    print(f"My name is {a_1} {a} and on {c} I will recieve the best news ever from {b}. \n{b} will offer me a position as a {d} and it weill be a remote postion in {e}! Aren't you glad you did this madlib?" )
    
    x = input("Would you like to try again? Entuer yes/no: ")
