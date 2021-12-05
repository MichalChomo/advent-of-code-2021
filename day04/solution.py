import copy


def find_winner_by_rows(board):
    for row in board:
        if sum(row) == -5:
            return board
    return None


def find_winner_by_cols(board):
    if len(board) == 0:
        return None

    for i in range(len(board[0])):
        col = [board[j][i] for j in range(len(board))]
        if sum(col) == -5:
            return board
    return None


def mark_number_in_board(number, board):
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == number:
                board[i][j] = -1

    return board


def find_winner_board(random_numbers, boards, return_on_first=True):
    result = None
    for random_number_index, random_number in enumerate(random_numbers):
        for board_index, board in enumerate(boards):
            board = mark_number_in_board(random_number, board)

            winner = find_winner_by_rows(board)
            if winner is None:
                winner = find_winner_by_cols(board)

            if winner is not None:
                if return_on_first:
                    return winner, random_number
                else:
                    result = winner, random_number
                    boards[board_index] = []

    return None if return_on_first else result


def get_board_score(board, n):
    return sum([x for row in board for x in row if x > -1]) * n


def part_one(random_numbers, boards):
    winner_board, random_number = find_winner_board(random_numbers, boards)
    return get_board_score(winner_board, random_number)


def part_two(random_numbers, boards):
    winner_board, random_number = find_winner_board(random_numbers, boards, return_on_first=False)
    return get_board_score(winner_board, random_number)


with open('input', 'r') as infile:
    random_numbers = [int(x) for x in infile.readline().strip('\n').split(',')]
    boards = [[int(x) for x in line.strip('\n').lstrip().rstrip().replace('  ', ' ').split(' ')] for line in
              infile.readlines() if line != '\n']

boards = [boards[i:i + 5] for i in range(0, len(boards), 5)]
boards_copy = copy.deepcopy(boards)

print(part_one(random_numbers, boards))
print(part_two(random_numbers, boards_copy))
