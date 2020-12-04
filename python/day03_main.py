from python.day03 import count_number_of_trees_encountered, count_number_of_trees_encountered_part_two

with open("input/day03.txt") as f:
    input = f.readlines()
input = [x.strip() for x in input]
print(count_number_of_trees_encountered(input))
print(count_number_of_trees_encountered_part_two(input))