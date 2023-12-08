#!/usr/bin/env python3
"""
2023 Day 08 Solution

"""

# import re
import sys
import os
from functools import lru_cache
# from multiprocessing import Pool
# import math
# import time
# import tqdm
# from collections import Counter
# from operator import itemgetter


def read_input(file: str) -> list:
    """
    Read and parse input
    """
    with open(file, 'r', encoding="utf-8") as fd:
        return [x.strip() for x in fd.readlines()]


@lru_cache
def parse_line(move: str) -> tuple:
    """
    Quick parsing of the line
    """
    return tuple(move.replace('=', '')
                 .replace('(', '')
                 .replace(')', '')
                 .replace(',', '')
                 .replace('  ', ' ')
                 .split(' '))


def parse_data(base_data: list) -> tuple:
    """
    Parse raw data
    """
    instructions = base_data[0]
    line = tuple(parse_line(base_data[x]) for x in range(2, len(base_data)))
    data = {r[0]: {'L': r[1], 'R': r[2]} for r in line}
    return instructions, data


def main():
    """
    Solves part1/part2
    """
    for arg in sys.argv:
        if arg.endswith('.input') and os.path.exists(arg):
            file = arg
            break

    moves, mapping = parse_data(list(read_input(file)))

    # part 1

    current = 'AAA'
    steps = 0
    while current != 'ZZZ':
        for m in moves:
            if current == 'ZZZ':
                break
            current = mapping[current][m]
            steps += 1

    print('Part 1:', steps)

    # part 2

    p2_current = [x for x in mapping.keys() if x.endswith('A')]
    p2_end = set(x for x in mapping.keys() if x.endswith('Z'))
    p2_steps = 0

    while not p2_end.issuperset(set(p2_current)):
        for m in moves:
            if p2_end.issuperset(set(p2_current)):
                break

            prev_current = p2_current
            p2_current = []
            # print('m', m)
            for s in prev_current:
                # print('s', s)
                p2_current.append(mapping[s][m])
            p2_steps += 1
            if p2_steps % 1000 == 0:
                print(p2_steps)

    print(p2_current)
    print(p2_end)
    print('Part 2:', p2_steps)


if __name__ == '__main__':
    main()
