import random

def pick6():
  numbers_list= list(range(1, 100))
  random6_numbers = []
  for idx in range (0, 6):
    random6_numbers.append(random.choice(numbers_list))
  return random6_numbers

def game():
  numbers_list= list(range(1, 100))
  new_list = []
  for idx in range (0, 6):
    new_list.append(random.choice(numbers_list))
  return new_list

def num_matches(pick6, game):
  matched_list=[]
  for idx in range(len(pick6)):
    if idx in range(len(game)):
      if pick6[idx] == game[idx]:
        matched_list.append(idx)
  return matched_list

how_many_games= 100000
total_balance= 0
for idx in range(how_many_games):
  current_balance=0
  player_1=pick6()
  print(f'the numbers you choose were {player_1}')
  player_2=game()
  print(f'the other player choose {player_2}')
  matched= num_matches(player_1, player_2)
  print(f'heres the matched {matched}')
  match_counter=0
  for match in matched:
    match_counter+= 1
  if match_counter == 1:
    current_balance+=4
  elif match_counter == 2:
    current_balance+=7
  elif match_counter == 3:
    current_balance+=100
  elif match_counter == 4:
    current_balance+=50000
  elif match_counter == 5:
    current_balance+=1000000
  elif match_counter == 6:
    current_balance+=25000000
  else:
    current_balance==0
  new_balance= current_balance -2
  total_balance= new_balance + total_balance

expenses = how_many_games * 2
roi = (current_balance - expenses) / expenses

end= (f'after {how_many_games} games your total balance is {total_balance}\n and your roi is {roi}')

print(end)

# numbers_list=0
# x= pick6()
# y=game()
# z=num_matches(x, y)

# print (x)
# print(y)
# print(z)