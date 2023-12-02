#!/usr/bin/env python3

import re

with open('01.input', 'r') as input:
    raw_input = [x.strip() for x in input.readlines()]


# return only calibration number
def return_cal(cal_str: str) -> int:
    num_only = re.sub(r"[^\d]", '', cal_str)
    return int(str(num_only[0]) + str(num_only[-1]))


# part 1
print('Part 1:', sum(list(map(return_cal, raw_input))))


# part 2
def replace_words(cal_str: str) -> str:
    replace_str = cal_str.lower()
    word_map = (
        ('three', '3'),
        ('seven', '7'),
        ('eight', '8'),
        ('four', '4'),
        ('five', '5'),
        ('nine', '9'),
        ('one', '1'),
        ('two', '2'),
        ('six', '6'),
    )
    for word, digit in word_map:
        replace_str = replace_str.replace(word, digit)
    return replace_str


def swap_w_digits(raw_str: str) -> str:
    """
    Check for number words coming in from left and right
    one character at a time. Otherwise something like
    eightwoakdfaldfj4 could be found as eigh2akdfaldfj4
    instead of 8woakdfaldfj4
    """
    orig_str = raw_str.lower()
    stop_r = False
    stop_l = False
    for i in range(len(orig_str)):
        if stop_r and stop_l:
            return str(orig_str)

        if orig_str[-i-1].isdigit() or stop_r:
            stop_r = True

        if orig_str[i].isdigit() or stop_l:
            stop_l = True

        if not stop_l:
            l_str = orig_str[:i+1]
            if (l_match := replace_words(l_str)) != l_str:
                orig_str = l_match + orig_str[i+1:]
                stop_l = True

        if not stop_r:
            r_str = orig_str[-i-1:]
            if (r_match := replace_words(r_str)) != r_str:
                orig_str = orig_str[:-i-1] + r_match
                stop_r = True
    return str(orig_str)


parsed_raw = list(map(swap_w_digits, raw_input))
print('Part 2:', sum(list(map(return_cal, parsed_raw))))
