#!/usr/bin/python3

"""Define classes for a singly-linked list."""

class Node:
    """singly-linked list node"""
    def __init__(self, data, next_node=None):
        """init new node
        
        Args:
            data (int): data of node
            next_node: the next node of the current node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter to retrieve data"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter to retrieve next node"""
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Singly Linked List"""
    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the SinglyLinkedList.

        inserts a new Node into the correct sorted
        position in the list (increasing order)

        Args:
            value (Node): Node to be inserted.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            new_node.next_node = None
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp_node = self.__head
            while (tmp_node.next_node is not None
                   and tmp_node.next_node.data < value):
                tmp_node = tmp_node.next_node
            new_node.next_node = tmp_node.next_node
            tmp_node.next_node = new_node

    def __str__(self):
        vals = []
        tmp_node = self.__head
        while tmp_node is not None:
            vals.append(tmp_node.data)
            tmp_node = tmp_node.next_node
        return ('\n'.join(vals))
