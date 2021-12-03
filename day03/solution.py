class LineIndexes:
    def __init__(self):
        self.numbers_that_have_zero = set()
        self.numbers_that_have_one = set()


def binary_list_to_int(lst):
    return int(''.join(map(str, lst)), 2)


def binary_string_to_int(string):
    return binary_list_to_int(list(string))


def get_score_list(lines, start_index=0):
    """
    :param start_index: Optional index where to start the score checking.
    :param lines: List of lines containing binary numbers.
    :return: List of scores for each line index, score is +1 for '1' and -1 for '0'
             e.g. line '101' gets score [1, -1, 1] and then line '001' changes it to [0, -2, 2].
    """
    score_list = [0 for _ in range(len(lines[0]))]

    for line in lines:
        for i in range(start_index, len(line)):
            if line[i] == '0':
                score_list[i] -= 1
            else:
                score_list[i] += 1

    return score_list


def get_rating(lines, original_score_list, list_of_line_indexes, least_common_value=False):
    line_indexes = set([x for x in range(len(lines))])
    i = 0
    score_list = original_score_list
    while len(line_indexes) > 1:
        if score_list[i] < 0:
            # There are more 0s at position i
            if least_common_value:
                line_indexes = line_indexes.intersection(list_of_line_indexes[i].numbers_that_have_one)
            else:
                line_indexes = line_indexes.intersection(list_of_line_indexes[i].numbers_that_have_zero)
        else:
            # There are more 1s at position i
            if least_common_value:
                line_indexes = line_indexes.intersection(list_of_line_indexes[i].numbers_that_have_zero)
            else:
                line_indexes = line_indexes.intersection(list_of_line_indexes[i].numbers_that_have_one)

        i += 1
        score_list = get_score_list([lines[x] for x in line_indexes], start_index=i)

    return binary_string_to_int(lines[line_indexes.pop()])


def part_one(lines):
    score_list = get_score_list(lines)

    gamma = [1 if x > 0 else 0 for x in score_list]
    epsilon = [1 if x == 0 else 0 for x in gamma]

    gamma = binary_list_to_int(gamma)
    epsilon = binary_list_to_int(epsilon)

    return gamma * epsilon


def part_two(lines):
    score_list = [0 for _ in range(len(lines[0]))]
    list_of_line_indexes = [LineIndexes() for _ in range(len(lines[0]))]

    for line_index, line in enumerate(lines):
        for char_index, num in enumerate(line):
            if num == '0':
                score_list[char_index] -= 1
                list_of_line_indexes[char_index].numbers_that_have_zero.add(line_index)
            else:
                score_list[char_index] += 1
                list_of_line_indexes[char_index].numbers_that_have_one.add(line_index)

    oxygen_generator_rating = get_rating(lines, score_list, list_of_line_indexes)
    co2_scrubber_rating = get_rating(lines, score_list, list_of_line_indexes, least_common_value=True)

    return oxygen_generator_rating * co2_scrubber_rating


with open('input', 'r') as infile:
    lines = infile.readlines()
    lines = list(map(lambda l: l.strip('\n'), lines))

res = part_two(lines)
print(res)
