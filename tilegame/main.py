from .state import update_board, check_end
from .create import generate
from .stats import maxTile, statistics

def simulate(moves: str):
    board = generate()
    for move in moves:
        best_tile, best_coods = maxTile(board)
        if check_end(board, move) or best_tile == 2048:
            return moves, best_tile, best_coods, board
        update_board(move)

def main():
    result = simulate() #result = (moves, best_tile, best_coods, board)
    statistics(*result)
    return 1