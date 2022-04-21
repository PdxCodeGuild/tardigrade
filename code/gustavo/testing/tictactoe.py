board = []
1,1|1,2|1,3
2,1|2,2|2,3
3,1|3,2|3,3

# '''
p_1 = {}
p_2 = {}
p_1 = input('''please enter your spot: 1, 2, 3...''')
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
# ''')
# # test_board[] = input('''please enter your x or o: 
# ''')
# for x in range(3):
#     for o in range(3):
#         board.append


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

# test_board = [1,'1','2','3','4','5','6','7','8','9'] 
test_board = [1,' ',' ',' ',' ',' ',' ',' ',' ',' '] 


print(display_board(test_board))