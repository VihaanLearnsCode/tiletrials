from tilegame.main import *
from tilegame.stats import count_freqs
import time 
import math
import matplotlib.pyplot as plt
import numpy as np

moves = "ASDS"
tile_nums = []
result_list = []
threshold = 0
n = 10000
start = time.time()

avg_num_moves = 0
for i in range(1, n + 1):
    if i % 1000 == 0:
        print(i)
    result = simulate(moves) #result = (num_moves, best_tile, best_coods, board, flag)
    result_list.append(result[1])
    avg_num_moves += result[0]
    if result[1] == 8:
        print(" ")
        print("------------------------------------")
        print(f"|  Bad Board in Game {i}:")
        print("------------------------------------")
        print(result[3])
        print(" ")
    if result[1] > threshold:
        print(" ")
        print("------------------------------------")
        print(f"| New Best {result[1]} found in Game {i} in {result[0]} moves")
        print(" ")
        print(result[3])
        print("------------------------------------")
        threshold = result[1]
        print(" ")
    tile_nums.append(result[1])
end = time.time()

taken = end - start
minutes = math.floor(taken / 60)
seconds = math.floor(taken % 60)
avg_num_moves = math.ceil(avg_num_moves / n)

print("------------------------------------")
print(f"| Time taken = {minutes} minutes {seconds} seconds")
print("------------------------------------")
print(" ")
print("------------------------------------")
print(f"| Average number of moves = {avg_num_moves}")
print("------------------------------------")



freq_dict = count_freqs(tile_nums)
highest = max(tile_nums)

print(" ")
print("------------------------------------")
print("|    Best Tile   :    Frequency    ")
print("|                                  ")
freq_dict = dict(sorted(freq_dict.items()))
for key in freq_dict:
    print(f"|       {key}               {freq_dict[key]}")
print("|                                  ")
print("------------------------------------")

print(" ")
print(f"Best Tile Value Found {highest}")

#plotting code
games = list(range(1, n + 1))
best_tiles = result_list
plt.figure(figsize=(12,6))
plt.plot(games, best_tiles, linewidth=1)
plt.xlabel("Game Number")
plt.ylabel("Best Tile Achieved")
plt.title(f"Best Tile vs Game Number over {n} Games")
plt.yscale("log", base=2)
max_tile = max(best_tiles)
powers = [2**k for k in range(1, int(np.log2(max_tile)) + 1)]
plt.yticks(powers, powers)  # tick positions + labels
plt.grid(alpha=0.3)
plt.show()