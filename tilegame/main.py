from state import update_board, check_end
from create import generate
from stats import maxTile

def simulate(board: int[[]], moves: str) -> int:
    board = generate()

    for move in moves:
        best_tile = maxTile(board)
        if check_end(board, move) or best_tile == 2048:
            return board
        update_board(move)



def main():
    generate()
    simulate(board, moves)
    return 1