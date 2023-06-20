def get_number_of_visible_trees(file: str) -> int:
    with open(file) as f:
        input = f.read().split("\n")
    forest = []
    for row in input:
        forest.append(list(row))
    number_of_visible_trees = 0
    for i in range(len(forest)):
        for j in range(len(forest[i])):
            if visible_tree(forest, j, i):
                number_of_visible_trees += 1
    return number_of_visible_trees


def visible_tree(forest, row, col):
    if visible_from_left(forest, row, col):
        return True
    if visible_from_right(forest, row, col):
        return True
    if visible_from_top(forest, row, col):
        return True
    if visible_from_bottom(forest, row, col):
        return True
    return False

def visible_from_left(forest, row, col):
    i = col-1
    max_height = -1
    while i > -1:
        tree_height = int(forest[row][i])
        i -= 1
        if tree_height > max_height:
            max_height = tree_height
    return int(forest[row][col]) > max_height

def visible_from_right(forest, row, col):
    i = col+1
    max_height = -1
    while i < len(forest[row]):
        tree_height = int(forest[row][i])
        i += 1
        if tree_height > max_height:
            max_height = tree_height
    return int(forest[row][col]) > max_height

def visible_from_top(forest, row, col):
    i = row-1
    max_height = -1
    while i > -1:
        tree_height = int(forest[i][col])
        i -= 1
        if tree_height > max_height:
            max_height = tree_height
    return int(forest[row][col]) > max_height

def visible_from_bottom(forest, row, col):
    i = row+1
    max_height = -1
    while i < len(forest):
        tree_height = int(forest[i][col])
        i += 1
        if tree_height > max_height:
            max_height = tree_height
    return int(forest[row][col]) > max_height