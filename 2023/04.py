#!/usr/bin/env python3
"""
2023 Day 03 Solution
"""

import re
import sys
import os
from functools import lru_cache


@lru_cache
def read_input(file: str):
    """
    Read and parse input
    """
    with open(file, 'r', encoding="utf-8") as fd:
        raw_input = [x.strip().replace('.', ' ') for x in fd.readlines()]

        clean_data = raw_input
    return clean_data


def parse_data(base_data: str):
    """
    Parse raw data
    """
    card, remainder = base_data.split(':')
    card = int(re.split(r'\s+', card)[1])
    win_num, my_num = remainder.split('|')
    win_num = frozenset([int(x.strip()) for x in win_num.strip().split(' ') if x != ''])
    my_num = frozenset([int(x.strip()) for x in my_num.strip().split(' ') if x != ''])
    return (card, win_num, my_num)


@lru_cache
def find_matches(data):
    """
    Returns matching numbers
    """
    # print(data)
    card, win_num, my_num = data
    matches = win_num.intersection(my_num)
    return (card, len(matches))  # , matches)


def part1_score(card_data):
    """
    Score card for part 1
    """
    num_of_matches = find_matches(card_data)[1]
    if num_of_matches == 0:
        return 0
    return 2**(num_of_matches - 1)


@lru_cache
def part2_find_children(card_data, full_dataset):
    """
    This uses recursion to find all possible matches
    """
    card, num_of_matches = fmatch = find_matches(card_data)
    if num_of_matches == 0:
        return []

    # builds list of cards I need to find matches in
    new_cards = [full_dataset[x] for x in range(card, card + num_of_matches)]

    # this list will capture all the matches. starting with the match from this call
    ret_list = []
    ret_list.append(fmatch)

    # call this same function for all new cards. keep the output in ret_list
    for c in new_cards:
        child_ret = part2_find_children(c, full_dataset)
        if len(child_ret) > 0:
            ret_list = ret_list + child_ret

    return ret_list


def main():
    """
    Solves part1/part2
    """
    for arg in sys.argv:
        if arg.endswith('.input') and os.path.exists(arg):
            file = arg
            break
    input_data = read_input(file)
    data_set = tuple(map(parse_data, input_data))

    # part 1
    scores = list(map(part1_score, data_set))
    print('Part 1:', sum(scores))

    # part 2
    c_ret = len(data_set)
    for c in data_set:       # loop through each of the cards
        co = [x[1] for x in part2_find_children(c, data_set)]
        c_ret += sum(co)
    print('Part 2:', c_ret)


if __name__ == '__main__':
    main()
