#!/usr/bin/env python3

import sys

required_fields = (
    "byr",  # Birth Year
    "iyr",  # Issue Year
    "eyr",  # Expiration Year
    "hgt",  # Height
    "hcl",  # Hair Color
    "ecl",  # Eye Color
    "pid",  # Passport ID
    "cid",  # Country ID
)


def batch_reader(filename):
    with open(filename) as file_object:
        return [
            dict(f.split(":") for f in rp)
            for rp in [p.split() for p in file_object.read().split("\n\n")]
        ]


if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <input file>")
    sys.exit(1)

filename = str(sys.argv[1])
passports = batch_reader(filename)

criteria = tuple(filter(lambda f: f != "cid", required_fields))

total_passports = len(passports)
passports_with_required_fields = list(
    filter(lambda p: all(c in p for c in criteria), passports)
)
count_passports_with_required_fields = len(passports_with_required_fields)

print(
    f"There are {count_passports_with_required_fields} "
    f"passports out of {total_passports} with all the required fields "
    f"present: {criteria}."
)


class PassportValidationError(Exception):
    pass


class PassportValidator:
    def _byr(
        self, value
    ):  # (Birth Year) - four digits; at least 1920 and at most 2002.
        if int(value) < 1920 or int(value) > 2002:
            raise PassportValidationError

    def _iyr(
        self, value
    ):  # (Issue Year) - four digits; at least 2010 and at most 2020.
        if int(value) < 2010 or int(value) > 2020:
            raise PassportValidationError

    def _eyr(
        self, value
    ):  # (Expiration Year) - four digits; at least 2020 and at most 2030.
        if int(value) < 2020 or int(value) > 2030:
            raise PassportValidationError

    def _hgt(self, value):  # (Height) - a number followed by either cm or in:
        unit = value[-2:]
        number = int(value[:-2])
        if unit not in ("cm", "in"):
            raise PassportValidationError
        if unit == "cm" and (number < 150 or number > 193):
            # If cm, the number must be at least 150 and at most 193.
            raise PassportValidationError
        elif unit == "in" and (number < 59 or number > 76):
            # If in, the number must be at least 59 and at most 76.
            raise PassportValidationError

    def _hcl(
        self, value
    ):  # (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if value[0] != "#" or len(value) != 7:
            raise PassportValidationError
        for character in value[1:]:
            if character not in (c for c in "0123456789abcdef"):
                raise PassportValidationError

    def _ecl(
        self, value
    ):  # (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if value not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
            raise PassportValidationError

    def _pid(
        self, value
    ):  # (Passport ID) - a nine-digit number, including leading zeroes.
        if len(value) != 9:
            raise PassportValidationError
        for character in value:
            if character not in (c for c in "0123456789"):
                raise PassportValidationError

    def _cid(self, value):  # (Country ID) - ignored, missing or not.
        pass

    def valid(self, passport):
        try:
            self._byr(passport["byr"])
            self._iyr(passport["iyr"])
            self._eyr(passport["eyr"])
            self._hgt(passport["hgt"])
            self._hcl(passport["hcl"])
            self._ecl(passport["ecl"])
            self._pid(passport["pid"])
        except PassportValidationError:
            return False
        return True


validator = PassportValidator()
count_valid_passports = sum(
    validator.valid(passport) for passport in passports_with_required_fields
)

print(
    f"There are {count_valid_passports} passports with correct fields out of "
    f"{count_passports_with_required_fields} with all fields present."
)
