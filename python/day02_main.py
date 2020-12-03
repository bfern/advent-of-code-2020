from python.day02 import count_valid_passwords

with open("input/day02.txt") as f:
    input = f.readlines()
input = [x.strip() for x in input]
print(count_valid_passwords(input))
print(count_valid_passwords_part_two(input))