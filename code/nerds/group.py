def legend_board(board):

    
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

test_board = [1,'1','2','3','4','5','6','7','8','9']

<<<<<<< HEAD
# print(legend_board(test_board))
class Game():
    def __init__(self, board) :
        self.board = board
=======
print(legend_board(test_board))
>>>>>>> aac520b866f2f503536fd258a391ac6b75ff5d58

def display_board(board):

    
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

board = [' ',' ','2','3','4','5','6','7','8','9',] * 10
print(display_board(board))







mark = 'X'

if (board[7] == mark and board[8] == mark and board[9]== mark):
    print('WIN')

elif (board[4] == mark and board[5] == mark and board[6]== mark):
    print('WIN')

# else:
#     continue 

# if player1 == turn:
#     mark = 'X'
# else:
#     mark = 'O'
