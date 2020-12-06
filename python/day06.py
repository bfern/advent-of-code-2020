def sum_of_counts(file: str) -> int:
    with open(file) as f:
        input = f.read()
    groups = input.split("\n\n")
    sum_of_counts = 0
    for group in groups:
        count = get_count(group)
        sum_of_counts += count
    return sum_of_counts


def get_count(answers: str) -> int:
    return len(set(answers.replace("\n", "")))


def sum_of_counts_part_two(file: str) -> int:
    with open(file) as f:
        input = f.read()
    groups = input.split("\n\n")
    sum_of_counts = 0
    for group in groups:
        count = get_count_part_two(group)
        sum_of_counts += count
    return sum_of_counts


def get_count_part_two(answers: str) -> int:
    answered_by_all = None
    for answer in answers.split("\n"):
        if answered_by_all is None:
            answered_by_all = answer
        else:
            answered_by_all = "".join(set(answered_by_all).intersection(answer))
    return len(answered_by_all)
