

board = [' ',' ','2','3','4','5','6','7','8','9',] * 10
mv_counter = 0

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
def move(self, spot):
    p1 = 'X'
    p2 = 'O'
    spot = 0
    
    if mv_counter == 0:
        player = p1
        input(f"Hello Player 1 you are {player}'s. please choose your spot 1-9: ")
        self.spot = board[spot].append(p1)
    mv_counter += 1
    print(self.spot)
    
    elif mv_counter == 1:
        input(f"Hello Player 2 you are {player}'s. please choose your spot 1-9: ")
        self.spot = board[spot].append(p2)
    mv_counter += 1
    print(self.spot)

print(board)