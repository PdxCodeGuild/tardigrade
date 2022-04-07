import random

city = input("Please enter your favorite city: ")
car = input("Please enter your favorite car: ")
team = input("Please enter your favorite sports team: ")
show = input("Please enter your favorite TV show: ")
adj_string = input('Enter 3 adjectives, each separated by a comma: ')
adj_list = adj_string.split(', ')
# print(adj_list)
#create message using a concatenation of all the user inputs provided above
random_adj = random.choice(adj_list)
message = f"{random_adj.title()} {team.title()} fans can mostly always be found watching {random_adj} re-runs of {show.title()} as they speedily drive their {random_adj} {car.title()}s at excessively high speeds up and down the roads of {city.title()}"
print(message)




