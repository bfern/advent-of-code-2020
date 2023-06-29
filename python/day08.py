def get_accumulator_value_at_end_of_first_loop(file: str) -> int:
    instruction_list = read_file_as_list(file)
    accumulator = 0
    instruction_index = 0
    instruction_indexes_visited = []
    while instruction_index not in instruction_indexes_visited:
        instruction = instruction_list[instruction_index]
        operation  = get_operation(instruction)
        argument = get_argument(instruction)
        accumulator = adjust_accumulator_value(accumulator, operation, argument)
        instruction_indexes_visited.append(instruction_index)
        instruction_index = go_to_next_instruction(instruction_index, operation, argument)
    return accumulator

def read_file_as_list(file: str) -> list:
    with open(file) as f:
        lines = f.read().split("\n")
    return lines

def get_operation(instruction: str) -> str:
    return instruction[0:3]

def get_argument(instruction: str) -> int:
    return int(instruction[4:])

def adjust_accumulator_value(accumulator: int, operation: str, argument: int) -> int:
    if operation == "acc":
        return accumulator + argument
    return accumulator

def go_to_next_instruction(instruction_index: int, operation: str, argument: int) -> int:
    if operation == "jmp":
        return instruction_index + argument
    return instruction_index + 1

