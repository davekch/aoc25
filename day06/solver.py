#!/usr/bin/env python

from aoc import utils
from aoc.cli import main
from operator import add, mul
from functools import reduce


def parse(raw):
    symbols = {
        "+": add,
        "*": mul,
    }
    *numberlines, opline = raw.splitlines()
    ops = [symbols[o] for o in opline.split()]
    return numberlines, ops


def parse1(preparsed):
    numberlines, ops = preparsed
    numbers = [utils.ints(l) for l in numberlines]
    return zip(*numbers, ops)


def solve1(data):
    data = parse1(data)
    result = 0
    for calc in data:
        *numbers, op = calc
        result += reduce(op, numbers)
    return result


def parse2(preparsed):
    numberlines, ops = preparsed
    # transpose numberlines
    numberstext = "\n".join(["".join(l).strip() for l in zip(*numberlines)])
    numbers = [utils.ints(b) for b in numberstext.split("\n\n")]
    return zip(numbers, ops)


def solve2(data):
    data = parse2(data)
    result = 0
    for numbers, op in data:
        result += reduce(op, numbers)
    return result


if __name__ == "__main__":
    main(parse, solve1, solve2)

