from tilegame.main import *

moves = "ASDSASDSDS"
best = 0
best_result = None
for i in range(10000):
    result = simulate(moves) #result = (moves, best_tile, best_coods, board, flag)
    if best < result[1]:
        best_result = result

print(" ")

if result[4] == 2:
    print("Invalid Sequence, please try again")
elif result[4] == 1:
    print("Game Over")
else:
    print("You Won!!")

print(f"Best Tile Value Found {result[1]}")
