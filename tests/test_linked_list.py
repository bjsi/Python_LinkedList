import pytest
from app.linked_list import List, Node
import random

# python -m pytest from root dir to run tests


def test_get_tail_returns_tail():
    lis = List()
    node = Node(1)
    lis.add(node)
    assert lis.get_tail() == node


def test_add_node_list_length_is_one():
    lis = List()
    node = Node(1)
    lis.add(node)
    assert lis.length() == 1


def test_add_n_nodes_length_is_n():
    lis = List()
    expected = random.randint(0, 100)
    for n in range(expected):
        node = Node(n)
        lis.add(node)
    assert lis.length() == expected


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


def test_iter_empty_list():
    lis = List()
    output = None
    for x in lis:
        output = x
    assert output is None


def test_iter_singleton_list():
    lis = List()
    node = Node(1)
    lis.add(node)
    for x in lis:
        output = x
    assert output is not None
    assert output is node

