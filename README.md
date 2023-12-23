# Depth First Search for Graph and Tree Traversal

## Lab Objective
This lab focuses on implementing the Depth First Search (DFS) algorithm for graph and tree traversals using Python.

## Lab Description
Depth First Search (DFS) is a recursive searching algorithm that utilizes backtracking. It involves exhaustive searches of all nodes by going ahead, if possible, or backtracking when necessary. The recursive nature of DFS can also be implemented iteratively using a Last In First Out (LIFO) structure.

## Lab Tasks

### Implement for Graphs (Iteratively)
In this task, DFS is implemented iteratively. The algorithm is applied to graphs (`graph1` and `graph2`). The starting nodes are specified for each case.


### Implement for Trees (Recursively)
For this task, DFS is implemented recursively and trees (`root1` and `root2`) are traversed using the implemented DFS algorithm. The starting nodes are specified for each case.


## Output
Below are the expected outputs for each task.

### Output for Task 1 (Graphs)
```
# Output for Graph 1
[6, 4, 3, 2, 1, 5]

# Output for Graph 2
['E', 'A', 'B', 'D', 'C']
```

### Output for Task 2 (Trees)
```
# Output for Tree 1
Pre-order: [1, 2, 4, 5, 7, 8, 3, 6]

In-order: [4, 2, 7, 5, 8, 1, 3, 6]

Post-order: [4, 7, 8, 5, 2, 6, 3, 1]

# Output for Tree 2
Pre-order: [50, 17, 9, 14, 23, 19, 12, 76, 54, 67, 72]

In-order: [9, 14, 17, 19, 23, 12, 50, 54, 67, 76, 72]

Post-order: [14, 12, 19, 23, 17, 9, 67, 72, 54, 76, 50]
```

#
_Documented by ChatGPT_
