from python.day12_2022 import get_current_possible_moves, get_fewest_steps, get_altitude, get_current_possible_moves, get_start_index, get_end_index, reduce_route
import os


def test_get_fewest_steps():
    test_input_file = os.path.join("test_input", "day12_2022.txt")
    assert get_fewest_steps(test_input_file) == 31



def test_get_altitude():
    with open(os.path.join("test_input", "day12_2022.txt")) as f:
        l = f.read().split("\n")
        board = []
        for val in l:
            board.append(list(val))
    assert get_altitude((0,1), board) == 1
    assert get_altitude((0,0), board) == 1
    assert get_altitude((2,5), board) == 26
    assert get_altitude((4,2), board) == 4


def test_get_current_possible_moves():
    with open(os.path.join("test_input", "day12_2022.txt")) as f:
        l = f.read().split("\n")
        board = []
        for val in l:
            board.append(list(val))
    assert get_current_possible_moves((0,0), board) == {(0,1), (1,0)}
    assert get_current_possible_moves((1,1), board) == {(0,1), (1,0), (1,2), (2,1)}
    assert get_current_possible_moves((3,4), board) == {(3,5), (3,3), (4,4)}


def test_get_start_index():
    with open(os.path.join("test_input", "day12_2022.txt")) as f:
        l = f.read().split("\n")
        board = []
        for val in l:
            board.append(list(val))
    assert get_start_index(board) == (0,0)


def test_get_end_index():
    with open(os.path.join("test_input", "day12_2022.txt")) as f:
        l = f.read().split("\n")
        board = []
        for val in l:
            board.append(list(val))
    assert get_end_index(board) == (2,5)


def test_reduce_route():
    assert reduce_route([(0,0), (0,1), (1,1), (1,0), (0,0), (0,1)]) == [(0,0), (0,1)]
    assert reduce_route([(0,0), (1,0), (0,0), (0,1)]) == [(0,0), (0,1)]