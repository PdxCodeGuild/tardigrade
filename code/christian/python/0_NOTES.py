
# class Game:
#     def __init__(self, board):
#         self.board = board
#     def __repr__(self):
#         self.board = {
#             (1, 1): 1, (1, 2): 2, (1, 3): 3,
#             (2, 1): 4, (2, 2): 5, (2, 3): 6,
#             (3, 1): 7, (3, 2): 8, (3, 3): 9,
#         }
#         print(self.board)


one = "1"
two = "2"
three = "3"

while True:

    board = f'''
    [{one}] [{two}] [{three}]
    [{4}] [{5}] [{6}]
    [{7}] [{8}] [{9}]
    '''
    print(board)

    tile_choice = input("Choose a tile: ")
    if tile_choice == "1":
        one = one = "X"
    elif ti
        

print(board)