from python.day05 import get_seat_id_from_boarding_pass


def test_get_seat_id_from_boarding_pass():
    assert get_seat_id_from_boarding_pass("FBFBBFFRLR") == 357
    assert get_seat_id_from_boarding_pass("BFFFBBFRRR") == 567
    assert get_seat_id_from_boarding_pass("FFFBBBFRRR") == 119
    assert get_seat_id_from_boarding_pass("BBFFBBFRLL") == 820
