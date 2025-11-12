import numpy as np
from .state import spawn_tile

def init_board():
    board = np.zeros((4, 4), dtype=int)
    return board

def generate():
    board = init_board()
    spawn_tile(board)
    spawn_tile(board)
    return board 