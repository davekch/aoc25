#!/usr/bin/env python

from aoc import utils
from aoc.cli import main


def parse(raw_data):
    ranges = []
    for ids in raw_data.split(","):
        a,b = ids.split("-")
        ranges.append((int(a), int(b)))
    return ranges


def is_valid_p1(i):
    s = str(i)
    l = len(s)
    return not (l % 2 == 0 and s[:l//2] == s[l//2:])


def solve1(data):
    result = 0
    for a, b in data:
        for i in range(a, b+1):
            if not is_valid_p1(i):
                # print(i)
                result += i
    return result


def is_valid_p2(i):
    def is_pattern(s, pattern):
        if len(s) < len(pattern):
            return False
        if s == pattern * (len(s)//len(pattern)):
            return True
        return is_pattern(s[1:], pattern + s[0])

    s = str(i)
    return not is_pattern(s[1:], s[0])


def solve2(data):
    result = 0
    for a, b in data:
        for i in range(a, b+1):
            if not is_valid_p2(i):
                # print(i)
                result += i
    return result


if __name__ == "__main__":
    main(parse, solve1, solve2)

