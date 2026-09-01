"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    # Python's insert() places the value at the requested position.
    # Elements at that index and after it shift one position to the right.
    # Inserting near the beginning can require shifting many elements,
    # giving the operation O(n) time in the worst case.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # Validate the index before attempting deletion. This prevents an
    # IndexError and allows the function to fail safely with None.
    if index < 0 or index >= len(lst):
        return None

    # pop(index) removes and returns the selected value. Elements after
    # the deleted position shift left to close the gap.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # This is a linear search because each element is examined
    # sequentially from the beginning until a match is found.
    # In the worst case, every element must be checked, giving O(n) time.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # -1 clearly indicates that the requested value was not found.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # This list models prioritized aircraft maintenance tasks.
    maintenance_tasks = [
        "Inspect landing gear",
        "Check hydraulic system",
        "Review maintenance log"
    ]

    print("Original maintenance tasks:")
    print(maintenance_tasks)

    # Beginning insertion shifts every existing item right.
    insert_at(maintenance_tasks, 0, "Safety inspection")
    print("\nAfter inserting a priority task at the beginning:")
    print(maintenance_tasks)

    # Middle insertion shifts only the elements at and after the index.
    middle_index = len(maintenance_tasks) // 2
    insert_at(maintenance_tasks, middle_index, "Inspect flight controls")
    print("\nAfter inserting a task in the middle:")
    print(maintenance_tasks)

    # End insertion requires no existing elements to shift.
    insert_at(maintenance_tasks, len(maintenance_tasks),
              "Close maintenance action")
    print("\nAfter inserting a task at the end:")
    print(maintenance_tasks)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Deleting from the beginning causes all remaining elements to shift left.
    removed = delete_at(maintenance_tasks, 0)
    print(f"Removed from beginning: {removed}")
    print(f"Updated list: {maintenance_tasks}")

    # Delete a valid element from the middle of the current list.
    middle_index = len(maintenance_tasks) // 2
    removed = delete_at(maintenance_tasks, middle_index)
    print(f"\nRemoved from middle: {removed}")
    print(f"Updated list: {maintenance_tasks}")

    # Removing the final element does not require later elements to shift.
    removed = delete_at(maintenance_tasks, len(maintenance_tasks) - 1)
    print(f"\nRemoved from end: {removed}")
    print(f"Updated list: {maintenance_tasks}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Search for an existing task.
    target = "Inspect landing gear"
    result = search_value(maintenance_tasks, target)

    if result != -1:
        print(f"'{target}' was found at index {result}.")
    else:
        print(f"'{target}' was not found.")

    # Search for a missing value to demonstrate the -1 result.
    missing_target = "Replace engine"
    result = search_value(maintenance_tasks, missing_target)

    if result != -1:
        print(f"'{missing_target}' was found at index {result}.")
    else:
        print(f"'{missing_target}' was not found. Search returned -1.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Invalid index. Safe validation returns None instead
    # of allowing an IndexError to terminate the program.
    invalid_result = delete_at(maintenance_tasks, 100)
    print(f"Delete using invalid index 100 returned: {invalid_result}")

    # Edge case 2: Deleting from an empty list safely returns None.
    empty_list = []
    empty_delete_result = delete_at(empty_list, 0)
    print(f"Delete from empty list returned: {empty_delete_result}")

    # Edge case 3: A Python list can accept its first element normally.
    insert_at(empty_list, 0, "First maintenance task")
    print(f"Insert into empty list produced: {empty_list}")

    # Additional search edge case on an empty collection.
    empty_search_result = search_value([], "Missing task")
    print(f"Search of empty list returned: {empty_search_result}")


if __name__ == "__main__":
    main()