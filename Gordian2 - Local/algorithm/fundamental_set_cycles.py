"""
Algorithm from Keith Paton paper for finding fundamental set of cycles of a graph
"""

# import graph_creator 
# graph = graph_creator.graph
# edges = graph_creator.graph_edges
from find_cycle import give_cycle

def find_fund_set(graph, edges):
    V = list(graph.keys()) #change name to vertices
    T = [] #change name to v_spanning_tree
    X = list(graph.keys()) #change name to vertex_queue

    spanning_tree = {}

    fundamental_set_cycles = [] #set of all fundamental cycles


    T.append(V[0])
    T_intersect_X = [value for value in T if value in X]
    while(len(T_intersect_X) != 0):
        # print("Spanning tree: ", spanning_tree)
        z = T_intersect_X[0]
        # print("z:", z)
        examine = []
        examine_reversed = [] #edges that must be reversed
        for edge in edges:
            if edge[0] == str(z):
                examine.append(edge)
            if edge[1] == str(z): #non-directed tree, we must account for edges with reversed order
                edge.reverse()
                examine_reversed.append(edge)
            else:
                continue
        # print("to examine: ", examine + examine_reversed)
        for examine_edge in examine + examine_reversed:
            # print("examine_edge: ", examine_edge)
            w = str(examine_edge[1])
            if w in T:
                #find cycle
                fundamental_set_cycles.append(give_cycle(spanning_tree, examine_edge))
            elif w not in T:
                #add z->w to the tree
                if z not in spanning_tree:
                    spanning_tree[z] = None
                spanning_tree[w] = z

                T.append(str(w))

            if examine_edge in examine:
                edges.remove(examine_edge)
            elif examine_edge in examine_reversed:
                examine_edge.reverse()
                edges.remove(examine_edge)

        X.remove(z)
        T_intersect_X = [value for value in T if value in X]
        # print('T: ', T)
        # print('X: ', X)
        # print('T_intersect_X: ', T_intersect_X)
        # print('')
    return fundamental_set_cycles

#Spanning tree is from vertex to it's parents
# print("Spanning Tree: ", spanning_tree)
# print('Fundamental set of cycles: ', fundamental_set_cycles)









