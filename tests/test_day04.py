from python.day04 import count_valid_passports, count_valid_passports_part_two
import os


def test_count_valid_passports():
    test_input_file = os.path.join("test_input", "day04.txt")
    assert count_valid_passports(test_input_file) == 2


def test_count_valid_passports_part_two():
    test_input_file = os.path.join("test_input", "day04_part_two.txt")
    assert count_valid_passports_part_two(test_input_file) == 4
