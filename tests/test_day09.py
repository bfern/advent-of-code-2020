import os
from python.day09 import find_first_invalid_number, find_sum_smallest_and_largest_contiguous_range

def test_find_first_invalid_number():
    test_input_file = os.path.join("test_input", "day09.txt")
    assert find_first_invalid_number(test_input_file, 5) == 127
    
def test_find_sum_smallest_and_largest_contiguous_range():
    test_input_file = os.path.join("test_input", "day09.txt")
    assert find_sum_smallest_and_largest_contiguous_range(test_input_file, 5) == 62