# #Bank Account Class
#   #how to use super(). __init__ to refrence another parent class

# class Bank_Account:
#     def __init__(self,accountNumber, name, balance):
#         self.accountNumber = accountNumber
#         self.name = name
#         self.balance = balance

# class Deposit(Bank_Account):
#     def __init__(self, accountNumber, name, balance, deposited):
#         super().__init__(accountNumber, name, balance)
#         self.deposited = deposited
#     def adding_money(self):
#         total = self.balance + self.deposited
#         return print(f'Account {self.accountNumber} has a begining balance of {self.balance}. {self.deposited} has been deposited, the new ending balance is {total}')

# jis_account = Deposit(1720,"jis", 10000,200)
# jis_account.adding_money()


# #draft of the withdraw function 
# #Bank Account Class
# class Bank_Account:
#     def __init__(self,accountNumber, name, balance):
#         self.accountNumber = accountNumber
#         self.name = name
#         self.balance = balance

#     def adding_money(self,deposited):
#         self.deposited = deposited
#         self.balance += self.deposited
#         return print(self.balance)
    
#     def withdrawing_money(self, withdraw):
#         self.withdraw = withdraw
#         self.balance -= self.withdraw
#         return print(self.balance)

# jis_account = Bank_Account(1720,"jis", 10000)
# jis_account.adding_money(200)
# jis_account.withdrawing_money(1)


class Game:
    def __init__(self):
        # Nested list, creates the gameboard
        self.board = [[" "," ", " "],[" "," ", " "],[" "," ", " "]]
    def __repr__(self):
        # This creates the print statement for the gameboard
        game_board = f"""\n\t{self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}
        {self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]}
        {self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}
        """
        return game_board
    def move(self, y, x, player):
        print(player)
        # set x/y to rows and columns
        cols = int(x)
        cols -= 1 #take 1 so it will match columns
        rows = int(y)
        rows -= 1 #take 1 so it will match the rows
        # This will put a x or o in the nested list index
        # while True:
        if self.board[rows][cols] == " ":
            if player[1] == "X":
                self.board[rows][cols] = "X"
            elif player[1] == "O":
                self.board[rows][cols] = "O"
            else:
                print("That spot is taken, choose another.")
    # What token character string has won or none if no one has.
    def calc_winner(self):
        if self.board[0] == ['X','X','X'] or self.board[1] == ['X','X','X'] or self.board[2]  == ['X','X','X']: # across "X" <-----------------------------------------
            return 'X'       
        elif self.board[0] == ['O','O','O'] or self.board[1] == ['O','O','O'] or self.board[2] == ['O','O','O']: # across "O" <----------------------------------------
            return 'O'                       
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == 'X': # down the left side
            return 'X'  
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == 'O': # down the left side
            return 'O'               
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == 'X': # down the middle
            return 'X'
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == 'O': # down the middle
            return 'O'
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == 'X': # down the right side
            return 'X'
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == 'O': # down the right side
            return 'O'
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == 'X': # diagonal
            return 'X'
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == 'O': # diagonal
            return 'O'
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == 'X': # diagonal
            return 'X'
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == 'O': # diagonal
            return 'O'
        else:
            return "no winner"
    # Returns True if the board is full.
    def is_full(self):
        count = 0
        for list in self.board:
            for char in list:
                if char == 'X' or char == 'O':
                    count += 1
        if count == 9:
            return True
        else:
            return False
    # Returns True if the game board is full or a player has won.
    def is_game_over(self):
        full_or_not = self.is_full()
        winner_or_not = self.calc_winner()
        if winner_or_not == 'X':
            # print('Winner is X')
            # print('Game Over')
            return True
        elif winner_or_not == 'O':
            # print('Winner is O')
            # print('Game Over')
            return True
        elif full_or_not == True:
            # print('Game Over')
            return True
        else:
            return False
    
class Player():
    def __init__(self, name, token):
        self.name = name
        self.token = token
# tic_tac_toe = Game()
def main():
    print("Tic Tac Toe")
    print("Rows start fromt he top and colums start from the left.")
    # Players and tokens
    player_1_name = input('Player 1 please enter your name: ')
    player_1_token = input('Do you want to be X or O: ').upper()
    player_2_name = input('Player 2 please enter your name: ')
    player_2_token = ' '
    
    if player_1_token == 'X':
        player_2_token = 'O'
    elif player_1_token == 'O':
        player_2_token == 'X'
    player_1 = Player(player_1_name, player_1_token)
    p1 = [player_1.name, player_1.token]
    player_2 = Player(player_2_name, player_2_token)
    p2 = [player_2.name, player_2.token]
 
    while True:
        # rows = input("What Row(1-3): ")
        rows = 1
        cols = 1
        while 0 < rows < 4 and 0 < cols < 4:
            print(f"{player_1.name}'s Turn({player_1.token})")
            rows = int(input("Row number must be #1-3: "))  
            cols = int(input("Column number must be #1-3: "))
        
            if 0 < rows < 4 and 0 < cols < 4:
                if tic_tac_toe.board[rows-1][cols-1] != "X" and  tic_tac_toe.board[rows-1][cols-1] != "O": 
                    tic_tac_toe.move(rows, cols, p1)
                    print(tic_tac_toe)
                    print(tic_tac_toe.board)
                    break
                else:
                    continue
        else:
            continue
        tic_tac_toe.is_game_over()
        if tic_tac_toe.is_game_over() == True:
            winner = tic_tac_toe.calc_winner()
            if player_1.token == winner:
                print(f"{player_1.name} is the winner!")
            elif player_2.token == winner:
                print(f"{player_2.name} is the winner!")
            else:
                print("Tie, Game Over")
            break
    
        while 0 < rows < 4 and 0 < cols < 4:
            print(f"{player_2.name}'s Turn({player_2.token})")
            rows = int(input("Row number must be #1-3: "))
            cols = int(input("Column number must be #1-3: "))
            
            if 0 < rows < 4 and 0 < cols < 4:
                if tic_tac_toe.board[rows-1][cols-1] != "X" and  tic_tac_toe.board[rows-1][cols-1] != "O": 
                    tic_tac_toe.move(rows, cols, p2)
                    print(tic_tac_toe)
                    print(tic_tac_toe.board)
                    break
                else:
                    continue
            else:
                rows = 1
                cols = 1
                continue
        tic_tac_toe.is_game_over()
        if tic_tac_toe.is_game_over() == True:
            winner = tic_tac_toe.calc_winner()
            if player_1.token == winner:
                print(f"{player_1.name} is the winner!")
            elif player_2.token == winner:
                print(f"{player_2.name} is the winner!")
            else:
                print("Tie, Game Over")
            break
tic_tac_toe = Game()
print(tic_tac_toe)
main()