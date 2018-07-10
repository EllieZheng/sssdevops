"""
This file is to test the mean function
"""


from sssdevops import mean
import pytest 


def test_simple():
    num_list = [1, 2]
    observed = mean(num_list)
    expected = 1.5
    assert observed == expected


@pytest.fixture # tell pytest that return a new, clean resource
def num_list():
    return [1, 2, 3, 4, 5]


def test_more(num_list): # pytest will scan for all the fixtures and search for num_lists
    assert mean(num_list) == 3.0
