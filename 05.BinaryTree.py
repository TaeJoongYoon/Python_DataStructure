# BinaryTree

"""
A binary tree is a tree data structure in which each node has at most two children,
which are referred to as the left child and the right child.

A recursive definition using just set theory notions is that a (non-empty) binary tree is a tuple (L, S, R),
where L and R are binary trees or the empty set and S is a singleton set.

Some authors allow the binary tree to be the empty set as well.
"""


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.parent = None
        self.left = None
        self.right = None

    def make_left(self, elem):
        new_node = Node(elem)
        self.left = new_node
        new_node.parent = self

    def make_right(self, elem):
        new_node = Node(elem)
        self.right = new_node
        new_node.parent = self

    def remove_left(self):
        self.left = None

    def remove_right(self):
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def element(self, node):
        return node.elem

    def root(self):
        return self.root

    def is_root(self, node):
        return node is self.root

    def parent(self, node):
        return node.parent

    def left_child(self, node):
        return node.left

    def right_child(self, node):
        return node.right

    def sibling(self, node):
        p = node.parent
        if p.left is node:
            return p.right
        else:
            return p.left

    def is_internal(self, node):
        return node.left is not None and node.right is not None

    def is_external(self, node):
        return node.left is None and node.right is None

    def replace_element(self, node, elem):
        node.elem = elem
        return elem

    def swap_elements(self, node1, node2):
        tmp = node1.elem
        node1.elem = node2.elem
        node2.elem = tmp

    # Recursive
    def depth(self, node):
        if self.is_root(node):
            return 0
        else:
            return 1 + self.depth(self.parent(node))

    # Recursive
    def height(self, node):
        if self.is_external(node):
            return 0
        else:
            h = max(self.height(self.left_child(node)), self.height(self.right_child(node)))
            return 1 + h

    # BinaryPreOrder
    def pre_order(self, node):
        print(node.elem)
        if self.is_internal(node):
            self.pre_order(self.left_child(node))
            self.pre_order(self.right_child(node))

    # BinaryPostOrder
    def post_order(self, node):
        if self.is_internal(node):
            self.post_order(self.left_child(node))
            self.post_order(self.right_child(node))
        print(node.elem)

    # BinaryInOrder
    def in_order(self, node):
        if self.is_internal(node):
            self.in_order(self.left_child(node))
        print(node.elem)
        if self.is_internal(node):
            self.in_order(self.right_child(node))

    # LevelOrder, you should use Queue.
