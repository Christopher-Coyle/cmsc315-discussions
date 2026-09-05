"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # The recursive helper returns the updated subtree root.
        # Smaller values move left and larger values move right,
        # preserving the BST ordering property at each step.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # A null reference marks the correct open position for a new node.
        if node is None:
            return Node(value)

        # Values smaller than the current node belong in the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Values larger than the current node belong in the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate values are ignored so each value appears only once.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # A BST can eliminate an entire subtree after each comparison.
        # A linear search may need to inspect every item one at a time.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Reaching None means the value is not in this search path.
        if node is None:
            return False

        if value == node.value:
            return True

        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return

        # In a BST, every left-subtree value is smaller than the node,
        # and every right-subtree value is larger. Visiting left,
        # node, then right therefore produces ascending sorted output.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    # This example models employee ID numbers stored in a BST.
    # Starting with a middle value creates useful branches on both sides.
    employee_ids = [1050, 1025, 1075, 1010, 1040, 1060, 1090]
    tree = BST()

    for employee_id in employee_ids:
        # Each comparison selects only the left or right subtree.
        # This reduces the remaining search space instead of scanning
        # every previously inserted value.
        tree.insert(employee_id)

    print("Inserted employee IDs:", employee_ids)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    # In-order traversal visits left subtree, node, then right subtree.
    # Because the BST keeps smaller values left and larger values right,
    # the resulting list is sorted from smallest to largest.
    print("Sorted employee IDs:", tree.inorder())

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # Existing values should return True because the recursive search
    # eventually reaches their nodes.
    print("Search 1025:", tree.search(1025))
    print("Search 1090:", tree.search(1090))

    # Missing values return False once the search reaches an empty
    # child reference on the only path where each value could exist.
    print("Search 1000:", tree.search(1000))
    print("Search 1080:", tree.search(1080))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # An empty BST has no root node. Traversal returns an empty list,
    # and search returns False because recursion immediately reaches None.
    empty_tree = BST()
    print("Empty-tree traversal:", empty_tree.inorder())
    print("Search empty tree for 1050:", empty_tree.search(1050))


if __name__ == "__main__":
    main()
c