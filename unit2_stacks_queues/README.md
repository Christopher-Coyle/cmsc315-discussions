# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explored two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

The program implemented both structures in Python and demonstrated their primary operations, edge cases, and practical uses.

## Learning Objectives

During this assignment, I:

- Implemented stack operations
- Implemented queue operations
- Demonstrated LIFO and FIFO behavior
- Tested required and additional edge cases
- Applied stacks and queues to a real-world scenario

## Completed Implementation

### Stack

I implemented the Stack class using a Python list.

The stack supported the following operations:

- `push()` added a value to the top of the stack.
- `pop()` removed and returned the most recently added value.
- `peek()` returned the top value without removing it.
- `is_empty()` determined whether the stack contained any values.

The program demonstrated Last In, First Out (LIFO) behavior by pushing the values `10`, `20`, `30`, and `40`. The values were then removed in the order `40`, `30`, `20`, and `10`.

### Queue

I implemented the Queue class using `collections.deque`.

The queue supported the following operations:

- `enqueue()` added a value to the back of the queue.
- `dequeue()` removed and returned the value at the front of the queue.
- `front()` returned the front value without removing it.
- `is_empty()` determined whether the queue contained any values.

The program demonstrated First In, First Out (FIFO) behavior by enqueueing the values `10`, `20`, `30`, and `40`. The values were then removed in the same order: `10`, `20`, `30`, and `40`.

## Edge Cases and Testing

I tested several edge cases to verify that the stack and queue behaved correctly under boundary conditions.

For the stack:

- Calling `pop()` on an empty stack returned `None`.
- Calling `peek()` on an empty stack returned `None`.
- A stack containing one item became empty after that item was removed.

For the queue:

- Calling `dequeue()` on an empty queue returned `None`.
- Calling `front()` on an empty queue returned `None`.
- A queue containing one item became empty after that item was removed.

I also added an additional queue test beyond the starter examples. The queue initially contained `A` and `B`. After `A` was dequeued, `C` was enqueued. The resulting queue contained `B` and `C`, and `B` remained at the front. This demonstrated that FIFO ordering was preserved when enqueue and dequeue operations were mixed.

## Real-World Scenario

I created an IT support desk scenario to demonstrate how stacks and queues can be used together.

The queue represented incoming support tickets. Tickets were processed in the same order in which they arrived, making FIFO behavior appropriate for handling customers fairly.

The stack represented technician actions that could potentially be undone. The most recently completed action was removed first, which demonstrated LIFO behavior.

For example, support tickets were added in the following order:

1. Password reset
2. Printer issue
3. Network connection

The password reset ticket was handled first because it entered the queue first.

Technician actions were stored in this order:

1. Reset user password
2. Restart printer service
3. Update network settings

When an action was undone, `Update network settings` was removed first because it was the most recently added action.

## Memory and Performance Considerations

Both the stack and queue grow as additional elements are added, so their memory use increases approximately in proportion to the number of stored elements.

The stack used a Python list. Adding and removing values from the end of the list supports efficient stack operations.

The queue used `collections.deque`, which supports efficient additions to the back and removals from the front. This makes it more appropriate for queue behavior than repeatedly removing the first item from a standard Python list.

## Discussion Board Reflection

The completed assignment demonstrated the differences between stacks and queues through both direct testing and a practical IT support scenario.

A stack uses Last In, First Out (LIFO) behavior, meaning the most recently added value is the first one removed. This is useful for operations such as undo histories where the most recent action should be reversed first.

A queue uses First In, First Out (FIFO) behavior, meaning the earliest value added is the first one removed. This is useful for situations such as support tickets where requests should normally be processed in the order received.

The assignment also reinforced the importance of testing edge cases. Empty stack and queue operations were handled by returning `None`, which prevented errors when attempting to remove or inspect values that were not present.