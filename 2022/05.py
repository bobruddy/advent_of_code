#!/usr/bin/env python3

import string
import re

with open('05.input', 'r') as f:
    raw_data = [x for x in f.readlines()]

raw_stack = [x for x in raw_data if x.startswith('[')]
raw_moves = [x.strip() for x in raw_data if x.startswith('move')]
raw_stack_pos = [x for x in raw_data if x.startswith(' 1')].pop()

# build the stack
stack_num_list = [x for x in re.split(r'\s+', raw_stack_pos) if x.isnumeric()]
stack_position = {x: raw_stack_pos.index(x) for x in stack_num_list}

raw_stack.reverse()     # want to read from bottom up
stack: dict = {key: [] for key in stack_num_list}
for row in raw_stack:
    for sn in stack_num_list:
        if (v := row[stack_position[sn]]) in string.ascii_uppercase:
            stack[sn].append(v)

for m in raw_moves:
    a, num, b, src, c, dest = re.split(r'\s+', m)
    for i in range(int(num)):
        stack[dest].append(stack[src].pop())


# part 1
def get_part1(s: dict) -> str:
    d: str = ''
    for k in stack.keys():
        d += stack[k].pop()
    return (d)


e = get_part1(stack)
print('Part 1:', e)
