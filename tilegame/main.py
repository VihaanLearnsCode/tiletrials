from .state import update_board, check_end, validSequence
from .create import generate
from .stats import maxTile, statistics


def simulate(moves: str):
    
    board = generate()
    print(board)
    
    i = 0
    best_tile = 0
    best_coods = (-1, -1)

    if not validSequence(moves):
        return moves, best_tile, best_coods, board, 2
    
    while(i < 1000): #loop until 2048 is found or 1000 moves have been played or 'game over'
        for move in moves:
            best_tile, best_coods = maxTile(board)
            if check_end(board):
                return moves, best_tile, best_coods, board, 1
            if best_tile >= 2048:
                return moves, best_tile, best_coods, board, 0
            update_board(move)
        i += 1

    return moves, best_tile, best_coods, board, 1

def main(moves):
    result = simulate(moves) #result = (moves, best_tile, best_coods, board, flag)
    if result[4] == 2:
        print("Invalid Sequence, please try again")
        return 1
    
    elif result[4] == 1:
        print("Game Over")
    else:
        print("You Won!!")
    print(f"Best Tile Found{result[0]}")
    statistics(*result)
    return 1