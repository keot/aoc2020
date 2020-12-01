#!/usr/bin/env python3

import sys
from functools import reduce
from itertools import permutations

DEMO_INPUT = """
1721
979
366
299
675
1456
"""


def integer_file_reader(filename):
    with open(filename) as file_object:
        return [int(x) for x in file_object]


def expense_report_lookup(data=DEMO_INPUT, target=2020, entries=2):
    for pair in permutations(data, entries):
        if sum(pair) == target:
            yield pair


if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} <input file> <target number> <entries to sum>")
    sys.exit(1)

filename = str(sys.argv[1])
target = int(sys.argv[2])
entries = int(sys.argv[3])

try:
    first_pair = next(
        expense_report_lookup(integer_file_reader(filename), target, entries)
    )
except StopIteration:
    print(f"Unable to find a set of {entries} that sum to {target} in" f" {filename}!")
    sys.exit(1)

first_product = reduce(lambda x, y: x * y, first_pair)
print(
    f"The first pair that sums to {target} in {filename} was {first_pair},"
    f" which multiplied equals {first_product:,}."
)
