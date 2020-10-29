"""
This file contains implementation of calculating the sum of nodes in a tree.
Author: DtjiSoftwareDeveloper
"""


class Node:
    def __init__(self, value):
        # type: (int) -> None
        self.value: int = value
        self.left: Node or None = None
        self.right: Node or None = None

    def add_node(self, value):
        # type: (int) -> None
        if value == self.value:
            return  # Cannot add node
        elif value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.add_node(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.add_node(value)

    def sum(self):
        # type: () -> int
        if self is None:
            return 0
        else:
            if self.left is None and self.right is None:
                return self.value
            elif self.left is None and isinstance(self.right, Node):
                return self.value + self.right.sum()
            elif self.right is None and isinstance(self.left, Node):
                return self.value + self.left.sum()
            else:
                return self.value + self.left.sum() + self.right.sum()


# Test code
a_tree: Node = Node(5)
a_tree.add_node(7)
a_tree.add_node(4)
print(a_tree.sum())  # 16
a_tree.add_node(35)
a_tree.add_node(99)
a_tree.add_node(57)
print(a_tree.sum())  # 207
