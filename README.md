# dsa-implement
Python package for implementation of common data structures and algorithms. 

## Data structures and algorithms

Data structures:
- Binary Search Tree
- Linked list
- Doubly linked list
- Stack
- Queue
- Max/Min Heap
- Graph
- Trie

Algorithms:
- Binary search
- Ternary search
- Bubble sort
- Count sort
- Insertion Sort
- Merge sort 
- Quick sort
- Radix sort
- Selection sort
- Shell sort

## Installation 
Install the package via pip symlinks.

```
conda env create -f environment.yml
conda activate dsa_env
pip install -e .
```

## Implementations

### Data structure example - binary search tree

```python
from dsaimplement.data_structures.BinarySearchTree import BinarySearchTree

# instantiate class
bst = BinarySearchTree()

# insert nodes
bst.insert(30)
bst.insert(20)
bst.insert(40)

# delete node
bst.delete(30)

# find minimum element
min_val = bst.find_min()

# find maximum element
max_val = bst.find_max()

# search for an element
found = bst.search(30)

# print elements in-order traversal
bst.in_order_traversal()

```

### Algorithm example - insertion sort
```python
from dsaimplement.algorithms.InsertionSort import insertionSort

# create array of values
arr = [-10, 30, 20, 50, 100]

# sort array using insertion sort
insertionSort(arr)

# print sorted array
print(arr)
```

