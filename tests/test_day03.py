from python.day03 import count_number_of_trees_encountered, count_number_of_trees_encountered_part_two


my_list = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#"
]

def test_count_number_of_trees_encountered():
    assert count_number_of_trees_encountered(my_list) == 7


def test_count_number_of_trees_encountered_part_two():
    assert count_number_of_trees_encountered_part_two(my_list) == 336
