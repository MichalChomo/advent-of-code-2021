def part_one(lines):
    position = 0
    depth = 0
    for line in lines:
        (command, steps) = line.split(' ')
        steps = int(steps)
        if command == 'forward':
            position += steps
        elif command == 'down':
            depth += steps
        elif command == 'up':
            depth -= steps

    return position, depth


def part_two(lines):
    position = 0
    depth = 0
    aim = 0
    for line in lines:
        (command, steps) = line.split(' ')
        steps = int(steps)
        if command == 'forward':
            position += steps
            depth += aim * steps
        elif command == 'down':
            aim += steps
        elif command == 'up':
            aim -= steps

    return position, depth


with open('input', 'r') as infile:
    lines = [l.strip('\n') for l in infile.readlines()]

res = part_two(lines)
print(res[0] * res[1])
