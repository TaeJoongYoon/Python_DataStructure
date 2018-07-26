# Stack

"""
A stack is an abstract data type that serves as a collection of elements

The order in which elements come off a stack gives rise to its alternative name, LIFO (last in, first out)
"""


class Stack(object):
    def __init__(self):
        self._stack = list()
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1

    # Using list's append method to add element
    def push(self, elem):
        self._stack.append(elem)
        self.top += 1

    # Using list's pop method to add element
    def pop(self):
        if self.is_empty():
            return self.empty_stack_exception()
        self.top -= 1
        return self._stack.pop()

    def peek(self):
        if self.is_empty():
            return self.empty_stack_exception()
        return self._stack[self.top]

    @staticmethod
    def empty_stack_exception():
        print("No element in the Stack")
