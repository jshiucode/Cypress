def split_into_cycles(edges):
    # Create a dictionary to represent the graph
    graph = {}
    for edge in edges:
        u, v = edge
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    # Perform a depth-first search to find cycles
    def dfs(node, visited, cycle):
        visited[node] = True
        cycle.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited, cycle)

    # Initialize variables
    visited = {node: False for node in graph}
    cycles = []

    # Iterate through all nodes
    for node in graph:
        if not visited[node]:
            cycle = []
            dfs(node, visited, cycle)
            cycles.append(cycle)

    if len(cycles) > 2:
        raise Exception("MORE THAN TWO CYCLES CREATED")

    if len(cycles) == 1:
        raise Exception("ONLY ONE CYCLE CREATED")

    return cycles[0], cycles[1]

# Example usage:
edges = [[1, 2], [2, 3], [3, 4], [4, 1], [5, 6], [6, 7], [7, 8], [8, 5]]
cycle1, cycle2 = split_into_cycles(edges)
print("Cycle 1:", cycle1)
print("Cycle 2:", cycle2)

edges1 = [[1,2], [3,4], [4,3]]
cycle1, cycle2 = split_into_cycles(edges1)
print("Cycle 1:", cycle1)
print("Cycle 2:", cycle2)




[[6, 7], [0, 1], [2, 3], [3, 4], [5, 2], [1, 6], [7, 5], [4, 0]]