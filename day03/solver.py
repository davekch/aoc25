#!/usr/bin/env python

from aoc import utils
from aoc.cli import main


def parse(raw_data):
    return [
        [int(i) for i in l]
        for l in raw_data.splitlines()
    ]


def solve1(data: list[list[int]]):
    result = 0
    for bank in data:
        digit1 = max(bank)
        index_digit1 = bank.index(digit1)
        if index_digit1 == len(bank) - 1:
            digit1 = max(bank[:-1])
            index_digit1 = bank.index(digit1)
        digit2 = max(bank[index_digit1+1:])
        result += 10*digit1 + digit2
    return result


def solve2(data):
    result = 0
    for bank in data:
        # print(bank)
        voltage = 0
        index = -1
        l = len(bank)
        for i in range(12):
            # print(f" {index+1}: {bank[index+1:l-(12-i)+1]}")
            digit = max(bank[index+1:l-(12-i)+1])
            index = bank[index+1:].index(digit) + index + 1
            # print(f"  {digit} @ {index}")
            # print(f"  {index}")
            voltage += 10**(11-i) * digit
        # print(voltage)
        result += voltage
    return result


if __name__ == "__main__":
    main(parse, solve1, solve2)

