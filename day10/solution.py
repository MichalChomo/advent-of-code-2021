import statistics
from collections import deque

opening_to_closing_char = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


def find_illegal_char(line):
    stack = deque()

    for char in line:
        if char in opening_to_closing_char.keys():
            stack.appendleft(char)
        else:
            expected_char = opening_to_closing_char[stack.popleft()]
            if char != expected_char:
                return char

    return None


def get_completed_chars(line):
    stack = deque()

    for char in line:
        if char in opening_to_closing_char.keys():
            stack.appendleft(char)
        else:
            stack.popleft()

    return [opening_to_closing_char[char] for char in stack]


def get_corrupted_lines(lines):
    return [char for char in [find_illegal_char(line) for line in lines] if char is not None]


def get_incomplete_lines(lines):
    return [line for line in lines if find_illegal_char(line) is None]


def count_points_of_illegal_chars(illegal_chars):
    char_to_points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    return sum([char_to_points[char] for char in illegal_chars])


def get_points_of_completed_chars(completed_chars_on_lines):
    char_to_points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }

    scores = []
    for line in completed_chars_on_lines:
        score = 0
        for char in line:
            score *= 5
            score += char_to_points[char]
        scores.append(score)

    return scores


def part_one(lines):
    return count_points_of_illegal_chars(get_corrupted_lines(lines))


def part_two(lines):
    completed = [get_completed_chars(line) for line in get_incomplete_lines(lines)]
    points = get_points_of_completed_chars(completed)
    return statistics.median(sorted(points))


with open('input', 'r') as infile:
    lines = [line.strip() for line in infile.readlines()]

print(part_one(lines))
print(part_two(lines))
