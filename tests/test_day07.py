from python.day07 import get_num_bag_colours_containing_shiny_gold_bag, get_number_of_bags_shiny_gold_bag_contains
import os


def test_get_num_bag_colours_containing_shiny_gold_bag():
    test_input_file = os.path.join("test_input", "day07.txt")
    assert get_num_bag_colours_containing_shiny_gold_bag(test_input_file) == 4


def test_get_number_of_bags_shiny_gold_bag_contains():
    test_input_file = os.path.join("test_input", "day07.txt")
    assert get_number_of_bags_shiny_gold_bag_contains(test_input_file) == 32
