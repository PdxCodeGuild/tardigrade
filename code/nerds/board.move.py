class Game():
    def __init__(self, board,mark,player):
        self.board = board
        self.mark = mark
        self.player = player

    def check_win(self):

        board = self.board 
        mark = self.mark 
        player = self.player 
        
        if (board[7] == mark and board[8] == mark and board[9] == mark)  == True:
            return (f'{player} wins')
        elif (board[4] == mark and board[5] == mark and board[6] == mark)  == True:
            return (f'{player} wins')
        elif (board[1] == mark and board[2] == mark and board[3] == mark)  == True:
            return (f'{player} wins')
        elif (board[7] == mark and board[4] == mark and board[1] == mark)  == True:
            return (f'{player} wins')
        elif (board[8] == mark and board[5] == mark and board[2] == mark)  == True:
            return (f'{player} wins')
        elif (board[9] == mark and board[6] == mark and board[3] == mark)  == True:
            return (f'{player} wins')
        elif (board[7] == mark and board[5] == mark and board[3] == mark)  == True:
            return (f'{player} wins')
        elif (board[9] == mark and board[5] == mark and board[1] == mark) == True:
            return (f'{player} wins')
        else:
            return False

    # def is_full(self):
    #     something = [' ','1','2','3','4','5','6','7','8','9']
    #     thing = ' '
    #     for i in range(1,10):
    #         for i in something:
    #            if i in self.board:


     
        

    def __repr__(self):
        board = self.board        
        w = f"""
           |   |
        {board[7]}  | {board[8]} |  {board[9]}
           |   |
        -----------
           |   |
        {board[4]}  | {board[5]} |  {board[6]}
           |   |
        -----------
           |   |
        {board[1]}  | {board[2]} |  {board[3]}
           |   |
      """
        return w

# board = [' ','1','2','3','4','5','6','7','8','9',]
# my_game = Game(board)
# print(repr(my_game))



class Player():
    def __init__(self, name, token):
        self.name =  name
        self.token = token

# def "
p1_start = print(f'''
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

# input(f'Player 1, please choose your spot
def is_even(x):
    if x % 2 == 0:
        return True


p1 = 'X'
p2 = 'O'
spot = 0
mv_counter = 0
game = True
player_turn = 'Player 1'
player = p1
board = [' ','1','2','3','4','5','6','7','8','9']
# my_game = Game(board)
my_game = Game(board,player,player_turn)
print(repr(my_game))

while game == True:
    
    if is_even(mv_counter) == True:
        player = p1
        spot = int(input(f"Hello Player 1 you are {player}'s. please choose your spot 1-9: "))
        board[spot] = player
        

        mv_counter += 1
        player_turn = 'Player 1'
        print(spot)
        print(mv_counter)

        print(repr(my_game))

    else:
        player = p2
        spot = int(input(f"Hello Player 2 you are {player}'s. please choose your spot 1-9: "))
        board[spot] = player
        
        mv_counter += 1
        player_turn = 'Player 2'
        print(mv_counter)
        print(repr(my_game))


    if mv_counter >= 5:
        if my_game.check_win() == False:
            continue
        else:
            print(my_game.check_win())
            game = False



# def is_full(self, board):
#     for row in self.board:
#         for item in row:
#             if item != 'x' or 'o':
#                 return False
#         return True





# def win_check(board,mark):
    
#     return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
#     (board[4] == mark and board[5] == mark and board[6] == mark) or 
#     (board[1] == mark and board[2] == mark and board[3] == mark) or 
#     (board[7] == mark and board[4] == mark and board[1] == mark) or 
#     (board[8] == mark and board[5] == mark and board[2] == mark) or 
#     (board[9] == mark and board[6] == mark and board[3] == mark) or 
#     (board[7] == mark and board[5] == mark and board[3] == mark) or 
#     (board[9] == mark and board[5] == mark and board[1] == mark)) 

# self.mark = player

# win_check(board,player)


#     print(spot)
# print(move())
# print(board)