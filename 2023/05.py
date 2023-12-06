#!/usr/bin/env python3
"""
2023 Day 05 Solution
"""

import re
import sys
import os
from functools import lru_cache
import pprint


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
    src: str = None
    tgt: str = None

    mapping = []
    oseeds = []

    for eid, line in enumerate(base_data):
        # if eid > 20:
        #    break

        if line == '':
            continue

        re_digit = re.compile(r'^[\d]+')
        if re_digit.match(line):
            tgt_start, src_start, range_len = line.split(' ')
            mapping.append((src, tgt, int(tgt_start), int(src_start), int(range_len)))
            continue

        re_map_type = re.compile(r'^([a-z]+)-to-([a-z]+)')
        if b := re_map_type.match(line.replace(' map', '')):
            src = b.group(1)
            tgt = b.group(2)
            continue

        re_seeds = re.compile(r'^seeds\s+')
        if re_seeds.match(line):
            seeds_str = re.sub(re_seeds, '', line, count=1)
            oseeds = [int(x) for x in seeds_str.split(' ')]
            continue

    return oseeds, mapping


def find_loc(loc_type: str, item: int, loc_data: list):
    """
    Traverse the hierarchy to find lowest point in this case "location"
    """
    orig_loc = loc_type
    loc = orig_loc
    position = item
    for src, tgt, t_start, s_start, r_len in loc_data:
        if src != loc_type:
            continue

        loc = tgt
        if s_start <= item < (s_start + r_len):
            position = t_start + item - s_start
            break

    if orig_loc != loc:
        loc, position = find_loc(loc, position, loc_data)
    return (loc, position)


def main():
    """
    Solves part1/part2
    """
    for arg in sys.argv:
        if arg.endswith('.input') and os.path.exists(arg):
            file = arg
            break
    input_data = read_input(file)
    orig_seeds, map_data = parse_data(input_data)

    # part 1
    a = [find_loc('seed', seed, map_data)[1] for seed in orig_seeds]
    print('Part 1:', min(a))

    # part 2
    print('Part 2:', )


if __name__ == '__main__':
    main()
