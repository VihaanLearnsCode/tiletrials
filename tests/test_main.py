from tilegame.main import *
from tilegame.stats import count_freqs
import time 

moves = "ASDSDS"
tile_nums = []

threshold = 0

start = time.time()
for i in range(10000):
    if i % 1000 == 0:
        print(i)
    result = simulate(moves) #result = (moves, best_tile, best_coods, board, flag)
    if result[1] == 8:
        print(" ")
        print(f"Bad Board in Game {i}:")
        print(result[3])
        print(" ")
    if result[1] > threshold:
        print(" ")
        print(f"New High Board found in Game {i} with tile {result[1]} at {result[2]}:")
        print(result[3])
        threshold = result[1]
        print(" ")
    tile_nums.append(result[1])
end = time.time()

taken = end - start
minutes = taken / 60
seconds = taken % 60
print(f"Time taken = {minutes} minutes {seconds} seconds")


freq_dict = count_freqs(tile_nums)
highest = max(tile_nums)

print(" ")
print("------------------------------------")
freq_dict = dict(sorted(freq_dict.items()))
for key in freq_dict:
    print(f"{key} : {freq_dict[key]}")

print(" ")
print(f"Best Tile Value Found {highest}")
