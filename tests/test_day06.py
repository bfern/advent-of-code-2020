from python.day06 import sum_of_counts
import os


def test_sum_of_counts():
    test_input_file = os.path.join("test_input", "day06.txt")
    assert sum_of_counts(test_input_file) == 11
