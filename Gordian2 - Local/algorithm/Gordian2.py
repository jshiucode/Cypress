from .graph_creator import create_graph, get_crossings_for_links, get_edges, get_crossings_for_knots
from .fundamental_set_cycles import find_fund_set
from .all_cycles import find_all_cycles
from .helpers import dictify_cycles
from .links import find_links
from .knots import find_knots


from .links import listify_cycles
from .links import find_links
import time

"""
Full integration of all other files
Used for API
"""
def Gordian(graph_data):
    if graph_data != 'favicon.ico':
        start_time = time.time()
        print("================ graph_data ================ ", graph_data)
        graph  = create_graph(graph_data)
        graph_edges = get_edges(graph_data)
        crossing_data_for_links = get_crossings_for_links(graph_data, graph)
        crossing_data_for_knots = get_crossings_for_knots(graph_data)
        fundamental_set_cycles = find_fund_set(graph, graph_edges)
        all_cycles = find_all_cycles(dictify_cycles(fundamental_set_cycles))
        links = find_links(all_cycles, crossing_data_for_links)

        # FOR WHEN KNOT FUNCTION IS MADE:
        knots = find_knots(all_cycles, crossing_data_for_knots, crossing_data_for_links)

        end_time = time.time()
        elapsed_time = end_time - start_time

        return links, elapsed_time, knots

inp = input()
i = "/Gordian2 - Local/Graph data files" + inp
print(Gordian(i))
