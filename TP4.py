import heapq


def build_weighted_matrix():

    size = 9
    w_matrix = [[0] * size for _ in range(size)]

    edge_list = [
        (1, 2, 4), (1, 5, 1), (1, 7, 2),
        (2, 3, 7), (2, 6, 5),
        (3, 4, 1), (3, 6, 8),
        (4, 6, 6), (4, 7, 4), (4, 8, 3),
        (5, 6, 9), (5, 7, 10),
        (6, 9, 2),
        (7, 9, 8),
        (8, 9, 1),
        (9, 8, 7)
    ]

    for src, dst, wt in edge_list:
        w_matrix[src - 1][dst - 1] = wt
        w_matrix[dst - 1][src - 1] = wt

    return w_matrix


def show_weighted_matrix(w_matrix):

    print("Weighted Adjacency Matrix:")
    for row in w_matrix:
        print(" ".join(f"{val:2}" for val in row))


def prim_mst(w_matrix, start_index):

    n = len(w_matrix)
    visited = [False] * n

    priority_queue = [(0, start_index, -1)]
    mst_edges = []
    mst_weight = 0

    while priority_queue:
        wt, node, parent = heapq.heappop(priority_queue)

        if visited[node]:
            continue

        visited[node] = True
        mst_weight += wt

        if parent != -1:
            mst_edges.append((parent + 1, node + 1, wt))

        for neighbor in range(n):
            if not visited[neighbor] and w_matrix[node][neighbor] > 0:
                heapq.heappush(priority_queue, (w_matrix[node][neighbor], neighbor, node))

    return mst_edges, mst_weight


def kruskal_mst(w_matrix):
    n = len(w_matrix)

    edge_array = []
    for i in range(n):
        for j in range(i + 1, n):
            if w_matrix[i][j] > 0:
                edge_array.append((w_matrix[i][j], i, j))

    edge_array.sort(key=lambda x: x[0])

    parent = list(range(n))
    rank = [0] * n

    def find_set(node):
        if parent[node] != node:
            parent[node] = find_set(parent[node])
        return parent[node]

    def union_sets(a, b):
        rootA = find_set(a)
        rootB = find_set(b)
        if rootA != rootB:
            if rank[rootA] > rank[rootB]:
                parent[rootB] = rootA
            elif rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
            else:
                parent[rootB] = rootA
                rank[rootA] += 1

    mst_edges = []
    mst_weight = 0

    for weight, u, v in edge_array:
        if find_set(u) != find_set(v):
            union_sets(u, v)
            mst_edges.append((u + 1, v + 1, weight))
            mst_weight += weight

    return mst_edges, mst_weight


if __name__ == "__main__":
    matrix_graph = build_weighted_matrix()
    show_weighted_matrix(matrix_graph)

    try:
        start_node_index = int(input("\nEnter the root node (1-9): ")) - 1

        print("\nPrim's Algorithm Results:")
        prim_result, prim_total = prim_mst(matrix_graph, start_node_index)
        print("MST Edges:", prim_result)
        print("Total MST Weight:", prim_total)

        print("\nKruskal's Algorithm Results:")
        kruskal_result, kruskal_total = kruskal_mst(matrix_graph)
        print("MST Edges:", kruskal_result)
        print("Total MST Weight:", kruskal_total)

    except ValueError:
        print("Invalid input! Please enter an integer between 1 and 9.")
