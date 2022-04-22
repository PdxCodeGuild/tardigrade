class Game
def __repr__(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


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
    
    if player in win_check(board, player):
        print ('You Win')
        game = False

    if board == full_method:



def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 

self.mark = player

win_check(board,player)


    print(spot)
print(move())
print(board)


