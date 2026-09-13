# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compared linear search and binary search using a student score lookup scenario. The implementation demonstrated how the organization and size of a dataset affected the efficiency of each search algorithm.

## Learning Objectives

During this assignment, I:

- Implemented linear search
- Implemented binary search
- Compared search performance
- Analyzed algorithm efficiency
- Tested required and additional edge cases
- Applied both search methods to a real-world scenario

## Completed Implementation

### Linear Search

I implemented linear search by checking each value from the beginning of the list until the target was found or the end of the list was reached.

The method returned the index when the target was found and returned `-1` when the target was not present.

Because linear search may need to inspect every item in the list, its worst-case time complexity was `O(n)`.

### Binary Search

I implemented binary search using `low`, `high`, and `mid` indexes.

The algorithm repeatedly checked the middle value of the remaining search range. If the target was greater than the middle value, the lower half was eliminated. If the target was smaller, the upper half was eliminated.

Because each comparison removed approximately half of the remaining search space, binary search had a worst-case time complexity of `O(log n)`.

## Dataset Testing

I tested both search algorithms using a small sorted list of student scores:

`[55, 62, 67, 72, 81, 88, 90, 95]`

I searched for:

- `81`, which was present in the list
- `79`, which was not present

Both algorithms returned index `4` for score `81` and returned `-1` for score `79`.

I also tested both algorithms using a much larger sorted dataset containing 100,000 values. Both methods located the target value correctly, but the test demonstrated the difference in how the algorithms scale as the dataset grows.

## Edge Cases

I tested several edge cases beyond the basic examples.

### Empty List

Both algorithms returned `-1` when searching an empty list because there were no values to examine.

### First Position

Both algorithms correctly returned index `0` when the target was the first value in the list.

### Last Position

Both algorithms correctly returned index `5` when the target was the final value in the boundary test list.

## Performance Analysis

Linear search was simpler because it did not require the data to be sorted. However, its `O(n)` worst-case time complexity meant that it could require checking every item in a large dataset.

Binary search was more efficient for sorted data because it reduced the remaining search space by approximately half after each comparison. This resulted in `O(log n)` worst-case time complexity.

The tradeoff was that binary search depended on the data being sorted. If the dataset was unsorted, binary search could not reliably determine which half of the list to eliminate.

## Real-World Application

I used a student score lookup scenario to demonstrate both algorithms.

Linear search would still be appropriate when working with a small or unsorted collection, especially if the data only needed to be searched once.

Binary search would be more appropriate when repeatedly searching a large, sorted dataset because its performance scaled much better as the number of values increased.

## Discussion Board Reflection

This assignment reinforced the practical difference between linear search and binary search. Linear search was easier to implement because it simply examined each value in order and did not require the dataset to be sorted. Binary search required more logic because I had to maintain the lower and upper search boundaries and calculate a midpoint during each iteration.

The main advantage of binary search became clearer when testing the larger dataset. Linear search has `O(n)` worst-case time complexity and may need to examine every item, while binary search has `O(log n)` worst-case complexity because each comparison eliminates approximately half of the remaining values.

Linear search would still be appropriate for a small or unsorted collection, especially when the data only needed to be searched once. Binary search would not be directly usable on unsorted data because the algorithm depends on the ordering of values to determine which half can safely be eliminated.