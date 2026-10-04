"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # Return an empty traversal if the start node does not exist.
    # This prevents an invalid key lookup and safely handles
    # missing-node and empty-graph edge cases.
    if start not in graph:
        return []

    # A queue provides FIFO (First-In, First-Out) behavior.
    # This allows BFS to visit all nearby nodes before moving
    # farther away from the starting node.
    queue = deque([start])

    # The visited set prevents nodes from being processed more
    # than once, which is especially important when a graph
    # contains cycles.
    visited = {start}

    # This list stores nodes in the order BFS visits them.
    traversal_order = []

    while queue:
        # Remove the oldest node from the front of the queue.
        current = queue.popleft()
        traversal_order.append(current)

        # Add unvisited neighbors to the queue so they can be
        # explored during later BFS iterations.
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # Unlike DFS, which follows one path deeply before backtracking,
    # BFS explores nodes level by level from the starting node.
    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    # This graph models a simple streaming recommendation network.
    # Each node represents a piece of content.
    # Each edge represents a similarity relationship, such as shared
    # genre, cast, viewing patterns, or audience preferences.
    graph = {
        "Space Quest": ["Cyber City", "Galaxy Wars"],
        "Cyber City": ["Space Quest", "Mystery Code"],
        "Galaxy Wars": ["Space Quest", "Alien Frontier"],
        "Mystery Code": ["Cyber City", "Hidden Truth"],
        "Alien Frontier": ["Galaxy Wars", "Hidden Truth"],
        "Hidden Truth": ["Mystery Code", "Alien Frontier"]
    }

    print("\n=== GRAPH STRUCTURE ===")
    # TODO: Create and display a graph.
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    # TODO: Perform and explain BFS traversal.

    start_node = "Space Quest"

    # BFS begins at Space Quest and explores all directly connected
    # content before moving to content farther away in the graph.
    original_traversal = bfs(graph, start_node)

    print(f"Starting node: {start_node}")
    print("Original BFS traversal:")
    print(" -> ".join(original_traversal))

    # Add a new content item to the recommendation network.
    graph["Deep Cosmos"] = ["Alien Frontier"]

    # Because the graph represents two-way similarity relationships,
    # Alien Frontier also receives Deep Cosmos as a neighbor.
    graph["Alien Frontier"].append("Deep Cosmos")

    print("\nAdded new node: Deep Cosmos")
    print("Connected Deep Cosmos to Alien Frontier.")

    updated_traversal = bfs(graph, start_node)

    print("Updated BFS traversal:")
    print(" -> ".join(updated_traversal))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # TODO: Demonstrate and explain edge cases.

    # Edge Case 1: Missing start node
    # The BFS function safely returns an empty list because the
    # requested starting node does not exist in the graph.
    missing_start = "Unknown Movie"
    missing_result = bfs(graph, missing_start)

    print("\nEdge Case 1: Missing start node")
    print(f"Starting node: {missing_start}")
    print(f"Traversal result: {missing_result}")
    print("Explanation: BFS returned an empty list because the start node "
          "was not found in the graph.")

    # Edge Case 2: Single-node graph
    # A graph containing only one node should return that node because
    # there are no additional neighbors to visit.
    single_node_graph = {
        "Standalone Documentary": []
    }

    single_result = bfs(single_node_graph, "Standalone Documentary")

    print("\nEdge Case 2: Single-node graph")
    print(f"Traversal result: {single_result}")
    print("Explanation: BFS visited the only node and then stopped because "
          "the node had no neighbors.")

    # Edge Case 3: Disconnected graph
    # Starting from one connected component does not allow BFS to reach
    # nodes in another disconnected component.
    disconnected_graph = {
        "Movie A": ["Movie B"],
        "Movie B": ["Movie A"],
        "Movie C": ["Movie D"],
        "Movie D": ["Movie C"]
    }

    disconnected_result = bfs(disconnected_graph, "Movie A")

    print("\nEdge Case 3: Disconnected graph")
    print(f"Traversal result: {disconnected_result}")
    print("Explanation: BFS visited Movie A and Movie B, but it could not "
          "reach Movie C or Movie D because no edge connects the two groups.")


if __name__ == "__main__":
    main()