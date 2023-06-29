from python.day08 import get_accumulator_value_at_end_of_first_loop
import os

def test_get_accumulator_value_at_end_of_first_loop():
    test_input_file = os.path.join("test_input", "day08.txt")
    assert get_accumulator_value_at_end_of_first_loop(test_input_file) == 5