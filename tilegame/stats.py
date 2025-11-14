import numpy as np

def statistics():
    return 1

def maxTile(board):
    max_val = np.max(board)
    coods = [tuple(xy) for xy in np.argwhere(board == max_val)]
    return max_val, coods

def count_freqs(results):
    freq_dict = {}
    for result in results:
        if result in freq_dict.keys():
            freq_dict[result] += 1
        else:
            freq_dict.update({result:1})
    return freq_dict