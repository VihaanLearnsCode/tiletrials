import numpy as np

def statistics():
    return 1

def maxTile(board):
    max_val = np.max(board)
    coods = [tuple(xy) for xy in np.argwhere(board == max_val)]
    return max_val, coods



