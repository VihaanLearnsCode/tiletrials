import numpy as np

def update_board(board, move) -> bool:
    print(board)
    #decide transform based on move
    if move == 'W':
        board = np.rot90(board)
    elif move == 'S':
        board = np.rot90(board, k=-1)
    elif move == 'D':
        board = np.rot90(np.rot90(board))

    print(board)
    for i in range(4):
        board[i] = mergeLeft(board[i])

    print(board)
    #transforms back into original
    if move == 'W':
        board = np.rot90(board, k=-1)
    elif move == 'S':
        board = np.rot90(board)
    elif move == 'D':
        board = np.rot90(np.rot90(board))

    return board 

def try_move(board, move):
    new_board = update_board(board, move)
    valid_move = (board == new_board)
    return (valid_move, new_board)

def check_end(board):
    return not (try_move('W')[0] or try_move('S')[0] or try_move('A')[0] or try_move('D')[0]) 

def spawn_tile(board):
    i = 0
    vals = [2, 4]
    weights = [0.9, 0.1]

    empty = np.argwhere(board == 0)
    if empty.size == 0:
        return board
    
    i, j = empty[np.random.randint(0, len(empty))]
    board[i, j] = np.random.choice(vals, p=weights)
    return board #returns same board if no space available

def validSequence(moves: str):
    return set(moves) not in ('W', 'A', 'S', 'D') or len(moves) > 10

def compressLeft(row):
    compressed = [x for x in row if x != 0]
    while(len(compressed) < 4):
        compressed.append(0)
    compressed = np.array(compressed)
    return compressed

def mergeLeft(row):
    row = compressLeft(row.copy())
    for i in range(3):
        if row[i] == row[i + 1] and row[i] != 0:
            row[i] *= 2
            row[i + 1] = 0
            row = compressLeft(row)
            i += 1
    return row
