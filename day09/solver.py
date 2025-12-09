#!/usr/bin/env python

from aoc import utils
from aoc.cli import main
from aoc import geometry as g
from functools import cache


def parse(raw_data: str):
    return [g.Vec(*utils.ints(l)) for l in raw_data.splitlines()]


def solve1(data):
    result = 0
    for i, (x1, y1) in enumerate(data[:-1]):
        for (x2, y2) in data[i+1:]:
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area > result:
                result = area
    return result


def plot(data, ppp=None):
    grid = {p: "#" for p in data}
    # fill in green edges
    for p1, p2 in zip(data, data[1:] + [data[0]]):
        if p1.x == p2.x:
            for y in range(min(p1.y, p2.y) + 1, max(p1.y, p2.y)):
                grid[g.Vec(p1.x, y)] = "X"
        else:
            for x in range(min(p1.x, p2.x) + 1, max(p1.x, p2.x)):
                grid[g.Vec(x, p1.y)] = "X"

    import matplotlib.pyplot as plt
    plt.scatter([p.x for p in grid if grid[p]=="X"], [p.y for p in grid if grid[p]=="X"], color="green")
    plt.scatter([p.x for p in grid if grid[p]=="#"], [p.y for p in grid if grid[p]=="#"], color="red")
    if ppp:
        plt.scatter([x for x,_ in ppp], [y for _,y in ppp], color="blue")
    plt.show()


def solve2(data):
    result = 0
    # upper half
    xs, ys = 94601, 50063 # taken from looking at the input 😓
    for p in data:
        if p.y < ys:
            continue
        if not any(p.x < p2.x < xs and p.y > p2.y > ys for p2 in data):
            area = (abs(xs - p.x) + 1) * (abs(ys - p.y) + 1)
            if area > result:
                result = area
                ppp = [(xs, ys), (p.x, p.y)]
    # lower half
    xs, ys = 94601, 48705
    for p in data:
        if p.y > ys:
            continue
        if not any(p.x < p2.x < xs and p.y < p2.y < ys for p2 in data):
            area = (abs(xs - p.x) + 1) * (abs(ys - p.y) + 1)
            if area > result:
                result = area
                ppp = [(xs, ys), (p.x, p.y)]

    # print(result)
    # plot(data, ppp)
    return result


if __name__ == "__main__":
    main(parse, solve1, solve2)
