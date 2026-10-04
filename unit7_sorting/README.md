# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compared Bubble Sort and Merge Sort using Python. I implemented both algorithms, tested them with multiple datasets, evaluated several edge cases, and compared their efficiency and practical use.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency
- Test sorting algorithms with different input conditions
- Evaluate edge cases and algorithm behavior

## Implementation

I implemented Bubble Sort by comparing adjacent values and swapping them whenever they were out of order. I also added an early-exit condition so the algorithm stopped when a complete pass occurred without any swaps.

I implemented Merge Sort recursively. The algorithm divided each list into smaller halves until the base case of zero or one element was reached. The sorted halves were then combined using a separate merge function that compared the next available value from each half.

Both algorithms returned new sorted lists instead of modifying the original input lists.

## Testing

I tested both algorithms using two unsorted datasets and verified that they produced identical ascending results.

I also tested several edge cases:

- Empty list
- Already sorted list
- List containing duplicate values
- Reverse-sorted list

Both algorithms handled all tested cases successfully.

## Performance Analysis

Bubble Sort has a typical and worst-case time complexity of O(n²). My implementation included an early-exit optimization, allowing an already sorted list to finish much faster when no swaps were required.

Merge Sort has O(n log n) time complexity and scales substantially better as the size of the dataset increases. Its tradeoff is that it uses additional memory while dividing and merging lists.

For small datasets, Bubble Sort can be useful because its logic is simple to understand and implement. For large datasets, Merge Sort is generally the better choice because its performance remains O(n log n).

## Real-World Application

A streaming platform could use sorting algorithms to organize movies and television programs by rating, popularity, release date, or another recommendation metric. Merge Sort would be more appropriate for large recommendation datasets because its O(n log n) performance scales better than Bubble Sort's O(n²) behavior.

## Discussion Board Reflection

While completing this assignment, I gained a better understanding of how two sorting algorithms can produce the same result while using very different approaches. Bubble Sort was straightforward because it repeatedly compared adjacent values and swapped them when they were out of order. I also implemented an early-exit condition, which showed why the condition of the input data can affect performance. Merge Sort required more thought because it used recursion, divided the original list into smaller parts, and then rebuilt the final result through the merge operation.

The main challenge was following the recursive flow of Merge Sort and understanding when each call reached its base case. Breaking the algorithm into separate `merge_sort()` and `merge()` functions made the process easier to trace.

The biggest difference between the algorithms was scalability. Bubble Sort has O(n²) performance in typical and worst cases, while Merge Sort maintains O(n log n) performance. Bubble Sort is easier to implement and can work adequately with very small datasets, but Merge Sort is a much stronger choice when processing large collections where performance matters.