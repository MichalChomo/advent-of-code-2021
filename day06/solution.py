def memoize(f):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return wrap


@memoize
def get_fishes_count(fish_age, days):
    if days == 0:
        return 1

    if fish_age == 0:
        return get_fishes_count(6, days - 1) + get_fishes_count(8, days - 1)
    else:
        return get_fishes_count(fish_age - 1, days - 1)


def get_total_count(fishes, days):
    return sum([get_fishes_count(f, days) for f in fishes])


def part_one(fishes):
    return get_total_count(fishes, 80)


def part_two(fishes):
    return get_total_count(fishes, 256)


with open('input', 'r') as infile:
    fishes = [int(x) for x in infile.readline().split(',')]

print(part_one(fishes))
print(part_two(fishes))
