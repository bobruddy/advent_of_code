#!/usr/bin/env python3
"""
2023 Day 09 Solution

"""

import sys
import os
import numpy as np
np.set_printoptions(linewidth=np.inf)


def read_input(file: str) -> list:
    """
    Read and parse input
    """
    with open(file, 'r', encoding="utf-8") as fd:
        return [x.strip() for x in fd.readlines()]


def parse_data(base_data: list) -> tuple:
    """
    Parse raw data
    """
    return tuple(np.array(tuple(map(int, row.split(' ')))) for row in base_data)


def day09_calc(data) -> list:
    """
    Calc the first and last numbers in one set of loops
    """
    right_num = []
    left_num = []
    for i_row in data:
        cur_row = i_row.copy()

        last_digit = []
        first_digit = []
        while sum(abs((new_diff := np.diff(cur_row)))) > 0:
            last_digit.append(cur_row[-1])
            first_digit.append(cur_row[0])
            cur_row = new_diff.copy()
        last_digit.append(cur_row[-1])
        first_digit.append(cur_row[0])

        last_digit.reverse()
        right_diff = 0
        for row in last_digit:
            right_diff = row + right_diff
        right_num.append(right_diff)

        first_digit.reverse()
        left_diff = 0
        for row in first_digit:
            left_diff = row - left_diff
        left_num.append(left_diff)

    return tuple(left_num), tuple(right_num)


def main():
    """
    Solves part1/part2
    """
    for arg in sys.argv:
        if arg.endswith('.input') and os.path.exists(arg):
            file = arg
            break
    parsed_input = parse_data(read_input(file))
    part02, part01 = day09_calc(parsed_input)

    # part 1
    print('Part 1:', sum(part01), f"{sum(part01):,}")  # my answer 1993300041
    # part 2
    print('Part 2:', sum(part02), f"{sum(part02):,}")  # my answer 1038


if __name__ == '__main__':
    main()
