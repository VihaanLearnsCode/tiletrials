import numpy as np

from state import update_board, check_end

def generate() -> int[[]]:
    count = 0
    rand_x = np.randint()
    return

def simulate(moves: str) -> int:
    for move in moves:
        update_board(move)
        if check_end(board, move):
            return check_end
    
    return

def statistics():
    return

def main():
    generate()
    simulate()
    statistics()
    return 1