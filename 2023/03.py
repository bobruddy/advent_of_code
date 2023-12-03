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


def find_gears(raw_input):
    """
    This is for part 2 of the question and will find the gears

    Same as part 1 where i'm finding all the * and coordinates
    around them then finding which numbers overlap. 

    I'm doing in three loops 1) find symbols 2) find numbers
    3) find and return the intersections. I could do the 3rd
    in the 2nd loop, with the number seach in a diff function
    with lru_cache to make it go faster. but i've got to do 
    some cleaning
    """
    gear_pattern = '[' + re.escape('*') + ']'
    gear_coordinates = []
    number_coordinates = {}
    for row_id, cur_row in enumerate(raw_input):
        # This finds the coorindates where a number has to be to be adjacent
        cur_row_indexes = {m.start(0) for m in re.finditer(gear_pattern, cur_row)}
        for col_id in cur_row_indexes:
            gear_coordinates.append({
                'rows': {row_id - 1, row_id, row_id + 1},
                'cols': {col_id - 1, col_id, col_id + 1},
            })

        # this finds the coordinates of all the numbers
        for m in re.finditer(r'\d+', cur_row):
            number = m.group(0)
            m_start = m.start()
            m_end = m.end()
            position = set(range(m_start, m_end))
            if not number_coordinates.get(row_id):
                number_coordinates[row_id] = []
            number_coordinates[row_id].append({
                'cols': position,
                'part_number': int(number)
            })

    # for every pattern find overlapping part numbers
    list_o_gears = []
    for ast in gear_coordinates:
        found_part = []
        col_list = ast.get('cols')
        for row_id in ast.get('rows'):
            # get all the numbers for thta tow and check for overlap by colum
            num_in_row = number_coordinates.get(row_id)
            for num in num_in_row:
                if col_list.intersection(num.get('cols')):
                    found_part.append(num.get('part_number'))

        # only save this combination if there are exactly two matches
        if len(found_part) == 2:
            list_o_gears.append(tuple(found_part))

    return list_o_gears


def main():
    """
    Solves part1/part2
    """
    input_data = read_input('03.input')

    # part 1
    # p_list = list_of_parts(input_data)
    # print('Part 1:', sum(p_list))

    # part 2
    g_list = find_gears(input_data)
    print(g_list)
    ratio_list = [g1 * g2 for g1, g2 in g_list]
    print('Part 2:', sum(ratio_list))


if __name__ == '__main__':
    main()
