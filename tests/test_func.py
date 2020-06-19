import pytest
from app.add_func import my_add

# python -m pytest from root dir to run tests


NUMBER_1 = 3.0
NUMBER_2 = 2.0


def test_my_add():
    value = my_add(NUMBER_1, NUMBER_2)
    assert value == 5
