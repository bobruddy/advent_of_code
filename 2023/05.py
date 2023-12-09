#!/usr/bin/env python3
"""
2023 Day 05 Solution
"""

import re
import sys
import os
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

    return tuple(oseeds), tuple(mapping)


def find_loc(find_start: int, find_len: int, find_type: str, loc_data: list):
    """
    Traverse the hierarchy to find lowest point in this case "location"
    """
    find_end = find_start + find_len - 1  # number at end of range
    print(f"find val -> find_start:{find_start:,} find_end:{find_end:,} find_len:{find_len:,} find_type:{find_type}")

    for src, tgt, t_start, s_start, r_len in loc_data:
        t_end = t_start + r_len - 1
        s_end = s_start + r_len - 1
        print(f"src map -> src:{src} tgt:{tgt} s_start:{s_start:,} s_end:{s_end:,} t_start:{t_start:,} t_end:{t_end:,} r_len:{r_len:,}")

        if src != find_type:
            continue

        # if the range ends less than this map starts move on
        if find_end < s_start:
            continue

        # if the range starts greater than the map ends move on
        if find_start > s_end:
            continue

        # in this case the find range is fully within the map range
        if find_start >= s_start and find_end <= s_end:
            new_start = find_start - s_start + t_start
            new_len = find_len
            new_type = tgt
            print(f"fully enclosed new_start:{new_start:,} new_len:{new_len:,}")
            # make sub call here and then return
            break

        # in this use case start is contained, but the end is not
        if find_start >= s_start and find_end > s_end:
            new_start = find_start - s_start + t_start
            new_len = t_end - new_start + 1
            new_type = tgt
            # make call with tgt type

            remainder_len = find_len - new_len
            remainder_start = find_end - remainder_len + 1
            remainder_type = src
            print(f"start enclosed new_start:{new_start:,} new_len:{new_len:,} remainder_start:{remainder_start:,} remainder_len:{remainder_len:,}")
            # make call with src type
            # combine both of these and then return
            break

        # in this use case end is contained, but the start is not
        if find_start < s_start and find_end <= s_end:
            new_start = s_start
            new_len = find_end - s_start + 1
            new_type = tgt
            # make call with tgt type

            remainder_start = find_start
            remainder_len = s_start - find_start
            remainder_type = src
            print(f"start enclosed new_start:{new_start:,} new_len:{new_len:,} remainder_start:{remainder_start:,} remainder_len:{remainder_len:,}")
            # make call with src type
            # combine both of these and then return
            break

        # in this case the s_range fully encloses the find_range


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
    # a = [find_loc('seed', seed, (map_data))[1] for seed in orig_seeds]
    # print('Part 1:', min(a))

    # part 2
    # making a list and reversing so can use pop
    reverse_seeds = list(orig_seeds)
    reverse_seeds.reverse()

    loc_list = []
    for s_range in range(int(len(reverse_seeds) / 2)):
        start = reverse_seeds.pop()
        leng = reverse_seeds.pop()

        print(find_loc(start, leng, 'seed', map_data))
        # print(f"{start:,} {leng:,}")
        break

    return

    print('Part 2:', min(list(loc_list)))


if __name__ == '__main__':
    main()
