amount = float(input("Please enter a dollar amount: "))
val = amount*100  
quarters = val // 25
quarters = int(quarters)
print(quarters, "quarters")
val = val%25
dimes = val // 10
dimes = int(dimes)
print(dimes, "dimes")
val =val%10
nickels = val // 5
nickels = int(nickels)
print(nickels, "nickels")
val = val%5
pennies = val
pennies = int(pennies)
print(pennies, "pennies")