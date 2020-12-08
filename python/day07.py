def get_num_bag_colours_containing_shiny_gold_bag(file: str) -> int:
    with open(file) as f:
        rules = f.read().split("\n")
    prev_possible_bag_colours = []
    possible_bag_colours = get_bag_colours_containing_specific_colour(rules, "shiny gold")
    while prev_possible_bag_colours != possible_bag_colours:
        prev_possible_bag_colours = possible_bag_colours
        for colour in possible_bag_colours:
            bag_colours = get_bag_colours_containing_specific_colour(rules, colour)
            possible_bag_colours = list(set(possible_bag_colours + bag_colours))
    return len(possible_bag_colours)


def get_bag_colours_containing_specific_colour(rules: list, colour: str) -> list:
    bag_colours = []
    for rule in rules:
        bag = get_bag(rule)
        bag_contents = get_bag_contents(rule)
        if colour in bag_contents:
            bag_colours.append(bag)
    return bag_colours


def get_bag(rule: str) -> str:
    return " ".join(rule.split(" ")[:2])


def get_bag_contents(rule: str) -> list:
    bag_contents_raw = rule.split(" contain ")[1].split(", ")
    if bag_contents_raw == ['no other bags.']:
        return []
    bag_contents = []
    for b in bag_contents_raw:
        b_manipulated = " ".join(b[2:].split(" ")[:2])
        bag_contents.append(b_manipulated)
    return bag_contents
