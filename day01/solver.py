#!/usr/bin/env python

from pathlib import Path
from aoc import utils
from aoc.cli import main


def parse(raw_data: str):
    return [
       int(n.replace("L", "-").replace("R", "+"))
       for n in raw_data.splitlines()
    ]


def solve1(data):
    pwd = 0
    start = 50
    for n in data:
        start = (start + n) % 100
        if start == 0:
            pwd += 1
    return pwd


# def solve2(data):
#     pwd = 0
#     start = 50
#     for n in data:
#         add = abs((start + n) // 100)
#         if add > 0 and start == 0 and n < 0:
#             add -= 1
#         if start == -n:
#             add += 1
#         print(f"{start} {n} -> {add}")
#         pwd += add
#         start = (start + n) % 100
#         # if start == 0:
#         #     pwd += 1

#     return pwd

def solve2(data):
    pwd = 0
    start = 50
    for n in data:
        # print(f"{start} {n}")
        for _ in range(abs(n)):
            start = (start + utils.sign(n)) % 100
            # print(f"  {start}")
            if start == 0:
                pwd += 1
    return pwd


if __name__ == "__main__":
    main(parse, solve1, solve2)

