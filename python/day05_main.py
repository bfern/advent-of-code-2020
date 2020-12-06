from python.day05 import get_seat_id_from_boarding_pass

with open("input/day05.txt") as f:
    input = f.readlines()
highest_seat_id = 0
for boarding_pass in input:
    seat_id = get_seat_id_from_boarding_pass(boarding_pass)
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id
print(highest_seat_id)
