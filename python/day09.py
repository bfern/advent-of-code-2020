def find_first_invalid_number(file: str, preamble_length: int=25) -> int:
    numbers = read_file_as_list(file)
    for i in range(preamble_length, len(numbers)):
        if number_is_invalid(numbers[i], numbers[(i - preamble_length):i]):
            return numbers[i]
    return 0

def read_file_as_list(file: str) -> list:
    with open(file) as f:
        lines = list(map(int, f.read().split("\n")))
    return lines

def number_is_invalid(number: int, prev_numbers: list) -> bool:
    for i in range(len(prev_numbers)):
        for j in range(i+1, len(prev_numbers)):
            if prev_numbers[i] + prev_numbers[j] == number:
                return False
    return True

def find_sum_smallest_and_largest_contiguous_range(file: str, preamble_length: int=25) -> int:
    numbers = read_file_as_list(file)
    first_invalid_number = find_first_invalid_number(file, preamble_length)
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if sum(numbers[i:(j+1)]) == first_invalid_number:
                return min(numbers[i:(j+1)]) + max(numbers[i:(j+1)])
    return -1
