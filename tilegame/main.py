from .state import update_board, check_end, validSequence, spawn_tile
from .create import generate
from .stats import maxTile, statistics
import numpy as np

def least_used(s):
    chars = ["W", "A", "S", "D"]
    counts = {c: s.count(c) for c in chars}
    return min(counts, key=counts.get)

def simulate(moves: str):
    
    board = generate()
    # print(board)

    i = 0
    best_tile = 0
    best_coods = (-1, -1)

    if not validSequence(moves):
        return moves, best_tile, best_coods, board, 2
    
    least = least_used(moves) 
    done = 0
    flag = 2
    length = len(moves)

    while(i < 2000): #loop until 2048 is found or 10000 moves have been played or 'game over'
        for move in moves:
            best_tile, best_coods = maxTile(board)
            if check_end(board):
                done = 1
                flag = 1
                break
            if best_tile >= 2048:
                done = 1
                flag = 0
            board = update_board(board, move)
            board = spawn_tile(board)
        i += 1
        if done:
            break

    num_moves = i*len(moves)
    return num_moves, best_tile, best_coods, board, flag

def main(moves):
    result = simulate(moves) #result = (moves, best_tile, best_coods, board, flag)
    if result[4] == 2:
        print("Invalid Sequence, please try again")
        return 1
    
    elif result[4] == 1:
        print("Game Over")
    else:
        print("You Won!!")
    print(f"Best Tile Found{result[1]}")
    statistics(*result)
    return 1