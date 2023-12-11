"""
Function that uses cycles and crossing data to find knots
"""

from graph_creator import create_graph, get_crossings_for_links, get_edges
from fundamental_set_cycles import find_fund_set
from all_cycles import find_all_cycles
from helpers import dictify_cycles, listify_cycles
from links import find_links

"""
FOR TESTING KNOTS.PY ONLY:
"""
# def Gordian(graph_filepath):
#     if graph_filepath != 'favicon.ico':
#         print("================ Graph_filepath ================ ", graph_filepath)
#         graph  = create_graph("./Graph data files/" + graph_filepath)
#         graph_edges = get_edges("./Graph data files/" + graph_filepath)
#         crossings = get_crossings("./Graph data files/" + graph_filepath, graph)
#         fundamental_set_cycles = find_fund_set(graph, graph_edges)
#         all_cycles = find_all_cycles(dictify_cycles(fundamental_set_cycles))
#         links = find_links(all_cycles, crossings)
#         # FOR WHEN KNOT FUNCTION IS MADE:
#         print(find_knots(all_cycles, crossings))
#         return 0
#         # return {links: knots}    , then integrate as key/values into html

"""
Function that listifies cycles and traverses all cycles 
"""
def find_knots(all_cycles, crossings) -> list:
    # listify cycles
    cycles = []
    for dict_cycle in all_cycles:
        cycles.append(listify_cycles(list(dict_cycle.keys())[0], dict_cycle, []))
    
    knotted_cycles = []
    for cycle in cycles:
        if cycle_is_knotted(cycle, crossings):
            knotted_cycles.append(cycle)
    
    return knotted_cycles

"""
Knotting algorithm for each cycle
"""
def cycle_is_knotted(cycle, crossings) -> bool:
    print("CYCLE: ", cycle)

    #initialize copy of crossing_data and crossing_seen data
    crossing_lk_num = crossings.copy()
    crossing_seen = set()

    #initialize a_2 at start
    a_2 = 0

    #get edges in cycle (with orientation)
    cycle_edges = []
    for indx, node in enumerate(cycle[0:len(cycle)-1]):
        edge = [int(node), int(cycle[indx+1])]
        cycle_edges.append(edge)

    #traverse cycle by edges
    for edge in cycle_edges:
        if is_unseen_undercrossing(edge, crossing_lk_num, cycle_edges)[1]:
            
            #add crossing to crossing_seen

            #smooth
            print("PLACEHOLDER")

        


    # return True if a_2 != 0 else False

def is_unseen_undercrossing(edge, crossing_data, cycle_edges):
    crossing_seen = [[], False]
    cycle_edges.remove(edge)
    for other_edge in cycle_edges:
        print("PLACEHOLDER")

    return crossing_seen

# Gordian("/unknot.txt")