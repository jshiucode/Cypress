"""
Function that uses cycles and crossing data to find knots
"""

from graph_creator import create_graph, get_crossings, get_edges
from fundamental_set_cycles import find_fund_set
from all_cycles import find_all_cycles
from helpers import dictify_cycles, listify_cycles
from links import find_links

def Gordian(graph_filepath):
    if graph_filepath != 'favicon.ico':
        print("================ Graph_filepath ================ ", graph_filepath)
        graph  = create_graph("./Graph data files/" + graph_filepath)
        graph_edges = get_edges("./Graph data files/" + graph_filepath)
        crossings = get_crossings("./Graph data files/" + graph_filepath, graph)
        fundamental_set_cycles = find_fund_set(graph, graph_edges)
        all_cycles = find_all_cycles(dictify_cycles(fundamental_set_cycles))
        links = find_links(all_cycles, crossings)
        # FOR WHEN KNOT FUNCTION IS MADE:
        find_knots(all_cycles, crossings)
        return 0
        # return {links: knots}    , then integrate as key/values into html

def find_knots(all_cycles, crossings):
    # listify cycles
    cycles = []
    for dict_cycle in all_cycles:
        cycles.append(listify_cycles(list(dict_cycle.keys())[0], dict_cycle, []))
    
    for cycle in cycles:
        start_v = cycle[0]
        for indx in range(0, len(cycle)-1):
            edge = [cycle[indx], cycle[indx+1]]




#SEE FIND_LINKS function for helper function to find linking number
#see Lowell's code, understand how he saves over/under crossing data and crossing data order

Gordian("/c12.txt")