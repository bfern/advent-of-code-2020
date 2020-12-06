def get_seat_id_from_boarding_pass(boarding_pass: str) -> int:
    row = get_row_from_boarding_pass(boarding_pass)
    column = get_column_from_boarding_pass(boarding_pass)
    return row * 8 + column


def get_row_from_boarding_pass(boarding_pass: str) -> int:
    boarding_pass_as_binary = ""
    for char in boarding_pass[:7]:
        if char == "F":
            boarding_pass_as_binary += "0"
        else:
            boarding_pass_as_binary += "1"
    return int(boarding_pass_as_binary, 2)

def get_column_from_boarding_pass(boarding_pass: str) -> int:
    boarding_pass_as_binary = ""
    for char in boarding_pass[7:]:
        if char == "L":
            boarding_pass_as_binary += "0"
        else:
            boarding_pass_as_binary += "1"
    return int(boarding_pass_as_binary, 2)
