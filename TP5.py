import heapq

def build_adjacency_matrix():
    size = 13
    graph_matrix = [[0] * size for _ in range(size)]

    graph_edges = [
        ('A', 'B', 4), ('A', 'C', 1),
        ('B', 'F', 3),
        ('C', 'F', 7), ('C', 'D', 8),
        ('D', 'H', 5),
        ('F', 'H', 1), ('F', 'E', 1),
        ('E', 'H', 2), ('E', 'L', 2),
        ('H', 'G', 3), ('H', 'M', 7), ('H', 'L', 6),
        ('G', 'L', 4), ('G', 'M', 4),
        ('L', 'M', 4)
    ]

    def char_to_index(ch):
        return ord(ch) - ord('A')

    for src, dst, weight in graph_edges:
        i = char_to_index(src)
        j = char_to_index(dst)
        graph_matrix[i][j] = weight
        graph_matrix[j][i] = weight

    return graph_matrix

def show_matrix(graph_matrix):
    print("Weighted Adjacency Matrix:")
    for row in graph_matrix:
        print(" ".join(f"{value:2}" for value in row))

def dijkstra_shortest_path(graph_matrix, source, target):

    size = len(graph_matrix)
    dist = [float('inf')] * size
    dist[source] = 0
    predecessor = [-1] * size
    visited = [False] * size
    priority_queue = [(0, source)]

    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)

        if visited[current_node]:
            continue
        visited[current_node] = True

        for neighbor in range(size):
            if graph_matrix[current_node][neighbor] > 0:  # edge exists
                alt_dist = current_dist + graph_matrix[current_node][neighbor]
                if alt_dist < dist[neighbor]:
                    dist[neighbor] = alt_dist
                    predecessor[neighbor] = current_node
                    heapq.heappush(priority_queue, (alt_dist, neighbor))

    path_nodes = []
    trace = target
    while trace != -1:
        path_nodes.append(trace)
        trace = predecessor[trace]
    path_nodes.reverse()

    return path_nodes, dist[target]

def char_to_index(ch):
    return ord(ch) - ord('A')

def index_to_char(idx):
    return chr(idx + ord('A'))

if __name__ == "__main__":
    adj_matrix = build_adjacency_matrix()
    show_matrix(adj_matrix)

    try:
        start_char = input("\nEnter the source node (A-M): ").upper()
        end_char = input("Enter the target node (A-M): ").upper()

        start_idx = char_to_index(start_char)
        end_idx = char_to_index(end_char)

        if 0 <= start_idx < len(adj_matrix) and 0 <= end_idx < len(adj_matrix):
            shortest_path, distance_sum = dijkstra_shortest_path(adj_matrix, start_idx, end_idx)
            path_labels = [index_to_char(node) for node in shortest_path]

            print("\nDijkstra's Algorithm Output:")
            print(f"Shortest path from {start_char} to {end_char}: {' -> '.join(path_labels)}")
            print(f"Total path cost: {distance_sum}")
        else:
            print("Invalid node input! Node labels must range from A to M.")
    except Exception as error:
        print(f"An error occurred: {error}")
