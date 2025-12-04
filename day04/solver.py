#!/usr/bin/env python

from aoc import utils
from aoc.cli import main
from aoc import geometry as geo


def parse(raw_data):
    return {
        k: v
        for k, v in utils.str_to_grid_dict(raw_data, keybuilder=geo.Vec).items()
        if v == "@"
    }


def solve1(data):
    count = 0
    for point in data:
        ns = [n for n in geo.neighbours8(point) if n in data]
        if len(ns) < 4:
            count += 1
    return count


def solve2(data):
    count = 0
    found = True
    while found:
        to_remove = []
        for point in data.keys():
            ns = [n for n in geo.neighbours8(point) if n in data]
            if len(ns) < 4:
                to_remove.append(point)
        found = len(to_remove) > 0
        count += len(to_remove)
        for p in to_remove:
            data.pop(p)
    return count



if __name__ == "__main__":
    main(parse, solve1, solve2)

