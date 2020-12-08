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


def get_contents_of_bag(bag: str, rules: list) -> list:
    rule = get_rule_for_bag(bag, rules)
    return get_bag_contents(rule)


def get_rule_for_bag(bag: str, rules: list) -> str:    
    for rule in rules:
        if get_bag(rule) == bag:
            return rule
    return None


def get_number_of_bags_shiny_gold_bag_contains(file: str) -> list:
    with open(file) as f:
        rules = f.read().split("\n")
    return get_number_of_bags_inside("shiny gold", rules) - 1


def get_number_of_bags_inside(bag, rules) -> int:
    contents_of_bag = get_contents_of_bag(bag, rules)
    number_of_bags_inside = 1
    for this_bag in contents_of_bag:
        number_of_bags_inside += get_size_of_bag(bag, this_bag, rules) * get_number_of_bags_inside(this_bag, rules)
    return number_of_bags_inside


def get_size_of_bag(bag: str, this_bag: str, rules: list) -> int:
    rule = get_rule_for_bag(bag, rules)
    return int(rule.split(this_bag)[0].split(" ")[-2])