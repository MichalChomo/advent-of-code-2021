def part_one(numbers):
    increasing = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            increasing += 1

    return increasing


def part_two(numbers):
    previous_window = 0
    window = 0
    increasing = 0
    for i, num in enumerate(numbers):
        if i > 2:
            previous_window = window
        window += num
        if i > 2:
            window -= numbers[i - 3]
            if window > previous_window:
                increasing += 1

    return increasing


with open('input', 'r') as infile:
    numbers = list(map(lambda l: int(l.strip('\n')), infile.readlines()))

print(part_one(numbers))
print(part_two(numbers))
