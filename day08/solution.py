def get_digits_with_unique_segment_counts(list_of_digits):
    unique_segment_counts = [2, 3, 4, 7]
    return [digit for digit in list_of_digits if len(digit) in unique_segment_counts]


def map_digits_to_patterns(unique_patterns):
    segment_count_to_digit = {
        2: 1,
        3: 7,
        4: 4,
        7: 8
    }
    return {segment_count_to_digit[len(pattern)]: set(pattern) for pattern in unique_patterns}


def get_pattern_to_digit_mapping(signal_patterns):
    unique_patterns = get_digits_with_unique_segment_counts(signal_patterns)
    digits_to_patterns = map_digits_to_patterns(unique_patterns)
    digits_to_patterns[3] = \
        [set(x) for x in signal_patterns if len(digits_to_patterns[1].intersection(set(x))) == 2 and len(x) == 5][0]

    correct_to_incorrect_segment = {
        'a': digits_to_patterns[7].difference(digits_to_patterns[1]),
        'bd': digits_to_patterns[4].difference(digits_to_patterns[1]),
        'eg': digits_to_patterns[8].difference(digits_to_patterns[4]).difference(digits_to_patterns[7]),
        'd': digits_to_patterns[4].intersection(digits_to_patterns[3]).difference(digits_to_patterns[1]),
    }

    correct_to_incorrect_segment['b'] = correct_to_incorrect_segment['bd'].difference(correct_to_incorrect_segment['d'])
    correct_to_incorrect_segment['e'] = correct_to_incorrect_segment['eg'].difference(digits_to_patterns[3])
    correct_to_incorrect_segment['g'] = correct_to_incorrect_segment['eg'].difference(correct_to_incorrect_segment['e'])

    digits_to_patterns[9] = digits_to_patterns[3].union(correct_to_incorrect_segment['b'])
    digits_to_patterns[0] = digits_to_patterns[8].difference(correct_to_incorrect_segment['d'])
    digits_to_patterns[5] = \
        [set(x) for x in signal_patterns if len(digits_to_patterns[9].intersection(set(x))) == 5 and len(x) == 5 and set(x) != digits_to_patterns[3]][0]

    correct_to_incorrect_segment['c'] = digits_to_patterns[1].difference(digits_to_patterns[5])
    correct_to_incorrect_segment['f'] = digits_to_patterns[1].difference(correct_to_incorrect_segment['c'])

    digits_to_patterns[2] = digits_to_patterns[8].difference(
        correct_to_incorrect_segment['f'].union(correct_to_incorrect_segment['b']))
    digits_to_patterns[6] = digits_to_patterns[5].union(correct_to_incorrect_segment['e'])

    return {frozenset(v): k for k, v in digits_to_patterns.items()}


def part_one(signal_patterns_and_digit_output):
    return sum([len(get_digits_with_unique_segment_counts(spdo[1])) for spdo in signal_patterns_and_digit_output])


def part_two(signal_patterns_and_digit_output):
    pattern_to_digit_mappings_to_digits_outputs = [(get_pattern_to_digit_mapping(spdo[0]), spdo[1]) for spdo in
                                                   signal_patterns_and_digit_output]
    return sum([
        int(
            ''.join(
                [str(pattern_to_digit_mapping[frozenset(digit_output)]) for digit_output in digits_output]
            )
        ) for pattern_to_digit_mapping, digits_output in pattern_to_digit_mappings_to_digits_outputs
    ])


with open('input', 'r') as infile:
    signal_patterns_and_digit_output = [[x.strip().split(' ') for x in line.strip().split('|')] for line in
                                        infile.readlines()]

print(part_one(signal_patterns_and_digit_output))
print(part_two(signal_patterns_and_digit_output))
