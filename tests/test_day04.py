from python.day04 import count_valid_passports
import os


def test_count_valid_passports():
    test_input_file = os.path.join("test_input", "day04.txt")
    assert count_valid_passports(test_input_file) == 2
