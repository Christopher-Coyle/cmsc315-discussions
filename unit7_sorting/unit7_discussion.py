"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """

    # Create a copy so the original list is not modified.
    sorted_list = lst.copy()

    # Each pass moves the largest remaining value toward the end.
    for i in range(len(sorted_list) - 1):
        swapped = False

        # Compare neighboring elements in the unsorted portion.
        for j in range(len(sorted_list) - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                # Swap adjacent values when they are out of order.
                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j],
                )
                swapped = True

        # If an entire pass completes without a swap,
        # the list is already sorted and processing can stop early.
        if not swapped:
            break

    return sorted_list


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """

    # A list containing zero or one element is already sorted.
    if len(lst) <= 1:
        return lst.copy()

    # Divide the list into two approximately equal halves.
    midpoint = len(lst) // 2
    left_half = lst[:midpoint]
    right_half = lst[midpoint:]

    # Recursively sort each half.
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge the two sorted halves into one sorted list.
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """

    merged = []
    left_index = 0
    right_index = 0

    # Compare the next available value from each sorted half.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # One side may still contain values after the other side is exhausted.
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")

    dataset1 = [42, 19, 88, 7, 31, 64, 12, 53]

    print("Original list:   ", dataset1)
    print("Bubble Sort:     ", bubble_sort(dataset1))
    print("Merge Sort:      ", merge_sort(dataset1))

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")

    dataset2 = [105, 3, 67, 44, 89, 21, 76, 10]

    bubble_result = bubble_sort(dataset2)
    merge_result = merge_sort(dataset2)

    print("Original list:   ", dataset2)
    print("Bubble Sort:     ", bubble_result)
    print("Merge Sort:      ", merge_result)
    print("Results match:   ", bubble_result == merge_result)

    # Both algorithms produce the same sorted output, but they use
    # different strategies. Bubble Sort repeatedly compares neighboring
    # values, while Merge Sort recursively divides and merges the data.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    empty_list = []
    already_sorted = [1, 2, 3, 4, 5]
    duplicate_values = [8, 3, 8, 1, 3, 8]
    reverse_sorted = [9, 7, 5, 3, 1]

    print("\nEmpty list:")
    print("Bubble Sort:     ", bubble_sort(empty_list))
    print("Merge Sort:      ", merge_sort(empty_list))
    print("Explanation: Both algorithms safely return an empty list.")

    print("\nAlready sorted list:")
    print("Original:        ", already_sorted)
    print("Bubble Sort:     ", bubble_sort(already_sorted))
    print("Merge Sort:      ", merge_sort(already_sorted))
    print(
        "Explanation: Bubble Sort stops early because no swaps are needed."
    )

    print("\nDuplicate values:")
    print("Original:        ", duplicate_values)
    print("Bubble Sort:     ", bubble_sort(duplicate_values))
    print("Merge Sort:      ", merge_sort(duplicate_values))
    print(
        "Explanation: Duplicate values are retained while the list is sorted."
    )

    print("\nReverse-sorted list:")
    print("Original:        ", reverse_sorted)
    print("Bubble Sort:     ", bubble_sort(reverse_sorted))
    print("Merge Sort:      ", merge_sort(reverse_sorted))
    print(
        "Explanation: Both algorithms sort the list correctly, but "
        "Bubble Sort requires many adjacent swaps."
    )

    # Real-world example:
    # A streaming platform could sort movie or television recommendations
    # by rating, popularity, or release date. Merge Sort is generally better
    # suited to large datasets because its O(n log n) performance scales
    # more efficiently than Bubble Sort's O(n^2) behavior.


if __name__ == "__main__":
    main()