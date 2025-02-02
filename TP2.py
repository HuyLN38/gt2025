from collections import defaultdict, deque

from Tools.demo.beer import n


def create_adjacency_matrix(edge_list, total_nodes):
    matrix = [[0] * total_nodes for _ in range(total_nodes)]
    for origin, target in edge_list:
        matrix[origin - 1][target - 1] = 1
    return matrix


def display_matrix(matrix):
    print("Adjacency Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))


def matrix_to_adjacency_list(matrix):
    adjacency_list = defaultdict(list)
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == 1:
                adjacency_list[i + 1].append(j + 1)
    return adjacency_list


def count_weak_components(matrix):
    directed_list = matrix_to_adjacency_list(matrix)

    undirected_list = defaultdict(list)
    for node, neighbors in directed_list.items():
        for n in neighbors:
            undirected_list[node].append(n)
            undirected_list[n].append(node)

    visited = set()
    weak_components = 0

    def bfs(start):
        queue = deque([start])
        while queue:
            current = queue.popleft()
            for neighbor in undirected_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    for node in range(1, len(matrix) + 1):
        if node not in visited:
            visited.add(node)
            bfs(node)
            weak_components += 1

    return weak_components


def count_strong_components(matrix):
    adjacency_list = matrix_to_adjacency_list(matrix)
    visited = set()
    stack_order = []
    def forward_dfs(node):
        visited.add(node)
        for n in adjacency_list[node]:
            if n not in visited:
                forward_dfs(n)
        stack_order.append(node)

    for node in range(1, len(matrix) + 1):
        if node not in visited:
            forward_dfs(n)
            stack_order.append(node)

        for node in range(1, len(matrix) + 1):
            if node not in visited:
                forward_dfs(node)

        reversed_list = defaultdict(list)
        for origin, neighbors in adjacency_list.items():
            for tgt in neighbors:
                reversed_list[tgt].append(origin)

        visited.clear()
        strong_components = 0

        def reverse_dfs(node):
            stack = [node]
            while stack:
                top = stack.pop()
                if top not in visited:
                    visited.add(top)
                    stack.extend(reversed_list[top])

        while stack_order:
            current = stack_order.pop()
            if current not in visited:
                reverse_dfs(current)
                strong_components += 1

        return strong_components

if __name__ == "__main__":

    sample_edges = [
        (1, 2), (1, 4), (2, 3), (2, 6),
        (6, 3), (6, 4), (5, 4), (7, 6),
        (7, 3), (7, 5), (7, 8), (8, 9), (5, 9)
    ]
    number_of_nodes = 9

    adj_matrix = create_adjacency_matrix(sample_edges, number_of_nodes)
    display_matrix(adj_matrix)

    weak_count = count_weak_components(adj_matrix)
    strong_count = count_strong_components(adj_matrix)

    print(f"\nNumber of weakly connected components: {weak_count}")
    print(f"Number of strongly connected components: {strong_count}")