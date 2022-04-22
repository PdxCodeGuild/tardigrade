



board = [' ',' ','2','3','4','5','6','7','8','9',]


class Player():
    def __init__(self, name, token):
        self.name =  name
        self.token = token

# def 
p1_start = print(''' 
Hello Players. \nWelcome to Nerds Tic Toe.
\nPlayer 1 is X's
\nPlayer 2 is O's
\nPlease choose a space on the board by typing in the number of the space:


       |   |
     7 | 8 | 9
       |   |
    -----------
       |   |
     4 | 5 | 6
       |   |
    -----------
       |   |
     1 | 2 | 3
       |   |

''')

# input(f'Player 1, please choose your spot')
def is_even(x):
    if x % 2 == 0:
        return True

def move():
    p1 = 'X'
    p2 = 'O'
    spot = 0
    mv_counter = 0
    game = True
    while game == True:
        if is_even(mv_counter) == True:
            player = p1
            spot = int(input(f"Hello Player 1 you are {player}'s. please choose your spot 1-9: "))
            board[spot] = player

            mv_counter += 1
            print(spot)
            print(mv_counter)
            print(board)
    
        else:
            player = p2
            spot = int(input(f"Hello Player 2 you are {player}'s. please choose your spot 1-9: "))
            board[spot] = player
            mv_counter += 1
            print(mv_counter)
            print(board)
    return board
    print(spot)
print(move())
print(board)