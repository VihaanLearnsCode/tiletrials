import numpy as np

def update_board(board, move) -> bool:
    #decide transform based on move
    if move == 'A':
        board = np.rot90(board)
    elif move == 'S':
        board = np.rot90(np.rot90(board))
    elif move == 'D':
        board = np.rot90(board, k=-1)

    #moves up
    for row in range(1, 4):
        for col in range(4):
            
            #merges
            if board[row][col] == board[row - 1][col]:
                board[row - 1][col] = board[row][col] * 2
                board[row][col] = 0

            #compresses up
            if board[row - 1][col] == 0:
                board[row - 1][col] = board[row][col]
                board[row][col] = 0
            
            


    #transforms back into original
    if move == 'A':
        board = np.rot90(board, k=-1)
    elif move == 'S':
        board = np.rot90(np.rot90(board))
    elif move == 'D':
        board = np.rot90(board)

    return board #no change or change?

def try_move(board, move):
    return (True, board)

def check_end(board):
    return not (try_move('W') or try_move('W') or try_move('W') or try_move('W')) 

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