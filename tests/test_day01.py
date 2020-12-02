from python.day01 import fix_expense_report


def test_fix_expense_report():
    assert fix_expense_report([1721, 979, 366, 299, 675, 1456]) == 514579
