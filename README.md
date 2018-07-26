# Python_DataStructure

##### Data Structures of Python.
##### These codes are what I was studing about Python Data Structure(abstract data type).
</br>

### 01.[Doubly Linked List](https://github.com/TaeJoongYoon/Python_DataStructure/blob/master/01.DoublyLinkedList.py)
<hr>

A **doubly linked list** is a linked data structure that consists of a set of sequentially linked records called nodes.

Each node contains two fields, called **links**, that are references to the previous and to the next node in the sequence of nodes.

The beginning and ending nodes' previous and next links, respectively, point to some kind of terminator, typically a sentinel node or **null**, to facilitate traversal of the list.

If there is only one sentinel node, then the list is circularly linked via the sentinel node.

It can be conceptualized as **two singly linked lists** formed from the same data items, but in opposite sequential orders

</br>

### 02.[Stack](https://github.com/TaeJoongYoon/Python_DataStructure/blob/master/02.Stack.py)
<hr>

A **stack** is an abstract data type that serves as a collection of elements, with two principal operations:

- push, which adds an element to the collection, and
- pop, which removes the most recently added element that was not yet removed.

The order in which elements come off a stack gives rise to its alternative name, **LIFO (last in, first out)**. 

</br>

### 03.[Queue](https://github.com/TaeJoongYoon/Python_DataStructure/blob/master/03.Queue.py)
<hr>

A **queue** is a particular kind of abstract data type or collection in which the entities in the collection are kept in order and the principal (or only) operations on the collection are the addition of entities to the rear terminal position, known as enqueue, and removal of entities from the front terminal position, known as dequeue.

This makes the queue a **FIFO (first in, first out)** data structure.

</br>

### 04.[Deque](https://github.com/TaeJoongYoon/Python_DataStructure/blob/master/04.Deque.py)
<hr>

A **double-ended queue (abbreviated to deque)** is an abstract data type that generalizes a queue, for which elements can be added to or removed from either the **front (head)** or **back (tail)**.

It is also often called a head-tail linked list, though properly this refers to a specific data structure implementation of a deque

</br>

### 05.[BinaryTree](https://github.com/TaeJoongYoon/Python_DataStructure/blob/master/05.BinaryTree.py)
<hr>

A **binary tree** is a tree data structure in which each node has at most two children, which are referred to as **the left child and the right child**.

A recursive definition using just set theory notions is that a (non-empty) binary tree is a tuple (L, S, R), where L and R are binary trees or the empty set and S is a singleton set.

Some authors allow the binary tree to be the empty set as well.

</br>

### 06.[BinarySearchTree](https://github.com/TaeJoongYoon/Python_DataStructure/blob/master/06.BinarySearchTree.py)
<hr>

A **Binary search trees (BST)**, sometimes called ordered or **sorted binary trees**, are a particular type of container:

data structures that store "items" (such as numbers, names etc.) in memory.

They allow fast lookup, addition and removal of items, and can be used to implement either dynamic sets of items, or lookup tables that allow finding an item by **its key**.

</br>

### 07.[Graph](https://github.com/TaeJoongYoon/Python_DataStructure/blob/master/07.Graph.py)
<hr>

A **graph** is an abstract data type that is meant to implement the undirected graph and directed graph concepts from mathematics, specifically the field of graph theory.

A graph data structure consists of a finite (and possibly mutable) set of **vertices** or nodes or points, together with a set of unordered pairs of these vertices for an undirected graph or a set of ordered pairs for a directed graph.

These pairs are known as edges, **arcs**, or lines for an undirected graph and as arrows, directed edges, directed arcs, or directed lines for a directed graph.

</br>
</br>

### Reference (by Wiki)
<hr>

[Doubly Linked List](https://en.wikipedia.org/wiki/Doubly_linked_list)

[Stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))

[Queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))

[Deque](https://en.wikipedia.org/wiki/Double-ended_queue)

[BinaryTree](https://en.wikipedia.org/wiki/Binary_tree)

[BinarySearchTree](https://en.wikipedia.org/wiki/Binary_search_tree)

[Graph](https://en.wikipedia.org/wiki/Graph_(abstract_data_type))
