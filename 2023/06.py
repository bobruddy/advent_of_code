#!/usr/bin/env python3
"""
2023 Day 06 Solution
"""

import re
import sys
import os
from functools import lru_cache
from multiprocessing import Pool
import math
import time


def read_input(file: str) -> list:
    """
    Read and parse input
    """
    with open(file, 'r', encoding="utf-8") as fd:
        raw_input = [x.strip().replace(':', ' ') for x in fd.readlines()]

        clean_data = raw_input
    return clean_data


def parse_data(base_data: list) -> tuple:
    """
    Parse raw data
    """

    return None


def main():
    """
    Solves part1/part2
    """
    for arg in sys.argv:
        if arg.endswith('.input') and os.path.exists(arg):
            file = arg
            break
    input_data = read_input(file)
    parsed_data = parse_data(input_data)

    # part 1
    print('Part 1:', )

    # part 2
    print('Part 2:', )


if __name__ == '__main__':
    main()
