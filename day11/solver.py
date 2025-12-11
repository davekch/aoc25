#!/usr/bin/env python

from aoc import utils
from aoc.cli import main
from functools import cache


def parse(raw_data: str):
    connections = {}
    for line in raw_data.splitlines():
        comp, cons = line.split(":")
        connections[comp] = cons.split()
    return connections


def count_paths(graph, start, finish):
    if start == finish:
        return 1
    total = 0
    for c in graph[start]:
        total += count_paths(graph, c, finish)
    return total


def solve1(data):
    return count_paths(data, "you", "out")


def solve2(data):

    @cache
    def count_bug_paths(start, finish, seen_dac, seen_fft):
        if start == finish:
            if seen_dac and seen_fft:
                return 1
            else:
                return 0
        elif start == "dac":
            seen_dac = True
        elif start == "fft":
            seen_fft = True
        total = 0
        for c in data[start]:
            total += count_bug_paths(c, finish, seen_dac, seen_fft)
        return total

    return count_bug_paths("svr", "out", False, False)


if __name__ == "__main__":
    main(parse, solve1, solve2)

