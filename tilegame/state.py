import numpy as np

def update_board(board, move) -> bool:
    #try move
    new_board = board.copy()
    for row in new_board:
        #do something based on direction
        print("remove this line")
    return (new_board == board) #no change or change?

def try_move(board, move):
    return (True, board)

def check_end(board):
    return not (try_move('W') or try_move('W') or try_move('W') or try_move('W')) 

def spawn_tile(board):
    i = 0
    vals = [2, 4]
    weights = [0.9, 0.1]

    empty = np.argwhere(board == 0)

    print(empty)
    if empty.size == 0:
        return board
    
    i, j = empty[np.random.randint(0, len(empty))]
    board[i, j] = np.random.choice(vals, p=weights)
    
    return board #returns same board if no space available
