

player_1_moves = set()
player_2_moves = set()


class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token


class Game:
    def __init__(self):
        self.board = {
            (0, 0): 1, (0, 1): 2, (0, 2): 3,
            (1, 0): 4, (1, 1): 5, (1, 2): 6,
            (2, 0): 7, (2, 1): 8, (2, 2): 9,
        }

    def __repr__(self):
        return self.board

    def move(self, x, y, player):

        self.player = player

        if self.player == "X":
            player_1_moves.add(self.board[(x, y)])
            # print(player_1_moves)
        else:
            player_2_moves.add(self.board[(x, y)])
            # print(player_2_moves)

        # return

    def calc_winner(self, player_1_moves, player_2_moves):
        win_condition = ({1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {
                         2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7})

        # if len(player_1_moves) == 0 and len(player_2_moves) == 0:
        #     return False
        # print(player_1_moves, "player 1", len(player_1_moves))
        # print(player_2_moves, "player 2", len(player_2_moves))

        for i, v in enumerate(win_condition):
            if len(player_1_moves) == 3 and player_1_moves == v:
                print(player_1_moves, v, "player 1", len(player_1_moves))
                return True
            elif len(player_2_moves) == 3 and player_2_moves.issubset(v):
                print(player_2_moves, v, "player 2")
                return True
            else:
                return False

    def is_full(self):
        player_1_set = player_1_moves
        player_2_set = player_2_moves
        board_filling = player_1_set.union(player_2_set)
        if board_filling == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            return True
        else:
            return False

    def is_game_over(self):
        # first, check whether there is a winner
        if self.calc_winner(player_1_moves, player_2_moves) == True:
            return True
        # if there is no winner, check whether the board is full
        if self.is_full() == True:
            return True
        # if there is no winner, and the board is not full, the game is not over yet
        else:
            return False


def main():

    # player_name = input("Please enter a name for Player 1: ")
    # player_token = input("Please select \"X\"or \"O\" for Player 1: ")
    # # if player_token == "X":
    # #     player_2_token = "O"
    # # elif player_1_token == "O":
    # #     player_2_token = "X"
    # # player_2_name = input("Please enter a name for Player 2: ")

    # print(f"Player: {player_name} has selected {player_token}'s")
    # print(f"Player 2: {player_2.name} has selected {player_2_token}'s")
    # player = Player(player_name, player_token)
    # player_2 = Player(player_2_name, player_2_token)
    # print(player)

    game = Game()

    grid = ([
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']
            ])

    while True:

        if len(player_1_moves) > len(player_2_moves):
            player = 'O'
        else:
            player = 'X'
        # first, check whether the game is over
        if game.is_game_over() == True:
            print(f"The game is over. Congrats to....!")
            break
        # if the game is not over, request the next move
        # else:

        x = int(input('Enter x coordinate from 0-2: '))
        y = int(input('Enter y coordinate from 0-2: '))

        grid[x][y] = player

        Array = [grid[0], grid[1], grid[2]]
        for i in Array:
            print('|'.join(i))

            game.move(x, y, player)


# game_1 = Game(board)
main()
