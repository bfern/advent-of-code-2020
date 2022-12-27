import numpy as np
from collections import Counter


def get_fewest_steps(file:str) -> int:
    with open(file) as f:
        l = f.read().split("\n")
        board = []
        for val in l:
            board.append(list(val))
    start_index = get_start_index(board)
    end_index = get_end_index(board)
    route = [start_index]
    already_travelled_to_indexes = [start_index]
    prev_index = start_index
    while prev_index != end_index:
        current_possible_moves = get_current_possible_moves(prev_index, board, already_travelled_to_indexes)
        print(f"current possible moves: {current_possible_moves}")
        prev_index = get_move_with_highest_altitude(current_possible_moves, board)
        already_travelled_to_indexes.append(prev_index)
        route.append(prev_index)
        print(f"route: {route}")
        route = reduce_route(route)
        print(f"reduced route: {route}")
        print("\n")
        if len(route) >= 1000:
            print(route)
            break
    return len(route)-1


def get_current_possible_moves(current_loc:tuple, board:list, route:list=[]) -> list:
    current_alt = get_altitude(current_loc, board)
    current_possible_moves = []
    if get_altitude((current_loc[0]-1, current_loc[1]), board) <= current_alt+1 and get_altitude((current_loc[0]-1, current_loc[1]), board) > 0 and (current_loc[0]-1, current_loc[1]) not in route:
        current_possible_moves.append((current_loc[0]-1, current_loc[1]))
    if get_altitude((current_loc[0]+1, current_loc[1]), board) <= current_alt+1 and get_altitude((current_loc[0]+1, current_loc[1]), board) > 0 and (current_loc[0]+1, current_loc[1]) not in route:
        current_possible_moves.append((current_loc[0]+1, current_loc[1]))
    if get_altitude((current_loc[0], current_loc[1]-1), board) <= current_alt+1 and get_altitude((current_loc[0], current_loc[1]-1), board) > 0 and (current_loc[0], current_loc[1]-1) not in route:
        current_possible_moves.append((current_loc[0], current_loc[1]-1))
    if get_altitude((current_loc[0], current_loc[1]+1), board) <= current_alt+1 and get_altitude((current_loc[0], current_loc[1]+1), board) > 0 and (current_loc[0], current_loc[1]+1) not in route:
        current_possible_moves.append((current_loc[0], current_loc[1]+1))
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
                return (i,j)
    return (-1,-1)


def get_end_index(board:list) -> list:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "E":
                return (i,j)
    return (-1,-1)


def reduce_route(route: list) -> list:
    reduced_route = route
    path_counts = {}
    for x in reduced_route:
        if tuple(x) not in path_counts:
            path_counts[tuple(x)] = 1
        else:
            path_counts[tuple(x)] += 1
    while max(path_counts.values()) > 1:
        for index in path_counts:
            if path_counts[index] > 1:
                cyclic_index = index
                break
        cyclic_index_positions_in_path = [index for index in range(len(reduced_route)) if reduced_route[index] == cyclic_index]
        print(cyclic_index)
        print(cyclic_index_positions_in_path)
        reduced_route = reduced_route[0:cyclic_index_positions_in_path[0]] + reduced_route[cyclic_index_positions_in_path[-1]:len(reduced_route)]
        path_counts = {}
        for x in reduced_route:
            if tuple(x) not in path_counts:
                path_counts[tuple(x)] = 1
            else:
                path_counts[tuple(x)] += 1
    return reduced_route


def get_move_with_highest_altitude(moves: list, board:list) -> tuple:
    highest_altitude = 0
    move_with_highest_altitude = (-1,-1)
    for move in moves:
        altitude = get_altitude(move, board)
        if altitude > highest_altitude:
            highest_altitude = altitude
            move_with_highest_altitude = move
    return move_with_highest_altitude

