from python.day01 import fix_expense_report

with open("input/day01.txt") as f:
    input = f.readlines()
input = [int(x.strip()) for x in input]
print(fix_expense_report(input))