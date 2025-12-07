#!/usr/bin/env python

from aoc import utils
from aoc.cli import main
from functools import cache
from collections import Counter


def parse(raw_data: str):
    fst, *rest = raw_data.splitlines()
    start = fst.find("S")
    return start, tuple(rest)


@cache
def solve(data):
    start, layers = data
    beams = Counter({start: 1}) # position of beams -> number of timelines
    splits = 0
    for layer in layers:
        new_beams = Counter()
        for beam, c in beams.items():
            if layer[beam] == "^":
                splits += 1
                new_beams[beam-1] += c
                new_beams[beam+1] += c
            else:
                new_beams[beam] += c
        beams = new_beams
    return splits, beams.total()


def solve1(data):
    solution, _ = solve(data)
    return solution


def solve2(data):
    _, solution = solve(data)
    return solution



if __name__ == "__main__":
    main(parse, solve1, solve2)

