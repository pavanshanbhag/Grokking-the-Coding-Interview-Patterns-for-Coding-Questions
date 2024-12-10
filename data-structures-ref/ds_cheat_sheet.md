# Data Structures

## Array

### Definition
- Stores data elements based on a sequential, most commonly 0-based, index.
- Based on tuples from set theory.
- One of the oldest and most commonly used data structures.

### What You Need to Know
- Optimal for indexing; less efficient for searching, inserting, and deleting (except at the end).
- Linear arrays (one-dimensional arrays) are the most basic form.
- Static in size, meaning they are declared with a fixed size.
- Dynamic arrays can grow by copying contents to a larger array when full.
- Multi-dimensional arrays (nested arrays) allow for multiple dimensions, such as a 2D array representing x, y coordinates.

### Time Complexity
- **Indexing**: 
  - Linear array: O(1)
  - Dynamic array: O(1)
- **Search**: 
  - Linear array: O(n)
  - Dynamic array: O(n)
- **Optimized Search**: 
  - Linear array: O(log n) (if sorted)
  - Dynamic array: O(log n) (if sorted)
- **Insertion**: 
  - Linear array: n/a
  - Dynamic array: O(n) (when resizing is needed)

## Linked List

### Definition
- Stores data with nodes that point to other nodes.
- Each node contains one datum and one reference (to another node).

### What You Need to Know
- Optimized for insertion and deletion; slower at indexing and searching.
- Doubly linked list: Nodes reference both the next and previous nodes.
- Circularly linked list: The last node references the first node.
- Stacks (LIFO) and queues (FIFO) can be implemented using linked lists or arrays.

### Time Complexity
- **Indexing**: O(n)
- **Search**: O(n)
- **Append**: O(1)
- **Prepend**: O(1)
- **Insertion**: O(n) (if inserting at a specific position)

## Hash Table (Hash Map)

### Definition
- Stores data with key-value pairs.
- Hash functions map keys to unique addresses in memory.

### What You Need to Know
- Optimized for searching, insertion, and deletion.
- Hash collisions occur when a hash function returns the same output for two distinct inputs.
- Important for associative arrays and database indexing.

### Time Complexity
- **Indexing**: O(1)
- **Search**: O(1)
- **Insertion**: O(1)

## Binary Tree

### Definition
- A tree-like data structure where each node has at most two children (left and right).

### What You Need to Know
- Optimized for searching and sorting.
- A degenerate tree (unbalanced) behaves like a linked list.
- Binary Search Trees (BST) use keys to determine the position of child nodes:
  - Left child has a key smaller than its parent node.
  - Right child has a key greater than its parent node.
  - No duplicate nodes allowed.

### Time Complexity
- **Indexing**: O(log n) (for balanced trees)
- **Search**: O(log n) (for balanced trees)
- **Insertion**: O(log n) (for balanced trees)


# Aditional Data Structures
## Heap

### Definition
- A specialized tree-based data structure that satisfies the heap property.
- In a max heap, for any given node I, the value of I is greater than or equal to the values of its children.
- In a min heap, the value of I is less than or equal to the values of its children.

### What You Need to Know
- Used to implement priority queues.
- Efficiently supports finding the maximum or minimum element.

### Time Complexity
- **Insertion**: O(log n)
- **Deletion**: O(log n)
- **Peek (find max/min)**: O(1)

## Graph

### Definition
- A collection of nodes (vertices) and edges connecting pairs of nodes.
- Can be directed or undirected.

### What You Need to Know
- Used to represent networks, such as social networks, computer networks, and transportation systems.
- Common algorithms include Depth-First Search (DFS), Breadth-First Search (BFS), Dijkstra's algorithm, and A* algorithm.

### Time Complexity
- **Adjacency List**:
  - Space: O(V + E)
  - Time (DFS/BFS): O(V + E)
- **Adjacency Matrix**:
  - Space: O(V^2)
  - Time (DFS/BFS): O(V^2)

## Trie (Prefix Tree)

### Definition
- A tree-like data structure that stores a dynamic set of strings, where keys are usually strings.

### What You Need to Know
- Used for efficient retrieval of a key in a dataset of strings.
- Commonly used in autocomplete and spell-checking applications.

### Time Complexity
- **Insertion**: O(m) where m is the length of the key.
- **Search**: O(m) where m is the length of the key.

## AVL Tree

### Definition
- A self-balancing binary search tree where the difference between heights of left and right subtrees cannot be more than one for all nodes.

### What You Need to Know
- Ensures O(log n) time complexity for search, insertion, and deletion operations.
- Balances itself after every insertion and deletion.

### Time Complexity
- **Insertion**: O(log n)
- **Deletion**: O(log n)
- **Search**: O(log n)

## Red-Black Tree

### Definition
- A self-balancing binary search tree with an extra bit of storage per node: its color, which can be either red or black.

### What You Need to Know
- Ensures the tree remains balanced, providing O(log n) time complexity for search, insertion, and deletion.
- Used in many libraries and frameworks, such as the TreeMap in Java.

### Time Complexity
- **Insertion**: O(log n)
- **Deletion**: O(log n)
- **Search**: O(log n)

# Search Algorithm