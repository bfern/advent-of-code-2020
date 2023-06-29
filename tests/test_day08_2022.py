from python.day08_2022 import get_number_of_visible_trees
import os


def test_get_number_of_visible_trees():
    test_input_file = os.path.join("test_input", "day08_2022.txt")
    assert get_number_of_visible_trees(test_input_file) == 21
