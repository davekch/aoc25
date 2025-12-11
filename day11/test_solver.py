import pytest
from solver import parse, solve1, solve2

TESTDATA = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

TESTDATA2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""

@pytest.fixture
def parsed_data():
    return parse(TESTDATA)


@pytest.fixture
def parsed_data2():
    return parse(TESTDATA2)


def test_parse():
    data = parse(TESTDATA)
    # asserts go here


# PART 1
def test_solve1(parsed_data):
    solution = solve1(parsed_data)
    assert solution == 5


# PART 2
def test_solve2(parsed_data2):
    solution = solve2(parsed_data2)
    assert solution == 2
