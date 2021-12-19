import copy
import itertools


def iterate_with_indexes(levels, func):
    for i in range(len(levels)):
        for j in range(len(levels[0])):
            levels = func(levels, i, j)


def increment_adjacent(levels, row, col):
    for i, j in itertools.product([x for x in [row - 1, row, row + 1] if 0 <= x < 10],
                                  [x for x in [col - 1, col, col + 1] if 0 <= x < 10]):
        if levels[i][j] > 0:
            levels[i][j] += 1

    return levels


def flash(levels):
    def append_to_flashing(levels, i, j):
        if levels[i][j] > 9:
            flashing.append((i, j))
        return levels

    flashing = []
    while True:
        iterate_with_indexes(levels, append_to_flashing)
        if len(flashing) == 0:
            break
        for row, col in flashing:
            levels = increment_adjacent(levels, row, col)
            levels[row][col] = 0
        flashing = []

    return levels


def step(levels):
    def increment_by_one(levels, i, j):
        levels[i][j] += 1
        return levels

    iterate_with_indexes(levels, increment_by_one)

    return flash(levels)


def part_one(levels):
    flashes = 0
    for i in range(100):
        levels = step(levels)
        flashes += len([col for row in levels for col in row if col == 0])

    return flashes


def part_two(levels):
    i = 1
    while True:
        levels = step(levels)
        if sum([col for row in levels for col in row]) == 0:
            return i
        i += 1


with open('input', 'r') as infile:
    levels = [[int(col) for col in row] for row in [line.strip() for line in infile.readlines()]]

levels_copy = copy.deepcopy(levels)
print(part_one(levels))
print(part_two(levels_copy))
