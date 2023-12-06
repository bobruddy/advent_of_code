#!/usr/bin/env python3
"""
2023 Day 06 Solution

This is inefficient. you could check from each side to see where you go
positive and then not have to loop all the way. maybe I'll do that later
"""

import re
import sys
import os
from functools import lru_cache
from multiprocessing import Pool
import math
import time
import tqdm


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
    re_n = re.compile('\d+')
    re_metric = re.compile('^([a-zA-Z]+)')
    data = {}
    for row in base_data:
        m_itr = re_metric.search(row)
        metric = m_itr.group(0).lower()
        data[metric] = []

        a = list(re_n.finditer(row))
        for z in a:
            data[metric].append(int(z[0]))
    return data


def main():
    """
    Solves part1/part2
    """
    for arg in sys.argv:
        if arg.endswith('.input') and os.path.exists(arg):
            file = arg
            break
    parsed_data = parse_data(read_input(file))

    # part 1
    score: int = 1
    for race_num, total_time in enumerate(parsed_data['time']):
        rec_dist = parsed_data['distance'][race_num]
        distance_traveled = [ms * (total_time - ms) for ms in range(1, total_time + 1)]
        num_record = [x for x in distance_traveled if x > rec_dist]
        score = score * len(num_record)
    print('Part 1:', score)

    # part 2
    score: int = 1
    time_str: str = str()
    rec_dist_str: str = str()
    for race_num, total_time in enumerate(parsed_data['time']):
        dist = parsed_data['distance'][race_num]
        time_str = time_str + str(total_time)
        rec_dist_str = rec_dist_str + str(dist)
    p2_time = int(time_str)
    p2_rec_dist = int(rec_dist_str)
    print(p2_time, p2_rec_dist)

    distance_traveled = [ms * (p2_time - ms) for ms in tqdm.tqdm(range(1, p2_time + 1))]
    num_record = [x for x in tqdm.tqdm(distance_traveled) if x > p2_rec_dist]
    p2_score = score * len(num_record)
    print('Part 2:', p2_score)


if __name__ == '__main__':
    main()
