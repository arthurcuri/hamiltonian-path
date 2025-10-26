def find_hamiltonian_path(graph, directed=False):
    n = len(graph)
    path = []
    visited = [False] * n
    
    def backtrack(vertex, depth):
        path.append(vertex)
        visited[vertex] = True
        
        if depth == n:
            return True
        
        for neighbor in range(n):
            if directed:
                can_visit = graph[vertex][neighbor] == 1
            else:
                can_visit = (graph[vertex][neighbor] == 1 or graph[neighbor][vertex] == 1)
            
            if can_visit and not visited[neighbor]:
                if backtrack(neighbor, depth + 1):
                    return True
        
        path.pop()
        visited[vertex] = False
        return False
    
    for start in range(n):
        if backtrack(start, 1):
            return path
    
    return None