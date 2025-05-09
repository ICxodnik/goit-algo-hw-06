import networkx as nx
import matplotlib.pyplot as plt

# Створення графа (метро Києва)
graph = {
    'Головна': ['Кловська', 'Палац Спорту'],
    'Кловська': ['Головна', 'Палац Спорту', 'Арсенальна'],
    'Палац Спорту': ['Головна', 'Кловська', 'Печерська'],
    'Печерська': ['Палац Спорту', 'Арсенальна', 'Либідська'],
    'Арсенальна': ['Кловська', 'Печерська'],
    'Либідська': ['Печерська', 'Дружби Народів'],
    'Дружби Народів': ['Либідська', 'Голосіївська'],
    'Голосіївська': ['Дружби Народів', 'Виставковий центр'],
    'Виставковий центр': ['Голосіївська']
}

# Створення графа в networkx
G = nx.Graph(graph)


print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
degrees = dict(G.degree())
print("Ступінь кожної вершини:")
for node, degree in degrees.items():
    print(f"{node}: {degree}")

# Візуалізація графа
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=5, font_weight='bold', edge_color='gray')
plt.title("Транспортна мережа метрополітену Києва")
plt.show()






