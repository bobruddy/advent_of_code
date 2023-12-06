#!/usr/bin/env python3
"""
2023 Day 05 Solution
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


@lru_cache
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


def proccess_list_o_seeds(r):
    """
    Process a group of seeds
    """
    start_time = time.time()
    s = r[0]
    l = r[1]
    mdata = r[2]
    seed_r = r[3]
    bin_num = r[4]
    max_bin = r[5]
    min_val = None
    for b in range(s, l):
        m = find_loc('seed', b, mdata)[1]
        if (min_val is None) or (m < min_val):
            min_val = m

    end_time = time.time() - start_time
    print(f"Finished seed range {seed_r} bin number {bin_num:,} out of {max_bin:,} in {end_time:,}")
    return min_val


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
    a = [find_loc('seed', seed, (map_data))[1] for seed in orig_seeds]
    print('Part 1:', min(a))

    # part 2
    # making a list and reversing so can use pop
    reverse_seeds = list(orig_seeds)
    reverse_seeds.reverse()

    loc_list = []
    l_seeds = []
    chunk = 10000000
    for s_range in range(int(len(reverse_seeds) / 2)):
        start = reverse_seeds.pop()
        leng = reverse_seeds.pop()

        # this whole thing is breaking apart the task list
        # into 10MM chunks to process. Each chuck will then
        # be executed as a forked process in parallel
        num_bin = math.ceil(leng / chunk)
        for i in range(num_bin):
            inc_s = start + (i * chunk)
            inc_e = start + ((i + 1) * chunk)
            if (start + leng) < inc_e:
                inc_e = start + leng

            l_seeds.append((inc_s, inc_e, map_data, s_range, i, num_bin))

    with Pool(processes=(os.cpu_count() - 1)) as pool:
        loc_list = pool.map(proccess_list_o_seeds, l_seeds)

    print('Part 2:', min(list(loc_list)))


if __name__ == '__main__':
    main()
