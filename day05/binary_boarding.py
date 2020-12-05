#!/usr/bin/env python3

import math
import sys
from operator import itemgetter


def boarding_pass_reader(filename):
    with open(filename) as file_object:
        return file_object.read().splitlines()


def _binary_search(path, lower, upper, maximum):
    row_min, row_max = 0, maximum
    for character in path:
        if character == lower:
            row_max -= math.floor((row_max - row_min) / 2)
        elif character == upper:
            row_min += math.floor((row_max - row_min) / 2)
    return row_min


def _decode_row(specification):
    return _binary_search(specification[:7], "F", "B", 128)


def _decode_column(specification):
    return _binary_search(specification[-3:], "L", "R", 8)


def decode_boarding_pass(specification):
    row = _decode_row(specification)
    column = _decode_column(specification)
    return {
        "specification": specification,
        "row": row,
        "column": column,
        "seat_id": (row * 8) + column,
    }


if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <input file>")
    sys.exit(1)

filename = str(sys.argv[1])
boarding_passes = [
    decode_boarding_pass(x) for x in boarding_pass_reader(filename)
]
number_boarding_passes = len(boarding_passes)
maximum_seat_id = max(boarding_passes, key=itemgetter("seat_id"))

print(
    f"In file '{filename}' there were {number_boarding_passes} "
    f"boarding passes, and the highest Seat ID was {maximum_seat_id}."
)


def _visualise_aeroplane(boarding_passes):
    occupancy = [["." for x in range(8)] for y in range(128)]
    for boarding_pass in boarding_passes:
        occupancy[boarding_pass["row"]][boarding_pass["column"]] = "#"
    for row, line in enumerate(occupancy):
        print(f"{row:03} " + "".join(line))


_visualise_aeroplane(boarding_passes)
