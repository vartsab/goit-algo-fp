import sys
import matplotlib.pyplot as plt
import networkx as nx

class MinHeap:
    def __init__(self):
        self.heap = []
        self.positions = {}

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, key, value):
        if key in self.positions:
            self.decrease_key(key, value)
        else:
            self.heap.append((key, value))
            self.positions[key] = len(self.heap) - 1
            self._sift_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        last_node = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_node
            self.positions[last_node[0]] = 0
            self._sift_down(0)
        del self.positions[root[0]]
        return root

    def decrease_key(self, key, new_value):
        if key in self.positions:
            index = self.positions[key]
            self.heap[index] = (key, new_value)
            self._sift_up(index)

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index][1] < self.heap[parent][1]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                self.positions[self.heap[index][0]] = index
                self.positions[self.heap[parent][0]] = parent
                index = parent
            else:
                break

    def _sift_down(self, index):
        size = len(self.heap)
        while index < size:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2
            if left < size and self.heap[left][1] < self.heap[smallest][1]:
                smallest = left
            if right < size and self.heap[right][1] < self.heap[smallest][1]:
                smallest = right
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                self.positions[self.heap[index][0]] = index
                self.positions[self.heap[smallest][0]] = smallest
                index = smallest
            else:
                break

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        self.edges[u].append((v, weight))
        self.edges[v].append((u, weight))  # Якщо граф неорієнтований

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.edges}
        distances[start] = 0
        min_heap = MinHeap()
        min_heap.insert(start, 0)

        while not min_heap.is_empty():
            current_vertex, current_distance = min_heap.extract_min()

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.edges[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    if neighbor in min_heap.positions:
                        min_heap.decrease_key(neighbor, distance)
                    else:
                        min_heap.insert(neighbor, distance)

        return distances

    def draw(self):
        G = nx.Graph()
        for node in self.edges:
            for neighbor, weight in self.edges[node]:
                G.add_edge(node, neighbor, weight=weight)

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=16, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

# Приклад використання
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

start_vertex = 'A'
distances = graph.dijkstra(start_vertex)

print(f"Shortest distances from {start_vertex}:")
for vertex, distance in distances.items():
    print(f"Distance to {vertex}: {distance}")

# Візуалізація графа
graph.draw()
