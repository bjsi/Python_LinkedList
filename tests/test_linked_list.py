import pytest
from app.linked_list import List, Node

# python -m pytest from root dir to run tests


def test_create_list_list_is_empty():
    lis = List()
    assert lis.length() == 0


def test_create_list_list_head_is_None():
    lis = List()
    assert lis.head is None


def test_create_node_node_not_None():
    node = Node(5)
    assert node is not None


def test_create_node_node_data_correct():
    node = Node(5)
    assert node.data == 5
