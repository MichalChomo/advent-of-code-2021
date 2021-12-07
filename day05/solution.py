import numpy as np


def get_int_tuple_from_string_pair(pair):
    return tuple((int(x) for x in pair.split(',')))


def get_zeroed_field(vectors):
    dimension_size = max(vectors.flat) + 1
    return np.zeros((dimension_size, dimension_size), dtype=int)


def get_overlaps_count_from_field(field):
    return len([x for x in field.flat if x > 1])


def filter_horizontal_and_vertical_lines(vector):
    return vector[0, 0] == vector[1, 0] or vector[0, 1] == vector[1, 1]


def filter_diagonal_lines(vector):
    return vector[0, 0] != vector[1, 0] and vector[0, 1] != vector[1, 1]


def get_lines_coordinates(vectors, predicate):
    return [(v[0, 0], v[1, 0], v[0, 1], v[1, 1]) for v in vectors if predicate(v)]


def fill_field_by_horizontal_and_vertical_lines(vectors, field):
    lines = get_lines_coordinates(vectors, filter_horizontal_and_vertical_lines)
    for x1, x2, y1, y2 in lines:
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                field[y][x] += 1


def fill_field_by_diagonal_lines(vectors, field):
    lines = get_lines_coordinates(vectors, filter_diagonal_lines)
    for x1, x2, y1, y2 in lines:
        xrange = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
        yrange = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
        for x, y in zip(xrange, yrange):
            field[y][x] += 1


def part_one(vectors, field):
    fill_field_by_horizontal_and_vertical_lines(vectors, field)
    return get_overlaps_count_from_field(field)


def part_two(vectors, field):
    fill_field_by_horizontal_and_vertical_lines(vectors, field)
    fill_field_by_diagonal_lines(vectors, field)
    return get_overlaps_count_from_field(field)


with open('input', 'r') as infile:
    vectors = [(get_int_tuple_from_string_pair(pair[0]), get_int_tuple_from_string_pair(pair[1])) for pair in
               (line.strip('\n').replace(' ', '').split('->') for line in infile.readlines())]

vectors = np.array(vectors)

print(part_one(vectors, get_zeroed_field(vectors)))
print(part_two(vectors, get_zeroed_field(vectors)))
