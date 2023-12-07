#!/usr/bin/env python3
"""
2023 Day 07 Solution

"""

import re
import sys
import os
from functools import lru_cache
from multiprocessing import Pool
import math
import time
import tqdm
from collections import Counter
from operator import itemgetter


def read_input(file: str) -> list:
    """
    Read and parse input
    """
    with open(file, 'r', encoding="utf-8") as fd:
        return (x.strip() for x in fd.readlines())


def parse_data(base_data: list) -> tuple:
    """
    Parse raw data
    """
    return ((x.split(' ')[0], int(x.split(' ')[1])) for x in base_data)


@lru_cache
def p1_find_type(hand: str) -> int:
    """
    Find type of the hand return int with 0 being the worst
    """
    h_type = Counter(hand)

    h_values = h_type.values()
    if 5 in h_values:
        return 6
    if 4 in h_values:
        return 5
    if 3 in h_values and 2 in h_values:
        return 4
    if 3 in h_values:
        return 3
    if 2 == len(tuple(filter(lambda x: x == 2, h_values))):
        return 2
    if 2 in h_values:
        return 1
    return 0


@lru_cache
def p2_find_type(hand: str) -> int:
    """
    Find type of the hand return int with 0 being the worst
    """
    h_type = Counter(hand)

    if (num_joker := h_type.get('J')) is None:
        return p1_find_type(hand)

    # get all values
    h_values = h_type.values()
    num_of_twos = len(tuple(filter(lambda x: x == 2, h_values)))

    # 5 of a kind -> 6
    if len(h_values) <= 2:
        return 6

    # 4 of a kind -> 5
    if num_joker >= 3:
        return 5
    if num_of_twos == 2 and num_joker == 2:
        return 5
    if max(h_values) >= 3 and num_joker == 1:
        return 5

    # full house -> 4
    if 3 in h_values and num_joker <= 2:
        return 4
    if num_of_twos == 2 and num_joker == 1:
        return 4

    # 3 of a kind -> 3
    if max(h_values) >= 3 or num_joker == 2:
        return 3
    if num_joker == 1 and max(h_values) == 2:
        return 3

    # two pairs -> 2
    if num_of_twos == 2:
        print('should never get two two pairs of twos')
        return 2
    if 2 in h_values and num_joker == 1:
        print('should never get here. this should be a 3 of a kind')
        return 2

    # one pair -> 1
    return 1


@lru_cache
def find_high_card(hand: str, card_ranking: tuple) -> tuple:
    """
    Figure our rank of high cards by position of card in hand. lowest is worst
    """
    c_rank = list(card_ranking)
    c_rank.reverse()
    return tuple(c_rank.index(x) for x in hand)


def sort_hands(hands: list):
    """
    Rank all the hands by order
    """
    for t in sorted({x[2] for x in hands}):
        t_hands = tuple(filter(lambda x: x[2] == t, hands))
        s_hands = sorted(t_hands, key=itemgetter(3, 4, 5, 6, 7))

        for i in s_hands:
            yield i


def main():
    """
    Solves part1/part2
    """
    for arg in sys.argv:
        if arg.endswith('.input') and os.path.exists(arg):
            file = arg
            break

    # part 1
    p1_parsed_data = parse_data(read_input(file))
    p1_ranking = ('A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2')
    p1_hands = tuple((hand, bid, p1_find_type(hand)) + find_high_card(hand, p1_ranking) for hand, bid in p1_parsed_data)
    p1_scores = tuple((rank + 1) * hand[1] for rank, hand in enumerate(sort_hands(p1_hands)))
    print('Part 1:', sum(p1_scores))

    # part 2
    p2_parsed_data = parse_data(read_input(file))
    p2_ranking = ('A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J')
    p2_hands = tuple((hand, bid, p2_find_type(hand)) + find_high_card(hand, p2_ranking) for hand, bid in p2_parsed_data)
    p2_scores = tuple((rank + 1) * hand[1] for rank, hand in enumerate(sort_hands(p2_hands)))
    print('Part 2:', sum(p2_scores))


if __name__ == '__main__':
    main()
