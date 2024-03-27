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
get_crossings_for_links: returns crossing data for use in link finding algorithm
- Parameters: .txt file path containing graph crossings (and edges)
"""
def get_crossings_for_links(filepath, graph):
    x = max([int(num) for num in list(graph.keys())]) + 1
    crossings = np.zeros((x,x,x,x)) #4 dimensional array with dimensions equal to highest signertex
    graph_data = open(str(filepath), 'r')
    for line in graph_data.readlines():
        line = line.replace(',', ' ').split()
        if len(line) == 7:
            a, b, c, d, sign = int(line[0]), int(line[1]), int(line[2]), int(line[3]), int(line[6])
            
            crossings[a][b][c][d] = sign
            crossings[a][b][d][c] = (-sign)
            crossings[b][a][c][d] = (-sign)
            crossings[b][a][d][c] = sign
            crossings[c][d][a][b] = sign
            crossings[d][c][a][b] = (-sign)
            crossings[c][d][b][a] = (-sign)
            crossings[d][c][b][a] = sign

    return crossings

"""
get_crossings_for_knots: returns dictionary of crossings. each crossing is an object of the crossing class. 
- Parameters: .txt file path containing graph crossings 
"""
class Crossing:
    def __init__(self, a, b, c, d, order_over, order_under, sign):
        self.over = [a, b]
        self.under = [c, d]
        self.seen = False
        self.order_over = order_over
        self.order_under = order_under
        self.sign = sign

    def __str__(self):
        return f"CROSSING => Over: {self.over}, Under: {self.under} Seen: {self.seen}, Over order: {self.order_over}, Under order: {self.order_under} "

    #for comparing crossings to eachother
    def representation(self):
        return f"CROSSING => Over: {sorted(self.over)}, Under: {sorted(self.under)} Seen: {self.seen}, Over order: {self.order_over}, Under order: {self.order_under} "

    def switch_over_under(self):
        placeholder = []
        placeholder = self.over
        self.over = self.under
        self.under = placeholder
        return self


def get_crossings_for_knots(filepath):
    crossing_list = []
    graph_data = open(str(filepath), 'r')
    for line in graph_data.readlines():
        line = line.replace(',', ' ').split()
        if len(line) == 7:
            a, b, c, d, order_a, order_b, sign = int(line[0]), int(line[1]), int(line[2]), int(line[3]), int(line[4]), int(line[5]), int(line[6])
            crossing = Crossing(a, b, c, d, order_a, order_b, sign)
            crossing_list.append(crossing)
    return crossing_list
