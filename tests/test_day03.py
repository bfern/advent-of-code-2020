from python.day03 import count_number_of_trees_encountered


def test_count_number_of_trees_encountered():
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
    assert count_number_of_trees_encountered(my_list) == 7
