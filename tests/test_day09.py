import os
from python.day09 import find_first_invalid_number

def test_find_first_invalid_number():
    test_input_file = os.path.join("test_input", "day09.txt")
    assert find_first_invalid_number(test_input_file, 5) == 127
