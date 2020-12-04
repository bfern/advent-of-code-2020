def count_number_of_trees_encountered(forest: list) -> int:
    traversing = True
    num_trees_encountered = 0
    current_loc = [0, 0]
    while traversing:
        current_loc = go_to_next_loc(current_loc)
        if is_valid_location(current_loc, forest):
            if is_tree(current_loc, forest):
                num_trees_encountered += 1
        else:
            traversing = False
    return num_trees_encountered


def go_to_next_loc(current_loc: list) -> list:
    return [current_loc[0] + 3, current_loc[1] + 1]


def is_valid_location(current_loc: list, forest: list) -> bool:
    return current_loc[1] < len(forest)


def is_tree(current_loc: list, forest: list) -> bool:
    row = list(forest[current_loc[1]])
    return row[current_loc[0] % len(row)] == "#"
