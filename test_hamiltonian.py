from main import find_hamiltonian_path

# Undirected graph (triangle)
graph1 = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
result1 = find_hamiltonian_path(graph1, directed=False)
print(f"Path found: {result1}")

# Undirected graph (square)
graph2 = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]
result2 = find_hamiltonian_path(graph2, directed=False)
print(f"Path found: {result2}")

# Directed graph
graph3 = [
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
result3 = find_hamiltonian_path(graph3, directed=True)
print(f"Path found: {result3}")

# Graph with no Hamiltonian path
graph4 = [
    [0, 1, 0],
    [1, 0, 0],
    [0, 0, 0]
]
result4 = find_hamiltonian_path(graph4, directed=False)
print(f"Path found: {result4}")

# Undirected graph
graph5 = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0]
]
result5 = find_hamiltonian_path(graph5, directed=False)
print(f"Path found: {result5}")