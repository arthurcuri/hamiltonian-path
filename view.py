import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from main import find_hamiltonian_path
import os

def visualize_hamiltonian_path(graph, directed=False, output_file='assets/hamiltonian_path.png'):
    n = len(graph)
    hamiltonian_path = find_hamiltonian_path(graph, directed)
    
    if directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    
    G.add_nodes_from(range(n))
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                G.add_edge(i, j)
    
    pos = nx.spring_layout(G, seed=42, k=2, iterations=50)
    plt.figure(figsize=(12, 8))
    
    if directed:
        nx.draw_networkx_edges(G, pos, edge_color='lightgray', 
                              width=2, alpha=0.6, arrows=True,
                              arrowsize=20, arrowstyle='->',
                              connectionstyle='arc3,rad=0.1')
    else:
        nx.draw_networkx_edges(G, pos, edge_color='lightgray', 
                              width=2, alpha=0.6)
    
    if hamiltonian_path:
        path_edges = [(hamiltonian_path[i], hamiltonian_path[i+1]) 
                     for i in range(len(hamiltonian_path)-1)]
        
        if directed:
            nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                                  edge_color='red', width=4, alpha=0.8,
                                  arrows=True, arrowsize=25,
                                  arrowstyle='->', connectionstyle='arc3,rad=0.1')
        else:
            nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                                  edge_color='red', width=4, alpha=0.8)
    
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                          node_size=800, alpha=0.9,
                          edgecolors='darkblue', linewidths=2)
    
    nx.draw_networkx_labels(G, pos, font_size=16, 
                           font_weight='bold', font_color='black')
    
    if hamiltonian_path:
        title = f'Hamiltonian Path Found: {" → ".join(map(str, hamiltonian_path))}'
        plt.title(title, fontsize=14, fontweight='bold', color='darkgreen')
    else:
        plt.title('Graph - No Hamiltonian Path Found', 
                 fontsize=14, fontweight='bold', color='darkred')
    
    legend_elements = [
        Line2D([0], [0], color='lightgray', linewidth=2, label='Graph edges'),
        Line2D([0], [0], color='red', linewidth=4, label='Hamiltonian path'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='lightblue', 
               markersize=10, markeredgecolor='darkblue', markeredgewidth=2, 
               label='Vertices', linestyle='None')
    ]
    plt.legend(handles=legend_elements, loc='upper right', fontsize=10)
    
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()

def visualize_multiple_graphs():
    if not os.path.exists('assets'):
        os.makedirs('assets')
    
    # Undirected graph (triangle)
    graph1 = [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
    visualize_hamiltonian_path(graph1, directed=False, 
                               output_file='assets/example1_triangle.png')
    
    # Undirected graph (square)
    graph2 = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    visualize_hamiltonian_path(graph2, directed=False, 
                               output_file='assets/example2_square.png')
    
    # Directed graph
    graph3 = [
        [0, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]
    visualize_hamiltonian_path(graph3, directed=True, 
                               output_file='assets/example3_directed.png')
    
    # Graph with no Hamiltonian path
    graph4 = [
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 0]
    ]
    visualize_hamiltonian_path(graph4, directed=False, 
                               output_file='assets/example4_no_path.png')
    
    # Undirected graph (pentagon)
    graph5 = [
        [0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0]
    ]
    visualize_hamiltonian_path(graph5, directed=False, 
                               output_file='assets/example5_pentagon.png')

if __name__ == "__main__":
    visualize_multiple_graphs()
