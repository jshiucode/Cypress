"""
Function that uses cycles and crossing data to find knots
"""

from graph_creator import create_graph, get_crossings_for_links, get_edges, get_crossings_for_knots
from fundamental_set_cycles import find_fund_set
from all_cycles import find_all_cycles
from helpers import dictify_cycles, listify_cycles
from links import find_links

"""
FOR TESTING KNOTS.PY ONLY:
"""
def Gordian(graph_filepath):
    if graph_filepath != 'favicon.ico':
        print("================ Graph_filepath ================ ", graph_filepath)
        graph  = create_graph("./Graph data files/" + graph_filepath)
        graph_edges = get_edges("./Graph data files/" + graph_filepath)
        crossing_data_for_links = get_crossings_for_links("./Graph data files/" + graph_filepath, graph)
        crossing_data_for_knots = get_crossings_for_knots("./Graph data files/" + graph_filepath)
        fundamental_set_cycles = find_fund_set(graph, graph_edges)
        all_cycles = find_all_cycles(dictify_cycles(fundamental_set_cycles))
        links = find_links(all_cycles, crossing_data_for_links)
        # FOR WHEN KNOT FUNCTION IS MADE:
        knots = find_knots(all_cycles, crossing_data_for_knots)
        return links
        # return {links: knots}    , then integrate as key/values into html

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

    #initialize copy of crossing_data
    crossings = crossings.copy()

    #initialize a_2 at start
    a_2 = 0

    #get edges in cycle (with orientation)
    cycle_edges = []
    for indx, node in enumerate(cycle[0:len(cycle)-1]):
        edge = [int(node), int(cycle[indx+1])]
        cycle_edges.append(edge)

    #traverse cycle by edges
    for edge in cycle_edges:
        # print(edge)
        for crossing in crossings:
            if (crossing.under == [edge[0], edge[1]] or crossing.under == [edge[1], edge[0]]) and crossing.seen != True:
                # if reach a crossing haven't seen yet: switch to over crossing, add to seen data
                # print(crossing)
                crossing.switch_over_under()
                crossing.seen = True
                # print(crossing)

                #TO DO:

                #SMOOTH

                #CALCULATE LINKING NUMBER

    return True if a_2 != 0 else False

Gordian("/unknot.txt")