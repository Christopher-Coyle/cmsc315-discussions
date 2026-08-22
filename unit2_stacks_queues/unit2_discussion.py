"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # append() adds the newest value to the top of the stack, supporting LIFO behavior.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return None

        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            return None

        # peek() returns the top value without removing it from the stack.
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # append() adds the newest value to the back of the queue, supporting FIFO behavior.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # What should happen if the queue is empty?
        if self.is_empty():
            return None

        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            return None

        # front() returns the oldest value without removing it from the queue.
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.
    print("\n=== ADDITIONAL TEST CASE ===")

    test_queue = Queue()
    test_queue.enqueue("A")
    test_queue.enqueue("B")
    print("Starting queue:", test_queue.items)
    print("Dequeued:", test_queue.dequeue())

    test_queue.enqueue("C")
    print("Queue after adding C:", test_queue.items)
    print("Next item should still be B:", test_queue.front())

    print("\n=== STACK DEMO ===")

    stack = Stack()

    print("Adding four values to the stack: 10, 20, 30, 40")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    print("Current stack:", stack.items)
    print("Top value using peek():", stack.peek())

    print("Removing values demonstrates LIFO behavior:")
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())

    print("Stack empty:", stack.is_empty())
    print("Attempting pop() on an empty stack:", stack.pop())
    print("Attempting peek() on an empty stack:", stack.peek())

    single_stack = Stack()
    single_stack.push(99)
    print("Single-item stack before removal:", single_stack.items)
    print("Removed:", single_stack.pop())
    print("Single-item stack empty after removal:", single_stack.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.


    print("\n=== QUEUE DEMO ===")

    queue = Queue()

    print("Adding four values to the queue: 10, 20, 30, 40")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)

    print("Current queue:", queue.items)
    print("Front value using front():", queue.front())

    print("Removing values demonstrates FIFO behavior:")
    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())

    print("Queue empty:", queue.is_empty())
    print("Attempting dequeue() on an empty queue:", queue.dequeue())
    print("Attempting front() on an empty queue:", queue.front())

    single_queue = Queue()
    single_queue.enqueue(99)
    print("Single-item queue before removal:", single_queue.items)
    print("Removed:", single_queue.dequeue())
    print("Single-item queue empty after removal:", single_queue.is_empty())
    print("\n=== REAL-WORLD IT SUPPORT DESK SCENARIO ===")

    support_queue = Queue()
    action_stack = Stack()

    print("Three support tickets arrive:")
    support_queue.enqueue("Ticket 101 - Password reset")
    support_queue.enqueue("Ticket 102 - Printer issue")
    support_queue.enqueue("Ticket 103 - Network connection")

    print("Tickets waiting:", support_queue.items)
    print("Next ticket handled:", support_queue.dequeue())
    print("Next ticket handled:", support_queue.dequeue())
    print("\nTechnician actions are recorded for possible undo:")
    action_stack.push("Reset user password")
    action_stack.push("Restart printer service")
    action_stack.push("Update network settings")

    print("Recorded actions:", action_stack.items)
    print("Most recent action undone:", action_stack.pop())
    print("Next action that would be undone:", action_stack.peek())
if __name__ == "__main__":
    main()
