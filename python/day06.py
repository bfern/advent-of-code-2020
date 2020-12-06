def sum_of_counts(file: str) -> int:
    with open(file) as f:
        input = f.read()
    groups = input.split("\n\n")
    sum_of_counts = 0
    for group in groups:
        count = get_count(group.replace("\n", ""))
        sum_of_counts += count
    return sum_of_counts


def get_count(answers: str) -> int:
    return len(set(answers))
