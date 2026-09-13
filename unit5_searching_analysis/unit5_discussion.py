"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Linear search checks each element one at a time from
    # the beginning of the list.
    # In the worst case, every element must be checked,
    # which gives linear search O(n) time complexity.
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    low = 0
    high = len(lst) - 1

    while low <= high:
        # Find the middle of the remaining search range.
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid

        # If the target is greater than the middle value,
        # eliminate the lower half of the remaining list.
        if lst[mid] < target:
            low = mid + 1

        # Otherwise, eliminate the upper half.
        else:
            high = mid - 1

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    # Real-world scenario: searching a sorted list of student scores.
    small_scores = [55, 62, 67, 72, 81, 88, 90, 95]

    existing_score = 81
    missing_score = 79

    print(f"Student scores: {small_scores}")

    print(
        f"Linear search for {existing_score}: "
        f"{linear_search(small_scores, existing_score)}"
    )

    print(
        f"Binary search for {existing_score}: "
        f"{binary_search(small_scores, existing_score)}"
    )

    print(
        f"Linear search for {missing_score}: "
        f"{linear_search(small_scores, missing_score)}"
    )

    print(
        f"Binary search for {missing_score}: "
        f"{binary_search(small_scores, missing_score)}"
    )

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    # Create a large sorted dataset containing 100,000 values.
    large_scores = list(range(1, 100001))
    large_target = 99999

    print(
        f"Linear search result: "
        f"{linear_search(large_scores, large_target)}"
    )

    print(
        f"Binary search result: "
        f"{binary_search(large_scores, large_target)}"
    )

    # Linear search may examine almost every value.
    # Binary search repeatedly removes half of the remaining
    # search space, which is more efficient as the dataset grows.
    print(
        "Linear search may need to check nearly every value, "
        "while binary search repeatedly cuts the remaining "
        "search space in half."
    )

    print(
        "Linear search has O(n) worst-case time complexity, "
        "while binary search has O(log n) worst-case time complexity."
    )

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Empty list.
    # Neither search can find a value because the collection
    # contains no elements.
    empty_scores = []

    print("Empty list test:")
    print(
        f"Linear search result: "
        f"{linear_search(empty_scores, 81)}"
    )
    print(
        f"Binary search result: "
        f"{binary_search(empty_scores, 81)}"
    )
    print("Both searches return -1 because the list is empty.")

    # Edge case 2: Target at the first position.
    boundary_scores = [55, 67, 72, 81, 90, 95]

    print("\nFirst-position test:")
    print(
        f"Linear search result: "
        f"{linear_search(boundary_scores, 55)}"
    )
    print(
        f"Binary search result: "
        f"{binary_search(boundary_scores, 55)}"
    )

    # Edge case 3: Target at the last position.
    print("\nLast-position test:")
    print(
        f"Linear search result: "
        f"{linear_search(boundary_scores, 95)}"
    )
    print(
        f"Binary search result: "
        f"{binary_search(boundary_scores, 95)}"
    )


if __name__ == "__main__":
    main()