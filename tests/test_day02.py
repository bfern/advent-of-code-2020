from python.day02 import count_valid_passwords


def test_count_valid_passwords():
    assert count_valid_passwords(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]) == 2
