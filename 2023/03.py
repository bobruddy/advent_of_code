#!/usr/bin/env python3
"""
2023 Day 03 Solution
"""

import re
import string
import sys
import os
from functools import lru_cache


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

    I'm finding all the symbols and then finding all the coordinates
    around each symbol where if there is a number in there they are
    adjacent.
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


@lru_cache
def find_numbers(row: str):
    """
    Find all the numbers in a row
    """

    numbers = []
    # this finds the coordinates of all the numbers
    for m in re.finditer(r'\d+', row):
        number = m.group(0)
        m_start = m.start()
        m_end = m.end()
        position = set(range(m_start, m_end))
        numbers.append({
            'cols': position,
            'part_number': int(number)
        })
    return numbers


def find_gears(raw_input):
    """
    This is for part 2 of the question and will find the gears

    Loop through each of the found symbols. find coordinates where
    a number would have to be. check to see if a number is in one
    of them. if so capture that number. if the number of captured
    numbers for each coordinate is exactly two then return that in
    the loop

    """
    gear_pattern = '[' + re.escape('*') + ']'
    re_gear = re.compile(gear_pattern)
    for row_id, cur_row in enumerate(raw_input):
        # This finds the coorindates where a number has to be to be adjacent
        cur_row_indexes = {m.start(0) for m in re_gear.finditer(cur_row)}
        for col_id in cur_row_indexes:
            rows = {row_id - 1, row_id, row_id + 1}
            cols = {col_id - 1, col_id, col_id + 1}

            # for every pattern find overlapping part numbers
            found_part = []  # list of find numbers per potential gear
            for sym_row_id in rows:
                # get all the numbers for thta tow and check for overlap by colum
                # check we aren't over limits
                if sym_row_id < 0 or row_id > len(raw_input) - 1:
                    continue
                numbers_in_row = find_numbers(raw_input[sym_row_id])
                for num in numbers_in_row:
                    if cols.intersection(num.get('cols')):
                        found_part.append(num.get('part_number'))

            # only save this combination if there are exactly two matches
            if len(found_part) == 2:
                yield tuple(found_part)


def main():
    """
    Solves part1/part2
    """
    for arg in sys.argv:
        if arg.endswith('.input') and os.path.exists(arg):
            file = arg
            break
    input_data = read_input(file)

    # part 1
    p_list = list_of_parts(input_data)
    print('Part 1:', sum(p_list))

    # part 2
    g_list = find_gears(input_data)
    ratio_list = [g1 * g2 for g1, g2 in g_list]
    print('Part 2:', sum(ratio_list))


if __name__ == '__main__':
    main()
