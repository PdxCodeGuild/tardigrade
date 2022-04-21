# def legend_board(board):

    
#     print('   |   |')
#     print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
#     print('   |   |')
#     print('-----------')
#     print('   |   |')
#     print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
#     print('   |   |')
#     print('-----------')
#     print('   |   |')
#     print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
#     print('   |   |')

# test_board = [1,'1','2','3','4','5','6','7','8','9']

# print(legend_board(test_board))

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

board = [' ','o','o','o','o','o','o','X','X','X',] * 10
print(display_board(board))

mark = 'X'

if (board[7] == mark and board[8] == mark and board[9]== mark):
    print('WIN')
    break
elif (board[4] == mark and board[5] == mark and board[6]== mark):
    print('WIN')
    break
else:
    continue 

if player1 == turn:
    mark = 'X'
else:
    mark = 'O'
