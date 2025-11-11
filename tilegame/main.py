from .state import update_board, check_end, validSequence
from .create import generate
from .stats import maxTile, statistics


def simulate(moves: str):
    
    board = generate()

    i = 0
    best_tile = 0
    best_coods = (-1, -1)
    if not validSequence(moves):
        return moves, best_tile, best_coods, board
    
    while(i < 1000): #loop until 2048 is found or 1000 moves have been played or 'game over'
        for move in moves:
            best_tile, best_coods = maxTile(board)
            if check_end(board, move) or best_tile >= 2048:
                return moves, best_tile, best_coods, board
            update_board(move)
        i += 1

    return moves, best_tile, best_coods, board

def main():
    result = simulate() #result = (moves, best_tile, best_coods, board)
    print(f"Best Tile Found{result[0]}")
    statistics(*result)
    return 1