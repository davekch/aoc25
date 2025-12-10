#!/usr/bin/env python

from aoc import utils
from aoc.cli import main
from itertools import combinations
from operator import xor
from functools import reduce


def parse(raw_data: str):
    machines = []
    for line in raw_data.splitlines():
        config, *rest, joltage = line.split()
        l = len(config) - 2
        config = int("".join(["0" if c == "." else "1" for c in config[1:-1]]), base=2)
        joltage = utils.ints(joltage)
        buttons = []
        for r in rest:
            idx = utils.ints(r)
            bin_digits = ["0"] * l
            for i in idx:
                bin_digits[i] = "1"
            buttons.append(int("".join(bin_digits), base=2))
        machines.append((config, buttons, joltage))
    return machines


def repr_machine(config, buttons, joltage):
    rconfig = f"[{config:b}]"
    rbuttons = " ".join([f"({b:b})" for b in buttons])
    return f"{rconfig} {rbuttons} {joltage}"


def min_presses(config, buttons):
    for n in range(1, len(buttons) + 1):
        for pressed in combinations(buttons, n):
            if reduce(xor, pressed) == config:
                return n


def solve1(data):
    presses = 0
    for config, buttons, _ in data:
        # print(repr_machine(config, buttons, _))
        presses += min_presses(config, buttons)
    return presses


def solve2(data):
    pass


if __name__ == "__main__":
    main(parse, solve1, solve2)

