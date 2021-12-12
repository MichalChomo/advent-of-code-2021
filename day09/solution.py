import math


def safe_element_at(array, row, col):
    if row < 0 or col < 0 or row > (len(array) - 1) or col > (len(array[0]) - 1):
        return 10
    return array[row][col]


def is_lower_than_adjacent(array, row, col):
    num = array[row][col]
    return (num < safe_element_at(array, row - 1, col)
            and num < safe_element_at(array, row, col - 1)
            and num < safe_element_at(array, row + 1, col)
            and num < safe_element_at(array, row, col + 1))


def get_low_points(array):
    return [(num, i, j) for i, row in enumerate(array) for j, num in enumerate(row) if
            is_lower_than_adjacent(array, i, j)]


def find_higher_adjacent(array, low_point):
    num, row, col = low_point
    up = safe_element_at(array, row - 1, col), row - 1, col
    down = safe_element_at(array, row + 1, col), row + 1, col
    left = safe_element_at(array, row, col - 1), row, col - 1
    right = safe_element_at(array, row, col + 1), row, col + 1
    higher_adjacent = {adjacent for adjacent in [up, down, left, right] if num < adjacent[0] < 9}
    if len(higher_adjacent) > 0:
        all_higher_in_basin = set()
        for point in higher_adjacent:
            all_higher_in_basin = all_higher_in_basin.union(find_higher_adjacent(array, point))
        return {low_point}.union(all_higher_in_basin)
    else:
        return {low_point}


def get_size_of_basin(array, low_point):
    return len(find_higher_adjacent(array, low_point))


def part_one(array):
    return sum([low_point[0] + 1 for low_point in get_low_points(array)])


def part_two(array):
    low_points = get_low_points(array)
    return math.prod(sorted([get_size_of_basin(array, lp) for lp in low_points])[-3:])


with open('input', 'r') as infile:
    array = [[int(x) for x in line.strip()] for line in infile.readlines()]

print(part_one(array))
print(part_two(array))
