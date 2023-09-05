"""
give cycle: Given spanning tree, find common parent between two edges,
            then put paths together and form cycle
"""

"""
Combine two paths and an edge to return a cycle
"""
def give_cycle(spanning_tree, edge):
    cycle = []
    path1 = []
    path2 = []
    i = edge[0]
    path1.append(i)
    while spanning_tree[i] != None:
        path1.append(spanning_tree[i])
        i = spanning_tree[i]

    i = edge[1]
    path2.append(i)
    while spanning_tree[i] != None:
        if spanning_tree[i] in path1:
            path1 = path1[:path1.index(spanning_tree[i])+1]
            break
        path2.append(spanning_tree[i])
        i = spanning_tree[i]
     
    path2.reverse()
    return path1 + path2 + [path1[0]]

#Test good
# tree = {'0': None, '1': '0', '2': '0'}
# edge = ['1', '2']
# print(give_cycle(tree, edge))

#Test h11 good
# tree = {'0': None, '1': '0', '6': '0', '9': '0', '10': '0', '2': '1', '3': '1', '7': '6', '4': '2', '5': '3', '8': '3'}
# edge = ['5', '9']
# print(give_cycle(tree, edge))

#Test h11
# tree = {'0': None, '1': '0', '6': '0', '9': '0', '10': '0', '2': '1', '3': '1', '7': '6', '4': '2', '5': '3', '8': '3'}
# edge = ['4', '5']
# print(give_cycle(tree, edge))