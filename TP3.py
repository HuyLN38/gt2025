def show_adj_matrix(tree):
    largest_node = max(tree.keys())
    adjacency_matrix = [[0] * (largest_node + 1) for _ in range(largest_node + 1)]

    for parent_node, children in tree.items():
        for child_node in children:
            adjacency_matrix[parent_node][child_node] = 1

    print("Adjacency Matrix:")
    for row in adjacency_matrix[1:]:
        print(" ".join(map(str, row[1:])))


def custom_inorder_traverse(current_node, tree, visited):
    if current_node is None or visited[current_node]:
        return

    visited[current_node] = True

    child_list = tree.get(current_node, [])

    if child_list:
        custom_inorder_traverse(child_list[0], tree, visited)

    print(current_node, end=" ")

    for child in child_list[1:]:
        custom_inorder_traverse(child, tree, visited)


if __name__ == "__main__":
    sample_graph = {
        1: [2, 3],
        2: [5, 6],
        3: [4],
        4: [8],
        5: [7],
        6: [],
        7: [],
        8: []
    }

    show_adj_matrix(sample_graph)

    try:
        starting = int(input("\nEnter the node from which to start traversal: "))
        visited_nodes = [False] * (max(sample_graph.keys()) + 1)

        print("In-order-style Traversal:")
        custom_inorder_traverse(starting, sample_graph, visited_nodes)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
