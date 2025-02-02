from collections import defaultdict, deque


class DirectedGraph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def insert_edge(self, from_node, to_node):
        self.adjacency_list[from_node].append(to_node)

    def path_exists(self, start_node, end_node):
        visited = set()
        queue = deque([start_node])

        while queue:
            current = queue.popleft()

            if current == end_node:
                return True

            visited.add(current)

            for neighbor in self.adjacency_list[current]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

        return False


graph = DirectedGraph()

connections = [
    (1, 2), (2, 5), (3, 6), (4, 6), (6, 7), (4, 7)
]

for src, dest in connections:
    graph.insert_edge(src, dest)

start_node = int(input("Enter starting node: "))
end_node = int(input("Enter target node: "))

if graph.path_exists(start_node, end_node):
    print("Path found!")
else:
    print("No path found.")
