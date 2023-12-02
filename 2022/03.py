#!/usr/bin/env python3

import string


def read_input(file):
    with open(file, "r") as f:
        return ([x.strip() for x in f.readlines()])


def split_items(packing_list):
    half_l = int(len(packing_list)/2)
    return (set(packing_list[:half_l]), set(packing_list[half_l:]))


def find_common(unique_items):
    x = unique_items[0].intersection(unique_items[1])
    return (x.pop())


def find_priority(com_letter):
    letters = string.ascii_lowercase + string.ascii_uppercase
    return (letters.index(com_letter) + 1)


# Part 1
input_data = read_input('03.input')
split_list = list(map(split_items, input_data))
common_list = list(map(find_common, split_list))
priority_list = list(map(find_priority, common_list))
print('Part 1:', sum(priority_list))

# Part 2


def find_badge(i_data):
    for i in range(int(len(input_data) / 3)):
        s1 = set(i_data.pop())
        s2 = set(i_data.pop())
        s3 = set(i_data.pop())
        s4 = s1.intersection(s2).intersection(s3)
        yield (s4.pop())


input_data = read_input('03.input')
badge_list = list(find_badge(input_data))
badge_priority = list(map(find_priority, badge_list))
print('Part 2:', sum(badge_priority))
