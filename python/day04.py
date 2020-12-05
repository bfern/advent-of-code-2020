def count_valid_passports(file: str) -> int:
    passports = convert_file_to_passports(file)
    num_valid_passports = 0
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for passport in passports:
        if passport_has_required_fields(passport, required_fields):
            num_valid_passports += 1
    return num_valid_passports


def convert_file_to_passports(file: str) -> list:
    with open(file) as f:
        input = f.read()
    input = input.split("\n\n")
    passports = []
    for val in input:
        passport = {}
        for v in val.replace("\n", " ").split(" "):
            passport[v.split(":")[0]] = v.split(":")[1]
        passports.append(passport)
    return passports


def passport_has_required_fields(passport: dict, required_fields: list) -> bool:
    for field in required_fields:
        if field not in passport.keys():
            return False
    return True


def count_valid_passports_part_two(file: str) -> int:
    passports = convert_file_to_passports(file)
    num_valid_passports = 0
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for passport in passports:
        if passport_has_required_and_valid_fields(passport, required_fields):
            num_valid_passports += 1
    return num_valid_passports


def passport_has_required_and_valid_fields(passport: dict, required_fields) -> bool:
    for field in required_fields:
        if (field not in passport.keys()) or (not is_valid(field, passport.get(field))):
            return False
    return True


def is_valid(field, value):
    if field == "byr":
        return (int(value) >= 1920) and (int(value) <= 2002)
    if field == "iyr":
        return (int(value) >= 2010) and (int(value) <= 2020)
    if field == "eyr":
        return (int(value) >= 2020) and (int(value) <= 2030)
    if field == "hgt":
        start = value[:-2]
        end = value[-2:]
        if (not start.isdigit()) or (end.isdigit()) or (end[-2:] not in ["cm", "in"]):
            return False
        if end == "cm":
            return (int(start) >= 150) and (int(start) <= 193)
        else:
            return (int(start) >= 59) and (int(start) <= 76)
    if field == "hcl":
        if value[0] != "#":
            return False
        if len(value[1:]) != 6:
            return False
        for char in value[1:]:
            if char not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]:
                return False
        return True
    if field == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if field == "pid":
        if len(value) != 9:
            return False
        for char in value:
            if char not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                return False
        return True
    return False
