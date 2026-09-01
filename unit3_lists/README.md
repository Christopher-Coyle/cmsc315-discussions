# Unit 3 Discussion: List Operations

## Overview

This assignment examined insertion, deletion, and searching in Python lists. I implemented and tested each operation using an aircraft maintenance task list as a real-world scenario. The program demonstrated how Python lists behave when elements are inserted, removed, and searched at different positions.

## Implementation

### Insertion

I implemented `insert_at()` using Python's `list.insert()` method. I tested insertion at the beginning, middle, and end of the list.

When an item was inserted near the beginning or middle, existing elements at and after that position shifted one position to the right. Because many elements may need to move, insertion near the beginning of an array-based list can require O(n) time. Inserting at the end generally requires less shifting.

### Deletion

I implemented `delete_at()` with index validation before calling `pop()`. A valid index removed and returned the requested value. An invalid index returned `None` rather than allowing the program to raise an `IndexError`.

Deleting an element from the beginning or middle caused later elements to shift left to close the gap. Removing the final element did not require those shifts.

### Search

I implemented `search_value()` as a linear search. The function examined list elements sequentially from index 0 until it found the requested value. It returned the matching index when successful and `-1` when the value was absent.

Linear search has O(n) worst-case time because the requested value may be the final element or may not exist, requiring every element to be examined.

## Testing and Edge Cases

I demonstrated insertion and deletion at the beginning, middle, and end of the list. I also searched for both existing and missing values.

Additional edge cases included:

- deleting with an invalid index
- deleting from an empty list
- inserting into an empty list
- searching an empty list for a missing value

These tests verified that invalid or empty-list operations were handled without unexpectedly terminating the program.

## Real-World Scenario

I modeled an aircraft maintenance task list. Maintenance actions can be added as new requirements arise, removed when completed or cancelled, and searched when personnel need to determine whether a specific action remains in the workload.

This type of ordered collection demonstrates why list performance matters. A system with a small number of tasks may show little performance difference, but shifting many array elements during frequent insertions and deletions could become significant as the collection grows.

## Reflection

This assignment helped reinforce the difference between using a list and understanding how its operations affect performance. The Python syntax for insertion and deletion was straightforward, but the more important part was recognizing what happens to the surrounding elements. In an array-based structure, inserting or deleting near the beginning or middle may require many elements to shift, so the location of an operation affects its cost.

The main challenge was handling indexes safely rather than assuming every requested position was valid. I addressed this by checking the index before deletion and returning `None` for invalid operations. I also used `-1` to distinguish an unsuccessful search from a valid index.

In a real application, the best list implementation depends on the workload. Array-based lists provide efficient indexed access, while linked lists can be advantageous when insertions and deletions are frequent and the relevant node is already known. The assignment made that trade-off more concrete by connecting individual operations to both usability and performance.