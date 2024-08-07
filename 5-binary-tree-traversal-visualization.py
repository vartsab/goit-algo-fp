import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex, Normalize

class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

# Функція для побудови бінарного дерева з масиву
def build_heap_tree(array):
    n = len(array)
    nodes = [Node(array[i]) for i in range(n)]
    
    for i in range(n):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < n:
            nodes[i].left = nodes[left_index]
        if right_index < n:
            nodes[i].right = nodes[right_index]
            
    return nodes[0] if nodes else None

# Функція для додавання ребер до графа на основі дерева
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

# Функція для генерації кольорів від темного до світлого синього
def generate_colors(n):
    colors = []
    norm = Normalize(vmin=0, vmax=n-1)
    for i in range(n):
        shade = norm(i)
        color = (shade, shade, 1.0)  # RGB в діапазоні [0, 1] для синього
        colors.append(to_hex(color))
    return colors

# Обхід дерева в ширину (BFS) з призначенням кольорів
def bfs_traversal(root):
    if not root:
        return []

    queue = [root]
    order = []
    while queue:
        node = queue.pop(0)
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return order

# Обхід дерева в глибину (DFS) з призначенням кольорів
def dfs_traversal(root):
    if not root:
        return []

    stack = [root]
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return order

# Функція для візуалізації дерева з кольоровими вузлами
def draw_tree(tree_root, traversal_order, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    # Призначення кольорів на основі порядку обходу
    colors = generate_colors(len(traversal_order))
    for i, node in enumerate(traversal_order):
        node.color = colors[i]
        tree.nodes[node.id]['color'] = node.color

    node_colors = [tree.nodes[node]['color'] for node in tree.nodes()]
    labels = {node: tree.nodes[node]['label'] for node in tree.nodes()}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.title(title)
    plt.show()

# Приклад масиву купи
heap_array = [0, 1, 4, 5, 10, 3]

# Побудова дерева
heap_tree_root = build_heap_tree(heap_array)

# Виконання обходів
bfs_order = bfs_traversal(heap_tree_root)
dfs_order = dfs_traversal(heap_tree_root)

# Візуалізація обходу в ширину
draw_tree(heap_tree_root, bfs_order, "Breadth-First Search Traversal")

# Візуалізація обходу в глибину
draw_tree(heap_tree_root, dfs_order, "Depth-First Search Traversal")
