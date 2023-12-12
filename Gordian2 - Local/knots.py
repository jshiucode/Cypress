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
        knots = find_knots(all_cycles, crossing_data_for_knots, crossing_data_for_links)
        return links
        # return {links: knots}    , then integrate as key/values into html

"""
Function that listifies cycles and traverses all cycles 
"""
def find_knots(all_cycles, crossing_data_knots, crossing_data_for_links) -> list:
    # listify cycles
    cycles = []
    for dict_cycle in all_cycles:
        cycles.append(listify_cycles(list(dict_cycle.keys())[0], dict_cycle, []))
    
    knotted_cycles = []
    for cycle in cycles:
        if cycle_is_knotted(cycle, crossing_data_knots, crossing_data_for_links):
            knotted_cycles.append(cycle)
    
    return knotted_cycles

"""
Knotting algorithm for each cycle
"""
def cycle_is_knotted(cycle, crossing_data_for_knots, crossing_data_for_links) -> bool:
    print("CYCLE: ", cycle)

    #initialize copy of crossing_data
    crossing_data_for_knots = crossing_data_for_knots.copy()

    #initialize a_2 at start
    a_2 = 0

    #get edges in cycle (with orientation)
    cycle_edges = []
    for indx, node in enumerate(cycle[0:len(cycle)-1]):
        edge = [int(node), int(cycle[indx+1])]
        cycle_edges.append(edge)

    #traverse cycle by edges
    for edge in cycle_edges:
        print(edge)
        for crossing in crossing_data_for_knots:
            if (crossing.under == [edge[0], edge[1]] or crossing.under == [edge[1], edge[0]]) and crossing.seen != True:
                # if reach a crossing haven't seen yet: switch to over crossing, add to seen data
                # print(crossing)
                crossing.switch_over_under()
                crossing.seen = True
                # print(crossing)

                # smooth the crossing, creating two disjoint cycles
                two_disjoint_cycles = smooth_crossing(crossing, cycle_edges)

                print(two_disjoint_cycles)

                # calculate the linking number of the two disjoint cycles
                a_2 += linking_number(two_disjoint_cycles, crossing_data_for_links)

    return True if a_2 != 0 else False

"""
Smooths the crossing
- returns two disjoint cycles
"""
def smooth_crossing(crossing, cycle_edges):
    print("SMOOTHING")
    print(crossing.over, crossing.under)
    # convert crossing class into correct orientation of the cycle
    for edge in cycle_edges:
        print(edge)
        edge.reverse()
        if crossing.over == edge:
            crossing.over = edge
        
        if crossing.under == edge:
            crossing.under = edge
        edge.reverse()
    
    # remove edges from crossing
    print(crossing.over, crossing.under)
    cycle_edges.remove(crossing.over)
    cycle_edges.remove(crossing.under)

    # 1st over -> 2nd under and 1st under -> 2nd over
    cycle_edges.append([crossing.over[0], crossing.under[1]])
    cycle_edges.append([crossing.under[0], crossing.over[1]])

    # !!!!!!!!!!!!!!!!!! CREATING NEW CROSSINGS?????

    return cycle_edges

def linking_number(two_disjoint_cycles, crossing_data_for_links):
    # initialize variables
    link_num = 0
    cycleA = []
    cycleB = []

    # seperate cycles helper function
    def seperate_cycles(disjoint_cycles):
        ## TO DO:
        # WRITE A RECURSIVE FUNCTION THAT SPLITS THIS LIST OF LISTS OF EDGES ([5,6], [6,7], ...) INTO TWO DISJOINT CYCLES
        # OF THE FORM [5,6,7,8,5] AND [1,2,3,4,1], FOR EXAMPLE
        print("PLACEHOLDER")

    # seperate cycles
    cycles = seperate_cycles(two_disjoint_cycles)
    cycleA = cycles[0]
    cycleB = cycles[1]



    # compare edges
    for a in range(len(cycleA)-1):
        for b in range(len(cycleB)-1):
            link_num += crossing_data_for_links[int(cycleA[a])][int(cycleA[a+1])][int(cycleB[b])][int(cycleB[b+1])]
    link_num = link_num/2

    return 0
        

Gordian("/unknot.txt")