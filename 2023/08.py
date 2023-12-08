#!/usr/bin/env python3
"""
2023 Day 08 Solution

"""

# import re
import sys
import os
from functools import lru_cache
# from multiprocessing import Pool
import math
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


def find_end(start: str, end: set(), node_mapping: tuple, move_list: tuple) -> int:
    """
    Returns an steps: int to get from start to a node in set end
    """
    current = start
    s = 0
    while not end.issuperset(set([current,])):
        for m in move_list:
            if end.issuperset(set([current, ])):
                break
            current = node_mapping[current][m]
            s += 1
    return s


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
    steps = find_end('AAA', {'ZZZ'}, mapping, moves)
    print('Part 1:', steps)

    # part 2
    p2_current = [x for x in mapping.keys() if x.endswith('A')]
    p2_end = set(x for x in mapping.keys() if x.endswith('Z'))
    p2_steps_to_z = [find_end(s, p2_end, mapping, moves) for s in p2_current]
    p2_steps = math.lcm(*p2_steps_to_z)
    print('Part 2:', p2_steps)  # 18215611419223


if __name__ == '__main__':
    main()
