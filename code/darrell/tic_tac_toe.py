class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
        player_1_name = input("Please enter a name for Player 1: ")
        player_1_token = input("Please select \"X\"or \"O\" for Player 1: ")
        player_2_name = input("Please enter a name for Player 2: ")
        player_2_token = input("Please select \"X\"or \"O\" for Player 2: ")
        player_1 = Player(player_1_name, player_1_token)
        player_2 = Player(player_2_name, player_2_token)
        print(f"Player 1: {player_1.name} has selected {player_1_token}'s")
        print(f"Player 2: {player_2.name} has selected {player_2_token}'s")


# board = [[[i, j] for j in range(3)] for i in range(3)]
board = [[[] for y in range(3)] for x in range(3)]
x = int(input("please select x coord: "))
y = int(input("please select y coord: "))
board[x][y].append("X")

print(board)


def move(self, x, y, player):
    self.x = x
    self.y = y
    self.player = player
    player_move = board[x][y].append(self.token)
    # if player == player_1:
    #     player_move = board[x][y].append(player_1_token)
    # else:
    #     player_move = board[x][y].append(player_2_token)
    return player_move


class Game:
    def __init__(self, board):
        self.board = board

    def __repr__(self):
        print(self.board)
        return self.board

    # def move(self, x, y, player):
        # board.move(2, 1, player_1)
        return

    def calc_winner(self):
        # board.calc_winner()
        return

    def is_full(self):
        # board.is_full()
        return

    def is_game_over(self):
        # first, check whether there is a winner
        if self.board.calc_winner() == True:
            return True
        # if there is no winner, check whether the board is full
        elif self.board.is_full() == True:
            return True
        # if there is no winner, and the board is not full, the game is not over yet
        else:
            return False

    def main(self):
        while True:
            # first, check whether the game is over
            if self.board.is_game_over() == True:
                break
            # if the game is not over, request the next move
            else:
                self.board.move()


# for x in range(0, 3):
#     for y in range(0, 3):
#         print([x][y], end="")
# print("\n")
