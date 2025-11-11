import numpy as np
from tilegame.stats import maxTile

def test_find_maxTile():
    board = np.zeros((4, 4), dtype=int)
    board[2][1] = 1
    max_val, coods = maxTile(board)
    assert max_val == 1
    assert coods == [(2, 1)]
