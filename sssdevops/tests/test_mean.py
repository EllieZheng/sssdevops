"""
This file is to test the mean function
"""


from sssdevops import mean
import pytest 


@pytest.mark.skip
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


def test_empty():
    with pytest.raises(ZeroDivisionError):
        mean([])


def test_type_error():
    with pytest.raises(TypeError):
        mean(5)


@pytest.mark.parametrize("num_list, expected_mean", [
    (   [1, 2, 3, 4, 5],     3.0    ),
    (   [2/3, 1/3],          0.5    ), 
    (   [1.2],               1.2    ),
])
def test_many(num_list, expected_mean):
    assert mean(num_list) == expected_mean
