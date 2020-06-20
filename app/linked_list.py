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

    def add(self, node: Node) -> None:
        """
        Add a node to the list.
        :returns: None.
        """

        tail = self.get_tail()
        if tail is None:
            self.head = node
            return
        tail.next = node

    def get_tail(self) -> Optional[Node]:
        """
        Get the last element in the list.
        :returns: Node or None.
        """

        if self.head is None:
            return None

        cur = self.head
        while cur.next is not None:
            cur = cur.next
        return cur
