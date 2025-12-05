#!/usr/bin/env python

from aoc import utils
from aoc.cli import main


def parse(raw_data):
    range_data, id_data = raw_data.split("\n\n")
    ranges = []
    for line in range_data.splitlines():
        a, b = line.split("-")
        ranges.append((int(a), int(b)))
    ids = utils.ints(id_data)
    return ranges, ids


def solve1(data):
    count = 0
    ranges, ids = data
    for i in ids:
        if any(a <= i <= b for a, b in ranges):
            count += 1
    return count


def reduce_ranges(ranges: list[tuple[int, int]]):
    """
    merges all overlapping adjacent ranges until there are no more overlaps
    """
    i = 0
    while i + 1 < len(ranges):
        (a1, b1), (a2, b2) = ranges[i], ranges[i+1]
        if a1 <= a2 <= b1:
            if b2 > b1:
                ranges[i] = (a1, b2)
                ranges.pop(i+1)
            else:
                ranges.pop(i+1)
        else:
            i += 1

    return ranges


def solve2(data):
    ranges, _ = data
    ranges = sorted(ranges)
    reduce_ranges(ranges)
    return sum([b-a+1 for a, b in ranges])



if __name__ == "__main__":
    main(parse, solve1, solve2)

