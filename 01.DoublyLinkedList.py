# Doubly Linked List with header and trailer

"""
A linked data structure that consists of a set of sequentially linked records called nodes.

Each node contains two fields, called links, that are references to the previous and
to the next node in the sequence of nodes.
"""


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None


class DoublyLinkedList(object):
    def __init__(self):
        self.header = Node(0)
        self.trailer = Node(0)
        self.size = 0

        self.header.next = self.trailer
        self.trailer.prev = self.header

    def is_empty(self):
        return self.header.next is self.trailer

    # Traverse the Doubly Linked list
    def traverse_list(self):
        node = self.header.next
        while node is not self.trailer:
            print(node.elem)
            node = node.next

    # Adding data element at the end
    def append(self, elem):
        prev_node = self.trailer.prev

        new_node = Node(elem)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next.prev = new_node
        self.size += 1

    # Inserting data element at the index
    def insert_at(self, index, elem):
        if index >= self.size:
            return self.invalid_index_exception()

        prev_node = self.header
        for _ in range(0, index):
            prev_node = prev_node.next

        new_node = Node(elem)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next.prev = new_node
        self.size += 1

    def remove_at(self, index):
        if index >= self.size:
            return self.invalid_index_exception()

        node = self.header.next
        for _ in range(0, index):
            node = node.next

        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    @staticmethod
    def invalid_index_exception():
        print("Invaild index")
