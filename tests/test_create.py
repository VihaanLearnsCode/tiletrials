import numpy as np
from tilegame.state import spawn_tile
from tilegame.create import *

def test_last_tile():
    board = np.ones((4, 4), dtype=int)
    board[0][0] = 0
    new_board = spawn_tile(board.copy())
    assert new_board.tolist() != board.tolist()
