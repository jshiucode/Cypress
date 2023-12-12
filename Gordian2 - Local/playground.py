"""
Helper DFS method to seperate list into two disjoint cycles
"""
def separate_cycles(edges):
    def dfs(node, cycle_number, start_node):
        visited[node] = True
        cycles[cycle_number].append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, cycle_number, start_node)

    # Create an undirected graph from the given edges
    graph = {}
    for edge in edges:
        u, v = edge
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    # Initialize variables
    visited = {node: False for node in graph}
    cycles = {1: [], 2: []}
    cycle_number = 1

    # Traverse the graph using DFS
    for node in graph:
        if not visited[node]:
            dfs(node, cycle_number, node)
            cycle_number += 1

    if len(cycles[1] > 0):
        cycles[1].append(cycles[1][0])
    if len(cycles[2] > 0):
        cycles[2].append(cycles[2][0])
    return cycles[1], cycles[2]

# Example usage:
edges = [[5, 6], [6, 7], [0, 1], [1, 2], [3, 4], [4, 5], [7, 3], [2, 0]]
cycle1, cycle2 = separate_cycles(edges)

print("Cycle 1:", cycle1)
print("Cycle 2:", cycle2)

