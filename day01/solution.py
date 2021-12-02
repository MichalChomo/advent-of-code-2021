def part_one(lines):
    increasing = 0
    previous = 0
    for line in lines:
        current = int(line)
        if current > previous:
            increasing += 1
        previous = current

    increasing -= 1
    return increasing


def part_two(lines):
    previous_window = 0
    window = 0
    increasing = 0
    for i, line in enumerate(lines):
        if i > 2:
            previous_window = window
        window += int(line)
        if i > 2:
            window -= int(lines[i - 3])
            if window > previous_window:
                increasing += 1

    return increasing


with open('input', 'r') as infile:
    lines = infile.readlines()

print(part_one(lines))
print(part_two(lines))
