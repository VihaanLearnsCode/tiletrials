from tilegame.main import *
from tilegame.state import *
from tilegame.stats import *
import numpy as np
import random
import time
import math

start = time.time()
n = 10000
best_tile = 0
best_sequence = ""
game_n = 0
longest = 0

tile_nums = []

for i in range(1, n + 1):
    if i % 500 == 0:
        print(i)

    init_board = generate().copy()
    board = init_board.copy()
    sequence = ""
    while(not check_end(board)):
        max_tile = board.max()
        best_board = board.copy()
        best_move = None
        for move in ['W', 'A', 'S', 'D']:
            new_board = update_board(board.copy(), move)
            if np.array_equal(new_board, board):
                continue

            new_max = new_board.max()
            if new_max >= max_tile:
                max_tile = new_max
                best_move = move
                best_board = new_board
        
        default_move = random.choice(valid_moves(board))

        if best_move is not None:
            sequence += best_move
            board = best_board
        else:
            if default_move == 'Z':
                break
            sequence += default_move
            board = update_board(board.copy(), default_move)
        board = spawn_tile(board)
    
    tile_nums.append(board.max())
    if board.max() > best_tile or (board.max() == best_tile and len(sequence) > longest):
        longest = len(sequence)
        game_n = i
        final_init_board = init_board
        final_board = board
        best_tile = board.max()
        best_sequence = sequence

end = time.time()

print(" ")
print("------------FINAL OUTPUT------------")
print("------------------------------------")
print(f"Highest tile of {final_board.max()} earned in game {game_n}")
print(f"Initial Board:")
print(final_init_board)
print(" ")
print(" ")
print(f"Final Board:")
print(final_board)
print(" ")
print(" ")
print(f"Sequence used: {best_sequence}")
print("------------------------------------")

freq_dict = count_freqs(tile_nums)

print(" ")
print("------------------------------------")
print("|    Best Tile   :    Frequency (%)   ")
print("|                                  ")
freq_dict = dict(sorted(freq_dict.items()))
for key in freq_dict:
    percent = (freq_dict[key] / n) * 100
    print(f"|       {key}               {freq_dict[key]}   ({percent:.2f}%)")
print("|                                  ")
print("------------------------------------")

taken = end - start
minutes = math.floor(taken / 60)
seconds = math.floor(taken % 60)

print("------------------------------------")
print(f"| Time taken = {minutes} minutes {seconds} seconds")
print("------------------------------------")

#paste below in code after inner loop for more data
# print(" ")
# print(f"Game {i}")
# print("------------------------------------")
# print(f"Initial Board:")
# print(init_board)
# print(" ")
# print(" ")
# print(f"Final Board:")
# print(board)