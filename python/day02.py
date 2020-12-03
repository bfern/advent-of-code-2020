def count_valid_passwords(passwords: list) -> int:
    num_valid_passwords = 0
    for password in passwords:
        lower_bound = get_lower_bound(password)
        upper_bound = get_upper_bound(password)
        letter = get_letter(password)
        word = get_word(password)
        num_occurrences = word.count(letter)
        if num_occurrences >= lower_bound and num_occurrences <= upper_bound:
            num_valid_passwords += 1
    return num_valid_passwords


def get_lower_bound(password: str) -> int:
    return int(password.split("-")[0])


def get_upper_bound(password: str) -> int:
    return int(password.split("-")[1].split(" ")[0])


def get_letter(password: str) -> str:
    return password.split(":")[0][-1]


def get_word(password: str) -> str:
    return password.split(":")[1][1:]
