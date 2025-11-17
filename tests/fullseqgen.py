from tilegame.main import *
from tilegame.stats import count_freqs
import time 
import math
import matplotlib.pyplot as plt
import numpy as np
import itertools

seqs = [''.join(p) for p in itertools.product(['W', 'A', 'S', 'D'], repeat=4)]
n = 1
limit = 2000
board = np.array([[0, 0, 2, 0], 
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 2, 0, 0]])

print(f"| {len(seqs)} sequences will be tested for {n} games each ( = { (n * len(seqs))} games)")

best_seq = None
best_tile = 0
best_seq_count = 0

for seq in seqs:
    print(seq)
    best_seq_tile = 0
    best_seq_tile_count = 0

    for i in range(n):
        result = simulate(seq, board.copy(), limit) #result = (num_moves, best_tile, best_coods, board, flag)
        tile = result[1]

        if tile > best_seq_tile:
            best_seq_tile = tile
            best_seq_tile_count = 1
        elif tile == best_seq_tile:
            best_seq_tile_count += 1

    if best_seq_tile > best_tile:
        best_tile = best_seq_tile
        best_seq = seq
        best_seq_count = best_seq_tile_count
    elif best_seq_tile == best_tile and best_seq_tile_count > best_seq_count:
        best_seq = seq
        best_seq_count = best_seq_tile_count

print("------------------------------------")
print(f"| Board Tested:")
print(board)
print(f"| Best sequence used: {best_seq}")
percent = (best_seq_count / n) * 100
print(f"| Best tile found: {best_tile} {best_seq_count} in {n} games ({percent}%)")
print("------------------------------------")

