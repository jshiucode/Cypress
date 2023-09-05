"""
Python script which takes text file as input and outputs a graph
Input must be a .txt file with edges listed, then crossings
"""
import numpy as np
"""
create_graph: takes .txt file and outputs the graph
- Parameters: .txt file path
"""
def create_graph(filepath):
    graph = {}
    graph_data = open(str(filepath), 'r')
    for word in graph_data.readlines():
        word = word.replace(',', ' ').split()
        if(len(word) > 2): #is a crossing
            continue
        if word[0] not in graph.keys():
            graph[word[0]] = [word[1]]
        elif word[0] in graph.keys():
            graph[word[0]].append(word[1])

        # if => full edges | elif => 'directed' edges
        if word[1] not in graph.keys(): 
            graph[word[1]] = [word[0]]
        elif word[1] in graph.keys():
            graph[word[1]].append(word[0])
    return graph

"""
get_edges: returns set of edges from a graph
- Parameters: .txt file path containing graph edges (and crossings)
"""
def get_edges(filepath):
    edges = []
    graph_data = open(str(filepath), 'r')
    for word in graph_data.readlines():
        word = word.replace(',', ' ').split()
        if len(word) > 2:
            continue
        edges.append(word)
    return edges
"""
get_crossings: returns set of edges from a graph
- Parameters: .txt file path containing graph crossings (and edges)
"""
def get_crossings(filepath, graph):
    x = max([int(num) for num in list(graph.keys())]) + 1
    crossings = np.zeros((x,x,x,x)) #4 dimensional array with dimensions equal to highest signertex
    graph_data = open(str(filepath), 'r')
    for line in graph_data.readlines():
        line = line.replace(',', ' ').split()
        if len(line) == 7:
            a,b,c,d,sign = int(line[0]), int(line[1]), int(line[2]), int(line[3]), int(line[6])
            crossings[a][b][c][d] = sign
            crossings[a][b][d][c] = (-sign)
            crossings[b][a][c][d] = (-sign)
            crossings[b][a][d][c] = sign
            crossings[c][d][a][b] = sign
            crossings[d][c][a][b] = (-sign)
            crossings[c][d][b][a] = (-sign)
            crossings[d][c][b][a] = sign
    return crossings
