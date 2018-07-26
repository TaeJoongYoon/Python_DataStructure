# BinarySearchTree

"""
A Binary search trees (BST), sometimes called ordered or sorted binary trees, are a particular type of container:
data structures that store "items" (such as numbers, names etc.) in memory.

They allow fast lookup, addition and removal of items,
and can be used to implement either dynamic sets of items, or lookup tables that allow finding an item by its key.
"""


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    # Driver func
    def insert(self, elem):
        self.root = self._insert_value(self.root, elem)
        return self.root is not None

    # Recursive
    def _insert_value(self, node, elem):
        if node is None:
            node = Node(elem)
        else:
            if elem <= node.elem:
                node.left = self._insert_value(node.left, elem)
            else:
                node.right = self._insert_value(node.right, elem)
        return node

    # Driver func
    def find(self, key):
        return self._find_value(self.root, key)

    # Recursive
    def _find_value(self, root, key):
        if root is None or root.elem == key:
            return root is not None
        elif key <= root.elem:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    # Driver func
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    # Recursive
    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.elem:
            deleted = True
            if node.left and node.right:
                # replace the node to the leftmost of node.right
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent is not node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.elem:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted
