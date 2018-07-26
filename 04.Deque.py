# Deque (Double-ended queue)

"""
A double-ended queue (abbreviated to deque) is an abstract data type that generalizes a queue,
for which elements can be added to or removed from either the front (head) or back (tail).

It is also often called a head-tail linked list,
though properly this refers to a specific data structure implementation of a deque
"""


class Deque(object):
    def __init__(self):
        self._deque = list()
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def size(self):
        return self.rear - self.front

    def push(self, elem):
        self.rear += 1
        self._deque.insert(0, elem)

    def pop(self):
        if self.is_empty():
            return self.empty_deque_exception()
        self.front += 1
        return self._deque.pop(0)

    def inject(self, elem):
        self.rear += 1
        self._deque.append(elem)

    def eject(self):
        if self.is_empty():
            return self.empty_deque_exception()
        self.front += 1
        return self._deque.pop()

    @staticmethod
    def empty_deque_exception():
        print("No element in the Deque")
