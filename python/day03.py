def count_number_of_trees_encountered(forest: list, right: int=3, down: int=1) -> int:
    traversing = True
    num_trees_encountered = 0
    current_loc = [0, 0]
    while traversing:
        current_loc = go_to_next_loc(current_loc, right, down)
        if is_valid_location(current_loc, forest):
            if is_tree(current_loc, forest):
                num_trees_encountered += 1
        else:
            traversing = False
    return num_trees_encountered


def go_to_next_loc(current_loc: list, right: int=3, down: int=1) -> list:
    return [current_loc[0] + right, current_loc[1] + down]


def is_valid_location(current_loc: list, forest: list) -> bool:
    return current_loc[1] < len(forest)


def is_tree(current_loc: list, forest: list) -> bool:
    row = list(forest[current_loc[1]])
    return row[current_loc[0] % len(row)] == "#"


def count_number_of_trees_encountered_part_two(forest: list) -> int:
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1,2]]
    total_trees_encountered = 1
    for slope in slopes:
        total_trees_encountered *= count_number_of_trees_encountered(forest, slope[0], slope[1])
    return total_trees_encountered
