#!/usr/bin/env python3

def read_input(file):
    with open(file, "r") as f:
        return ([x.strip() for x in f.readlines()])


def return_sets(a):
    return (set(range(int(a[0]), int(a[1])+1)), set(range(int(a[2]), int(a[3])+1)))


# data prep
input_data = read_input('04.input')
expanded_data = list(map(lambda x: x.replace(',', '-').split('-'), input_data))
set_data = list(map(return_sets, expanded_data))

# part 1
is_subset = list(map(lambda st: st[0].issubset(
    st[1]) or st[1].issubset(st[0]), set_data))
filtered_is_subset = list(filter(lambda x: x is True, is_subset))
print("Part 1:", len(filtered_is_subset))

# part 2
is_intersection = list(map(lambda st: st[0].intersection(st[1]), set_data))
filtered_is_intersection = list(filter(lambda x: len(x) != 0, is_intersection))
print("Part 2:", len(filtered_is_intersection))
