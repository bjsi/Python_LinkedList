import pytest
from lib import my_add


NUMBER_1 = 3.0
NUMBER_2 = 2.0


def test_my_add():
    value = my_add(NUMBER_1, NUMBER_2)
    assert value == 5
