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
