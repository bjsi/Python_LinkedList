from typing import Any, Optional


class Node:

    """
    Represents an element in a singly linked list.
    """

    data: Any
    next: Optional["Node"]

    def __init__(self, data: Any):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"<Node: data: {self.data} next: {self.next}>"


class List:

    """
    Represents a singly linked list.
    """

    head: Optional["Node"]

    def __init__(self):
        self.head = None

    def length(self) -> int:
        """
        Get the number of Nodes in the List.
        :returns: number of Nodes or -1.
        """

        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count
