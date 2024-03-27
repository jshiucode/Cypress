"""
Turns dictionary formatted cycle into oriented list formatted cycle
"""
def listify_cycles(loc, cycle, graveyard):
    graveyard.append(loc)
    for next in cycle[loc]:
        if next in graveyard:
            continue
        elif next not in graveyard:
            return listify_cycles(next, cycle, graveyard)
    return graveyard + [graveyard[0]]



"""
Converts all cycles in fundamental set of cycles from list form to dictionary form
"""
def dictify_cycles(fundamental_set):
    cycles_dictified = []
    for cycle in fundamental_set:
        dic_cycle = {}
        if cycle[0] != cycle[len(cycle)-1]:
            print("Invalid Cycle:", cycle)
            continue
        for i in range(len(cycle)-1):
            if cycle[i] not in dic_cycle.keys():
                dic_cycle[cycle[i]] = [str(cycle[i+1])]
            elif cycle[i] in dic_cycle.keys():
                dic_cycle[cycle[i]].append(str(cycle[i+1]))
            if cycle[i+1] not in dic_cycle.keys():
                dic_cycle[cycle[i+1]] = [str(cycle[i])]
            elif cycle[i+1] in dic_cycle.keys():
                dic_cycle[cycle[i+1]].append(str(cycle[i]))
        cycles_dictified.append(dic_cycle)

    return cycles_dictified

"""
Outputs list of all binary strings (list form) of length n
"""
def bin_strings(n):
    def genbin(n, bin_strings, bs = []):
        if len(bs) == n:
            bin_strings.append(bs)
        else:
            genbin(n, bin_strings, bs + [0])
            genbin(n, bin_strings, bs + [1])

    bin_strings = []
    genbin(n, bin_strings, bs = [])
    bin_strings.remove([0] * n)
    return bin_strings

"""
Takes in list of edges (each edge in in list form) and outputs the two disjoint cycles in list form
"""
def seperate_cycles(edges):
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

    if len(cycles) < 2:
        raise Exception("ONLY ONE CYCLE CREATED")

    #append extra vertex to complete the cycle
    cycles[0].append(cycles[0][0])
    cycles[1].append(cycles[1][0])

    return cycles[0], cycles[1]


"""
Takes in a cycle of nodes in string form and returns the oriented cycle starting at the smallest node:
ex: input = ['5', '6', '7', '1', '2', '3', '4', '5']
    output = [1, 2, 3, 4, 5, 6, 7, 1]
"""
def orient_cycle_at_smallest(cycle):
    cycle = [int(node) for node in cycle]
    smallest = min(cycle)
    hold_cycle = []
    end_cycle = []
    for i, node in enumerate(cycle):
        if i == 0 and node == smallest:
            return cycle
        if node == smallest:
            end_cycle.extend(cycle[i:])
            break
        else:
            hold_cycle.append(node)
    
    end_cycle.extend(hold_cycle[1:])
    end_cycle.append(smallest)
    return end_cycle

# print(orient_cycle_at_smallest(['5', '6', '7', '1', '2', '3', '4', '5']))
# t1 = ['5', '9', '8', '1', '5']
# print(orient_cycle_at_smallest(t1))
