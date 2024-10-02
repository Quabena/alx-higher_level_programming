#!/usr/bin/python3
"""This module defines a Node and SinglyLinkedList class.

The Node class represents a node in a singly linked list.
The SinglyLinkedList class manages the linked list operations.
"""


class Node:
    """A class that defines a node in a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node or None): The next node in the list.
    """

    def __init__(self, data, next_node=None):
        """Initialize a new node instance.

        Args:
            data (int): The data of the node.
            next_node (Node or None): The next node. Defaults to None.

        Raises:
            TypeError: If data is not an integer or
            next_node is not a Node.
        """
        self.data = data  # Use the setter to validate data
        self.next_node = next_node  # Use the setter to validate next_node

    @property
    def data(self):
        """int: The data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value (int): The data of the node.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Node or None: The next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node of the current node.

        Args:
            value (Node or None): The next node.

        Raises:
            TypeError: If next_node is not None or a Node.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """Return a string representation of the list."""
        current = self.__head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """Insert a new Node into the list in sorted order.

        Args:
            value (int): The data for the new Node.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < new_node.data:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
