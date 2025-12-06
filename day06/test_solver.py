import pytest
from solver import parse, solve1, solve2

TESTDATA = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
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
    assert solution == 4277556


# PART 2
def test_solve2(parsed_data):
    solution = solve2(parsed_data)
    assert solution == 3263827
