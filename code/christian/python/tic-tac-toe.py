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
        else:
            player_2_moves.add(self.board[(x, y)])
    def calc_winner(self, player_1_moves, player_2_moves):
        win_condition = ({1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {
                         2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7})
        for i, v in enumerate(win_condition):
            if player_1_moves.issuperset(v) or player_2_moves.issuperset(v):
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
        if self.calc_winner(player_1_moves, player_2_moves) == True:
            print(f"The game is over. Congrats to...{self.player}!")
            return True
        if self.is_full() == True:
            return True
        else:
            return False
def main():
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
        if game.is_game_over() == True:
            break
        x = int(input('Enter x coordinate from 0-2: '))
        y = int(input('Enter y coordinate from 0-2: '))
        if grid[x][y] != '_':
            print('Choice already selected, try again!')
            continue
        grid[x][y] = player
        Array = [grid[0], grid[1], grid[2]]
        for i in Array:
            print('|'.join(i))
            game.move(x, y, player)
main()