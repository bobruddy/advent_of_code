#!/usr/bin/env python3
"""
2023 Day 03 Solution
"""

import re
import string


def read_input(file: str):
    """
    Read and parse input
    """
    with open(file, 'r', encoding="utf-8") as fd:
        raw_input = [x.strip().replace('.', ' ') for x in fd.readlines()]

        clean_data = raw_input
    return clean_data


def list_of_parts(raw_input):
    """
    gets a list of parts from the input
    """
    sym_pattern = '[' + re.escape(string.punctuation) + ']'
    prev_row_indexes = set()
    next_row_indexes = set()
    part_numbers = []
    for cur_id, cur_row in enumerate(raw_input):
        row_len = len(cur_row)
        index_set = set()
        if (prev_id := cur_id - 1) >= 0:
            prev_row = raw_input[prev_id]
            prev_row_indexes = {m.start(0) for m in re.finditer(sym_pattern, prev_row)}
        if (next_id := cur_id + 1) < len(raw_input):
            next_row = raw_input[next_id]
            next_row_indexes = {m.start(0) for m in re.finditer(sym_pattern, next_row)}
        cur_row_indexes = {m.start(0) for m in re.finditer(sym_pattern, cur_row)}
        index_set = index_set.union(prev_row_indexes, cur_row_indexes, next_row_indexes)
        index_w_diag = index_set.copy()
        for item in index_set:
            if item > 0:
                index_w_diag.add(item - 1)
            if item < row_len:
                index_w_diag.add(item + 1)

        cur_row_numbers = []
        for m in re.finditer(r'\d+', cur_row):
            number = m.group(0)
            m_start = m.start()
            m_end = m.end()
            position = set(range(m_start, m_end))
            cur_row_numbers.append((number, position))

        for number, position in cur_row_numbers:
            if position.intersection(index_w_diag):
                part_numbers.append(int(number))
    return part_numbers


def main():
    """
    Solves part1/part2
    """
    input_data = read_input('03.input')

    # part 1
    p_list = list_of_parts(input_data)
    print('Part 1:', sum(p_list))

    # part 2
    print('Part 2:')


if __name__ == '__main__':
    main()
