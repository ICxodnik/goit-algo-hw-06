import networkx as nx
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from graph_search_algo.bfs import bfs_iterative
from graph_search_algo.dfs import dfs_iterative
from dijkstra_algo.dijkstra import dijkstra

# Створення графа (метро Києва)
graph = {
    'Головна': {'Кловська': 2, 'Палац Спорту': 3},
    'Кловська': {'Головна': 2, 'Палац Спорту': 2, 'Арсенальна': 4},
    'Палац Спорту': {'Головна': 3, 'Кловська': 2, 'Печерська': 4},
    'Печерська': {'Палац Спорту': 4, 'Арсенальна': 3, 'Либідська': 5},
    'Арсенальна': {'Кловська': 4, 'Печерська': 3},
    'Либідська': {'Печерська': 5, 'Дружби Народів': 6},
    'Дружби Народів': {'Либідська': 6, 'Голосіївська': 4},
    'Голосіївська': {'Дружби Народів': 4, 'Виставковий центр': 3},
    'Виставковий центр': {'Голосіївська': 3}
}

# Створення графа в networkx
G = nx.Graph()

# Додаємо вершини і ребра
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

# Аналіз
print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
degrees = dict(G.degree())
print("Ступінь кожної вершини:")
for node, degree in degrees.items():
    print(f"{node}: {degree}")

# Обхід DFS
dfs_tree = nx.dfs_tree(G, source='Головна')
print("DFS-дерево:")
print(list(dfs_tree.edges()))  # виведе ребра DFS-дерева з коренем у вузлі Головна
dfs_iterative(G, 'Головна')

# Обхід BFS
bfs_tree = nx.bfs_tree(G, source='Головна')
print("\nBFS-дерево:")
print(list(bfs_tree.edges()))  # виведе ребра BFS-дерева з коренем у вузлі Головна
bfs_iterative(G, 'Головна')

# Найкоротші шляхи між всіма парами вершин
dijkstra(graph, 'Головна')
all_paths = dict(nx.all_pairs_dijkstra_path(G))
all_lengths = dict(nx.all_pairs_dijkstra_path_length(G))
for source in all_paths:
    print(f"\nНайкоротші шляхи з {source}:")
    for target in all_paths[source]:
        path = all_paths[source][target]
        length = all_lengths[source][target]
        print(f"  до {target} {length} хв: шлях {path}")

# Візуалізація графа
pos = nx.spring_layout(G, seed=42)
labels = nx.get_edge_attributes(G, 'weight') 

# Малювання графа
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')

# Малювання ваг на ребрах з налаштуванням шрифтів
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12, font_color='black')

plt.title("Транспортна мережа метрополітену Києва")
plt.show()






