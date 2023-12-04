#!/usr/bin/env python3
"""
2023 Day 03 Solution
"""

import re
import string
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
    win_num = {int(x.strip()) for x in win_num.strip().split(' ') if x != ''}
    my_num = {int(x.strip()) for x in my_num.strip().split(' ') if x != ''}
    return (card, win_num, my_num)


def part1_score(card_data):
    """
    Score card for part 1
    """
    card, win_num, my_num = tuple(card_data)
    match = win_num.intersection(my_num)
    if len(match) == 0:
        return 0
    return 2**(len(match) - 1)


def main():
    """
    Solves part1/part2
    """
    for arg in sys.argv:
        if arg.endswith('.input') and os.path.exists(arg):
            file = arg
            break
    input_data = read_input(file)
    data_set = list(map(parse_data, input_data))
    scores = list(map(part1_score, data_set))

    # part 1
    print('Part 1:', sum(scores))

    # part 2
    print('Part 2:', )


if __name__ == '__main__':
    main()
