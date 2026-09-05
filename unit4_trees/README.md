Unit 4 Discussion: Binary Search Trees

Overview

This assignment introduced Binary Search Trees (BSTs) and recursive tree operations.

Learning Objectives

Built a BST

Inserted values recursively

Searched recursively

Performed in-order traversal

Examined BST organization and search efficiency

Implementation Summary

The program was completed as an employee ID lookup example. Seven employee ID values were inserted into a Binary Search Tree using recursive insertion. Values smaller than a node were placed in the left subtree, while larger values were placed in the right subtree.

The completed program:

Built a BST containing seven employee ID values.

Inserted values recursively into both left and right subtrees.

Performed an in-order traversal and displayed the IDs in ascending order.

Searched for two values that existed and two values that did not exist.

Demonstrated an empty-tree edge case.

Included comments explaining BST insertion, recursive search, traversal, and search-space reduction.

Values Used

The following employee IDs were inserted:

1050, 1025, 1075, 1010, 1040, 1060, 1090

The resulting in-order traversal was:

1010, 1025, 1040, 1050, 1060, 1075, 1090

Search Tests

The program searched for:

1025 — found

1090 — found

1000 — not found

1080 — not found

Edge Case

An empty BST was created and tested. Its in-order traversal returned an empty list, and searching the empty tree returned False. This demonstrated the recursive base case where reaching a None node means the target is not present.

Real-World BST Example

The application modeled employee records organized by employee ID. A BST can support efficient lookup because each comparison determines whether the search should continue in the left or right subtree. This can reduce the amount of data that must be examined compared with a linear search.

BST performance still depends on tree shape. A reasonably balanced tree can support searches in approximately O(log n) time, while sequential or nearly sorted insertion can create a skewed tree with O(n) search behavior.

Discussion Board Reflection

The initial discussion post should include the GitHub repository link and a 150–200 word reflection addressing:

Concepts or skills learned while completing the assignment.

Challenges encountered and how they were overcome.

BST behavior and how ordering improves efficiency compared with other data structures.