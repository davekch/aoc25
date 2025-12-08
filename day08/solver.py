#!/usr/bin/env python

from aoc import utils
from aoc.cli import main
import aoc.geometry as g


def parse(raw_data: str):
    return [g.Vec(*utils.ints(l)) for l in raw_data.splitlines()]


def solve1(data: list[g.Vec], n=1000):
    # calculate shortest distances between all pairs
    dists = []   # list of (dist, vec1, vec2)
    for i, v1 in enumerate(data[:-1]):
        for j in range(i+1, len(data)):
            v2 = data[j]
            dists.append((v1.dist2(v2), v1, v2))
    dists = sorted(dists)

    circuits = [set([v]) for v in data]
    for i, (_, v1, v2) in enumerate(dists):

        if i == n:
            # part 1
            sizes = sorted(list(map(len, circuits)), reverse=True)
            # print(sizes)
            s1, s2, s3, *_ = sizes
            yield s1 * s2 * s3

        alter = []  # these are the cirtuit(s) to which v1 and v2 belong
        for circuit in circuits:
            if v1 in circuit or v2 in circuit:
                alter.append(circuit)
        # if there are two circuits in alter, we need to join those
        # to one big circuit. otherwise, just add the points or make a new
        if len(alter) == 1:
            # one of v1, v2 was already connected, add the other one
            alter[0].add(v1)
            alter[0].add(v2)
        elif len(alter) == 2:
            c1, c2 = alter
            # merge c2 into c1
            c1.update(c2)
            circuits.remove(c2)
        else:
            raise NotImplementedError("gaah")
        if len(circuits) == 1:
            break

    yield v1.x * v2.x


if __name__ == "__main__":
    main(parse, solve1)
