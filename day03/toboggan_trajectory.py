#!/usr/bin/env python3

import sys
from functools import reduce

DEBUG = False


def terrain_tile_reader(filename):
    with open(filename) as file_object:
        terrain = list()
        for line in file_object:
            terrain.append(line[:-1])  # removing trailing newline
        return terrain


def navigate_terrain(terrain, right, down):
    results = {}
    x, y = 0, 0
    height = len(terrain)
    width = len(terrain[0])
    while True:
        x += right
        x %= width
        y += down
        character = terrain[y][x]
        if DEBUG:
            print(
                f"({x}, {y}) inside ({width}, {height}) with step "
                f"({right}, {down}) yields '{character}'."
            )
        if character in results:
            results[character] += 1
        else:
            results[character] = 1

        if y >= height - 1:  # I wish Python had "do until" loops
            break
    return results


if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <input file>")
    sys.exit(1)

filename = str(sys.argv[1])
directions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree = "#"

terrain = terrain_tile_reader(filename)
statistics = list()

for right, down in directions:
    results = navigate_terrain(terrain, right, down)
    statistics.append(results[tree])

for rightdown, trees in zip(directions, statistics):
    print(f"For trajectory {rightdown}, we encountered {trees} trees.")

tree_product = reduce((lambda x, y: x * y), statistics)
print(f"Multiplying all these trees together gives us {tree_product:,}.")
