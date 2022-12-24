import numpy as np
import random
from collections import Counter


def get_fewest_steps(file:str, random_seed:int) -> int:
    random.seed(random_seed)
    with open(file) as f:
        l = f.read().split("\n")
        board = []
        for val in l:
            board.append(list(val))
    start_index = get_start_index(board)
    end_index = get_end_index(board)
    route = []
    prev_index = start_index
    while prev_index != end_index:
        current_possible_moves = get_current_possible_moves(prev_index, board)
        prev_index = list(random.choice(list(current_possible_moves)))
        route.append(prev_index)
        route = reduce_route(route)
        if len(route) >= 1000:
            print(route)
            break
    return len(route)


def get_current_possible_moves(current_loc:list, board:list) -> list:
    current_alt = get_altitude(current_loc, board)
    current_possible_moves = []
    if get_altitude([current_loc[0]-1, current_loc[1]], board) <= current_alt+1 and  get_altitude([current_loc[0]-1, current_loc[1]], board) > 0:
        current_possible_moves.append([current_loc[0]-1, current_loc[1]])
    if get_altitude([current_loc[0]+1, current_loc[1]], board) <= current_alt+1 and get_altitude([current_loc[0]+1, current_loc[1]], board) > 0:
        current_possible_moves.append([current_loc[0]+1, current_loc[1]])
    if get_altitude([current_loc[0], current_loc[1]-1], board) <= current_alt+1 and get_altitude([current_loc[0], current_loc[1]-1], board) > 0:
        current_possible_moves.append([current_loc[0], current_loc[1]-1])
    if get_altitude([current_loc[0], current_loc[1]+1], board) <= current_alt+1 and get_altitude([current_loc[0], current_loc[1]+1], board) > 0:
        current_possible_moves.append([current_loc[0], current_loc[1]+1])
    return set(tuple(x) for x in current_possible_moves)


def get_altitude(loc:list, board:list) -> int:
    board_dim = np.shape(np.array(board))
    if loc[0] <= -1 or loc[0] >= board_dim[0] or loc[1] <= -1 or loc[1] >= board_dim[1]:
        return 0
    if board[loc[0]][loc[1]] == "S":
        return 1
    if board[loc[0]][loc[1]] == "E":
        return 26
    return ord(board[loc[0]][loc[1]]) - 96


def get_start_index(board:list) -> list:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "S":
                return [i,j]
    return [-1,-1]


def get_end_index(board:list) -> list:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "E":
                return [i,j]    
    return [-1,-1]


def reduce_route(route: list) -> list:
    route_as_set = set(tuple(x) for x in route)
    path_counts = dict((x,route.count(list(x))) for x in route_as_set)
    cyclic_index = [-1,-1]
    for index in path_counts:
        if path_counts[index] >= 2:
            cyclic_index = list(index)
    if cyclic_index == [-1,-1]:
        return route
    cyclic_index_positions_in_path = [index for index in range(len(route)) if route[index] == cyclic_index]
    return route[0:cyclic_index_positions_in_path[0]] + route[cyclic_index_positions_in_path[1]:len(route)]