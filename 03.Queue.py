# Queue

"""
A queue is a particular kind of abstract data type or collection in which the entities
in the collection are kept in order and the principal (or only) operations on the collection are
the addition of entities to the rear terminal position, known as enqueue,
and removal of entities from the front terminal position, known as dequeue.

This makes the queue a First-In-First-Out (FIFO) data structure.

In a FIFO data structure, the first element added to the queue will be the first one to be removed.
"""


class Queue(object):
    def __init__(self):
        self._queue = list()
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def size(self):
        return self.rear - self.front

    # Use list's append method to add element
    def enqueue(self,elem):
        self._queue.append(elem)
        self.rear += 1

    # Use list's pop method to add element with 0 index
    def dequeue(self):
        if self.is_empty():
            return self.empty_queue_exception()
        self.front += 1
        return self._queue.pop(0)

    @staticmethod
    def empty_queue_exception():
        print("No element in the Queue")
