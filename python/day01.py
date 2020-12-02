import numpy as np

def fix_expense_report(report: list) -> int:
    report_subtract_2020 = 2020 - np.array(report)
    for val in report_subtract_2020:
        if val in report:
            return val * (2020 - val)
    return 0

def fix_expense_report_part_two(report: list) _. int:
    return 0
