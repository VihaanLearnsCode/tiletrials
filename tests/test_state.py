from tilegame.state import *
import numpy as np

def test_update_boardW():
    board = np.array([[2, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0]])
    board = update_board(board.copy(), "W")
    assert board.tolist() == np.array([[4, 0, 0, 0], [4, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]).tolist()

def test_update_boardA():
    board = np.array([[2, 2, 2, 2], [2, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0]])
    board = update_board(board.copy(), "A")
    assert board.tolist() == np.array([[4, 4, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0]]).tolist()

def test_update_boardS():
    board = np.array([[2, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0]])
    board = update_board(board.copy(), "S")
    assert board.tolist() == np.array([[0, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 0], [4, 0, 0, 0]]).tolist()

def test_update_boardD():
    board = np.array([[2, 2, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0]])
    board = update_board(board.copy(), "D")
    assert board.tolist() == np.array([[0, 0, 0, 4], [0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 2]]).tolist()

def test_check_game_over():
    board = np.array([[2, 4, 2, 4], [4, 2, 4, 2], [2, 4, 2, 4], [4, 2, 4, 2]])
    assert check_end(board) == True