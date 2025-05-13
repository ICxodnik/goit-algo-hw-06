def print_table(distances, visited):
    # Верхній рядок таблиці
    print("\n {:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)
    
    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)
        
        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print("\n")

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)
        
        # Вивід таблиці після кожного кроку
        print_table(distances, visited)

    return distances
if __name__ == "__main__":
    # Приклад графа у вигляді словника
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
    # Виклик функції для вершини A
    dijkstra(graph, 'Головна')
