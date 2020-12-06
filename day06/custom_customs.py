#!/usr/bin/env python3

import sys


def group_reader(filename):
    with open(filename) as file_object:
        return file_object.read().split("\n\n")


def unique_characters(characters):
    return set(c for c in characters if c != "\n")


def intersection_characters(characters):
    if len(characters) == 2:
        return [characters[0]]  # this is horrible
    return [list(c for c in line) for line in characters.split("\n")]


if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <input file>")
    sys.exit(1)

filename = str(sys.argv[1])

data = group_reader(filename)

groups = [unique_characters(g) for g in data]
count_groups = len(groups)
sum_of_yes_answers = sum(len(g) for g in groups)

print(
    f"There were {count_groups} groups with a the total number of yes "
    f"answers being {sum_of_yes_answers} for the first scenario."
)

groups = [intersection_characters(g) for g in data]
count_groups = len(groups)

intersections = [set(group[0]).intersection(*group) for group in groups]
sum_of_yes_answers = sum(len(g) for g in intersections)

print(
    f"There were {count_groups} groups with a the total number of yes "
    f"answers being {sum_of_yes_answers} for the second scenario."
)
