import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

graph = {
    # Південь
    'Odesa': ['Mykolaiv', 'Vinnytsia'],
    'Mykolaiv': ['Odesa', 'Kherson', 'Kryvyi Rih'],
    'Kherson': ['Mykolaiv', 'Simferopol', 'Sevastopol', 'Melitopol'],
    'Simferopol': ['Sevastopol', 'Kherson'],
    'Sevastopol': ['Simferopol', 'Kherson'],
    'Melitopol': ['Kherson', 'Zaporizhzhia'],
    
    # Центр
    'Uman': ['Kyiv', 'Vinnytsia', 'Kropyvnytskyi'],
    'Kropyvnytskyi': ['Uman', 'Dnipro', 'Kryvyi Rih'],
    'Vinnytsia': ['Uman', 'Odesa', 'Zhytomyr'],
    'Kryvyi Rih': ['Mykolaiv', 'Kropyvnytskyi', 'Dnipro'],
    'Poltava': ['Kyiv', 'Kharkiv'],

    # Схід
    'Dnipro': ['Zaporizhzhia', 'Kharkiv', 'Donetsk', 'Kropyvnytskyi', 'Kryvyi Rih'],
    'Donetsk': ['Dnipro', 'Kharkiv', 'Mariupol'],
    'Mariupol': ['Donetsk'],
    'Zaporizhzhia': ['Dnipro', 'Melitopol'],
    'Kharkiv': ['Dnipro', 'Donetsk', 'Poltava', 'Sumy'],
    'Luhansk': ['Donetsk'],

    # Північ
    'Kyiv': ['Uman', 'Zhytomyr', 'Chernihiv', 'Poltava'],
    'Chernihiv': ['Kyiv'],
    'Sumy': ['Kharkiv'],
    'Zhytomyr': ['Vinnytsia', 'Kyiv'],

    # Захід
    'Lviv': ['Ivano-Frankivsk', 'Ternopil', 'Lutsk'],
    'Ivano-Frankivsk': ['Lviv', 'Chernivtsi'],
    'Ternopil': ['Lviv', 'Khmelnytskyi'],
    'Khmelnytskyi': ['Ternopil', 'Vinnytsia'],
    'Chernivtsi': ['Ivano-Frankivsk'],
    'Lutsk': ['Lviv', 'Rivne'],
    'Rivne': ['Lutsk', 'Zhytomyr'],
}

# Регіони
regions = {
    'South': ['Odesa', 'Mykolaiv', 'Kherson', 'Melitopol'],
    'Center': ['Uman', 'Vinnytsia', 'Kropyvnytskyi', 'Kryvyi Rih', 'Poltava', 'Zhytomyr'],
    'East': ['Dnipro', 'Donetsk', 'Mariupol', 'Zaporizhzhia', 'Kharkiv', 'Luhansk'],
    'North': ['Kyiv', 'Chernihiv', 'Sumy'],
    'West': ['Lviv', 'Ivano-Frankivsk', 'Ternopil', 'Khmelnytskyi', 'Chernivtsi', 'Lutsk', 'Rivne'],
    'Crimea': ['Simferopol', 'Sevastopol']
}

region_colors = {
    'South': 'gold',
    'Center': 'lightgreen',
    'East': 'tomato',
    'North': 'lightskyblue',
    'West': 'orchid',
    'Crimea': 'lightgray'
}

# Побудова графа
G = nx.Graph(graph)

print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
degrees = dict(G.degree())
print("Ступінь кожної вершини:")
for node, degree in degrees.items():
    print(f"{node}: {degree}")

# Присвоєння кольорів вузлам за регіонами
node_colors = []
for node in G.nodes():
    for region, cities in regions.items():
        if node in cities:
            node_colors.append(region_colors[region])
            break
    else:
        node_colors.append('white')  # Якщо не знайдено регіон

# Розташування вузлів автоматичне
pos = nx.spring_layout(G, seed=42, k=0.4)

# Малювання
plt.figure(figsize=(16, 12))
plt.title("Граф міст України за регіонами", fontsize=16)

# Вузли
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2000)

# Мітки
nx.draw_networkx_labels(G, pos, font_size=7)

# Ребра (усі одного кольору)
nx.draw_networkx_edges(G, pos, edge_color='gray', width=1.5)

# Легенда
legend_elements = [Patch(facecolor=color, label=region) for region, color in region_colors.items()]
plt.legend(handles=legend_elements, title="Регіони", loc='upper center', ncol=3)

plt.axis('off')
plt.tight_layout()
plt.show()