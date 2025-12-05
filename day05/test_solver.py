import pytest
from solver import parse, solve1, solve2

TESTDATA = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

@pytest.fixture
def parsed_data():
    return parse(TESTDATA)


def test_parse():
    data = parse(TESTDATA)
    # asserts go here


# PART 1
def test_solve1(parsed_data):
    solution = solve1(parsed_data)
    assert solution == 3


# PART 2
def test_solve2(parsed_data):
    solution = solve2(parsed_data)
    assert solution == 14
