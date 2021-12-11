import numpy as np
from collections.abc import Iterable
import copy

def flatten(x):  # x-dimensionale array -> 1d array
    if isinstance(x, Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]

def get_boards(filename):  # Lees data
    with open(filename) as f:
        lines = f.read().splitlines()
        f.close()
        for count, value in enumerate(lines):  # Verwijdert witregels
            if value == '':
                lines.remove(value)
        return lines


def split_boards(boards_list):  # Geeft instructies als lijst en borden als lijst met 5 x 5 x aantal borden als dimensies
    numbers = boards_list[0]
    boards_list.remove(boards_list[0])
    for count, value in enumerate(boards_list):  # Creert lijsten van ints ipv strings
        boards_list[count] = list(map(int, value.split()))
    boards_3d = []
    amount_of_boards = int((len(boards_list)/5))

    # zorgt voor de juiste dimensies bord per bord
    for k in range(amount_of_boards):  # Start aan een nieuw bord
        boards_3d.append([])
        for j in range(5):  # Start aan een nieuwe rij
            boards_3d[k].append([])
            for i in range(5):  # Voegt alle elementen in de huidige rij toe
                boards_3d[k][j].append(boards_list[j+k*5][i])

    numbers = numbers.split(",")
    return numbers, boards_3d

def play_bingo(numbers, boards_3d):
    boards_amount = len(boards_3d)
    deleted_boards = []
    completed_boards = 0
    rows = boards_3d
    columns = boards_3d.copy()
    for count, value in enumerate(boards_3d):  # Geeft lijsten van alle kolommen in de juiste dimensies
        columns[count] = np.array(value).transpose().tolist()

    for count, value in enumerate(numbers):  # alle bingo cijfers

        for i in range(boards_amount):  # aantal borden
            for c, v in enumerate(rows[0]):  # aantal rijen
                try:
                    rows[i][c].remove(int(value))
                except ValueError:
                    pass
                try:
                    columns[i][c].remove(int(value))
                except ValueError:
                    pass

                if not rows[i][c] or not columns[i][c]:  # Indien een rij het beslissende was
                    if completed_boards == 0:
                        first_value = value
                        first_rows = copy.deepcopy(rows[i])
                        first_columns = copy.deepcopy(columns[i])

                    if i not in deleted_boards:  # Tel borden niet mee indien hier al bingo gehaald is
                        completed_boards += 1
                        deleted_boards.append(i)
                if completed_boards == boards_amount:  # Stop als elk bord bingo heeft
                    last_value, last_rows, last_columns = value, rows[i], columns[i]
                    return first_rows, first_value, first_columns, last_value, last_rows, last_columns

def calculate_score(first_rows, first_value, first_columns, last_value, last_rows, last_columns):
    # Eerste
    flat_list_rows = flatten(first_rows)
    flat_list_columns = flatten(first_columns)
    first_sum_of_remainders = min(sum(flat_list_rows), sum(flat_list_columns))
    first_total_score = first_sum_of_remainders*int(first_value)

    # Laatste
    flat_list_rows = flatten(last_rows)
    flat_list_columns = flatten(last_columns)
    last_sum_of_remainders = min(sum(flat_list_rows), sum(flat_list_columns))
    last_total_score = last_sum_of_remainders * int(last_value)

    print(f"Eerste bord: {first_total_score}, {first_sum_of_remainders}, {first_value}")
    print(f"Laatste bord: {last_total_score}, {last_sum_of_remainders}, {last_value}")


calculate_score(*play_bingo(*split_boards(get_boards('Puzzle_Input.txt'))))

