import statistics


def difference(x, y):
    return abs(x - y)


def difference_with_constant_rise(x, y):
    """
    Since the difference between cost at each move is 1, this can be calculated as arithmetic progression starting
    at 1 and ending at the positive difference of the numbers because an = n.
    E.g. For 2 to 5, the cost of moves is [1, 2, 3], so an = n = 3, ((1 + 3) * 3) / 2 = 6
    """
    diff = difference(x, y)
    return ((1 + diff) * diff) / 2


def get_total_fuel(position_to_align_to, positions):
    return sum([difference(p, position_to_align_to) for p in positions])


def get_total_fuel_two(position_to_align_to, positions):
    return sum([int(difference_with_constant_rise(p, position_to_align_to)) for p in positions])


def part_one(positions):
    return get_total_fuel(int(statistics.median(positions)), positions)


def part_two(positions):
    return get_total_fuel_two(int(statistics.mean(positions)), positions)


with open('input', 'r') as infile:
    positions = [int(x) for x in infile.readline().split(',')]

print(part_one(positions))
print(part_two(positions))
