"""
Function that uses cycles and crossing data to find knots
"""

from graph_creator import create_graph, get_crossings_for_links, get_edges, get_crossings_for_knots
from fundamental_set_cycles import find_fund_set
from all_cycles import find_all_cycles
from helpers import dictify_cycles, listify_cycles, seperate_cycles, orient_cycle_at_smallest
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
        print(all_cycles)
        links = find_links(all_cycles, crossing_data_for_links)
        # FOR WHEN KNOT FUNCTION IS MADE:
        knots = find_knots(all_cycles, crossing_data_for_knots, crossing_data_for_links)
        return links, knots

"""
Function that listifies cycles and traverses all cycles, returns knotted cycles 
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
Smooths the crossing
- returns two disjoint cycles
- built into cycle_is_knotted() to access crossing_data_for_knots and crossing_data_for_links as local variables
"""
def smooth_crossing(crossing, cycle_edges, crossing_data_for_links, crossing_data_for_knots):
    # print("SMOOTHING")
    # print("SMOOTHING:", crossing)
    
    # remove crossing edges from cycle
    if crossing.over in cycle_edges:
            cycle_edges.remove(crossing.over)
    if crossing.under in cycle_edges:
            cycle_edges.remove(crossing.under)

    # add in smoothed edges
    cycle_edges.append([crossing.over[0], crossing.under[1]])
    cycle_edges.append([crossing.under[0], crossing.over[1]])

    for inspected_crossing in crossing_data_for_knots:
        if inspected_crossing.representation() == crossing.representation():
            continue
        crossing_data_for_links = check_crossing_order(inspected_crossing, crossing, crossing_data_for_links, crossing_data_for_knots)

    return cycle_edges, crossing_data_for_links

"""
Orients crossing object with cycle's orientation. Edits crossing sign accordingly
"""
def orient_crossing(crossing, edges):
    crossing_changes = 0
    for edge in edges:
        if edge == [crossing.over[1], crossing.over[0]]:
            crossing.over = edge
            crossing_changes += 1
        if edge == [crossing.under[1], crossing.under[0]]:
            crossing.under = edge
            crossing_changes += 1
    
    if crossing_changes == 1:
        crossing.sign = -crossing.sign
    
    return crossing

"""
Knotting algorithm for each cycle
"""
def cycle_is_knotted(cycle, crossing_data_for_knots, crossing_data_for_links) -> bool:
    #orient the cycle correctly, start at 0 so all edges are [a,b] such that a < b
    print("cycle before func", cycle)
    cycle = orient_cycle_at_smallest(cycle)
    print("cycle oriented", cycle)

    #initialize copy of crossing_data
    crossing_data_for_knots = crossing_data_for_knots.copy()

    #initialize a_2 at start
    a_2 = 0

    #get edges in cycle (with orientation being smallest node to largest node)
    cycle_edges = []
    for indx, node in enumerate(cycle[0:len(cycle)-1]):
        edge = [int(node), int(cycle[indx+1])]
        cycle_edges.append(edge)

    #traverse cycle by edges
    # print("START CYCLE EDGES", cycle_edges)
    start_cycle = cycle_edges.copy()

    #orient all crossings to cycle's orientation
    for crossing in crossing_data_for_knots:
        print("crossing before orient", crossing)
        crossing = orient_crossing(crossing, cycle_edges)
        print("crossing after orient", crossing)

    for edge in cycle_edges:

        print("edge", edge)
        # print("EDGE LOOKING AT:", edge)

        for crossing in crossing_data_for_knots:

            #if we see an undercrossing we havent seen yet, and the over crossing is in the cycle
            if (crossing.under == [edge[0], edge[1]]) and (crossing.seen != True) and (crossing.over in cycle_edges):

                # if reach a crossing haven't seen yet: switch to over crossing, add to seen data
                crossing.seen = True
                # print(crossing)

                # smooth the crossing, creating two disjoint cycles
                two_disjoint_cycles, crossing_data_for_links = smooth_crossing(crossing, cycle_edges, crossing_data_for_links, crossing_data_for_knots)

                # remove the crossing that has been smoothed
                crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, crossing.over[0], crossing.over[1], crossing.under[0], crossing.under[1], 0)
                
                # calculate the linking number of the two disjoint cycles
                a_2 -= linking_number(two_disjoint_cycles, crossing_data_for_links)
                print("a2", a_2)

                #remove smoothed edges
                cycle_edges.remove([crossing.over[0], crossing.under[1]])
                cycle_edges.remove([crossing.under[0], crossing.over[1]])

                #crossing edges need to be added back into cycle with switched under/over
                cycle_edges.insert(start_cycle.index(crossing.over), crossing.over)
                cycle_edges.insert(start_cycle.index(crossing.under), crossing.under)
                crossing.switch_over_under()
                # print("CYCLE EDGES AFTER SMOOTH", cycle_edges)

                #switch sign of crossing in link data
                crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, crossing.over[0], crossing.over[1], crossing.under[0], crossing.under[1], 
                                        -crossing_data_for_links[crossing.over[0]][crossing.over[1]][crossing.under[0]][crossing.under[1]])

    return True if a_2 != 0 else False

"""
Update the crossing_data_for_links matrix depending on crossing order after smoothing
- params: 
- return: crossing_data_for_links
"""
def check_crossing_order(inspected_crossing, crossing, crossing_data_for_links, crossing_data_for_knots):
    # !! for the following comments, go by diagram dranw on iPad 'Meeting 1.18 on fixing smoothing'
    # print("inspected_crossing:", inspected_crossing)
    # print("crossing:", crossing)

    # if inspected_crossing and crossing do not share any edges, continue
    if (inspected_crossing.over != crossing.over and
        inspected_crossing.under != crossing.under and
        inspected_crossing.over != crossing.under and
        inspected_crossing.under != crossing.over):
        # print("NO SHARED EDGES")
        return crossing_data_for_links
    
    # inspected_crossing and crossing share edges
    #TODO: PUT IN CORRECT ALGORITHM FOR EDITING CROSSINGS GIVEN ORDER OF CROSSINGS

    # -a crossing (SHARED OVER):
    if (inspected_crossing.over == crossing.under) and inspected_crossing.order_over < crossing.order_under:
        # if crossing goes through to other edge, both inspected crossing and through crossing disappear
        for through_crossing in crossing_data_for_knots:
                if through_crossing.over == crossing.over and through_crossing.order_over > crossing.order_over:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

                if through_crossing.under == crossing.over and through_crossing.order_under > crossing.order_over:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

        # change crossing_data_for_links accordingly (not special through case)
        # inspected crossing's over goes from (a,b) to (a,d)
        crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, crossing.under[0], crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], inspected_crossing.sign)

    # -a crossing (SHARED UNDER):
    if (inspected_crossing.under == crossing.under) and inspected_crossing.order_under < crossing.order_under:
        # if crossing goes through to other edge, both inspected crossing and through crossing disappear
        for through_crossing in crossing_data_for_knots:
                if through_crossing.over == crossing.over and through_crossing.order_over > crossing.order_over:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

                if through_crossing.under == crossing.over and through_crossing.order_under > crossing.order_over:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

        # change crossing_data_for_links accordingly (not special through case)
        # inspected crossing's under goes from (a,b) to (a,d)
        crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], crossing.under[0], crossing.over[1], inspected_crossing.sign)
        # change crossing_data_for_links accordingly (not special through case)

    # -b crossing (SHARED OVER):
    if (inspected_crossing.over == crossing.under) and inspected_crossing.order_over > crossing.order_under:
        # if crossing goes through to other edge, both inspected crossing and through crossing disappear
        for through_crossing in crossing_data_for_knots:
                if through_crossing.over == crossing.over and through_crossing.order_over < crossing.order_over:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

                if through_crossing.under == crossing.over and through_crossing.order_under < crossing.order_over:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

        # change crossing_data_for_links accordingly (not special through case)
        # inspected crossing's over goes from (a,b) to (c,b)
        crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, crossing.over[0], crossing.under[1], inspected_crossing.under[0], inspected_crossing.under[1], inspected_crossing.sign)

    # -b crossing (SHARED UNDER):
    if (inspected_crossing.under == crossing.under) and inspected_crossing.order_under > crossing.order_under:
        # if crossing goes through to other edge, both inspected crossing and through crossing disappear
        for through_crossing in crossing_data_for_knots:
                if through_crossing.over == crossing.over and through_crossing.order_over < crossing.order_over:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

                if through_crossing.under == crossing.over and through_crossing.order_under < crossing.order_over:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

        # change crossing_data_for_links accordingly (not special through case)
        # inspected crossing's under goes from (a,b) to (c,b)
        crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], crossing.over[0], crossing.under[1], inspected_crossing.sign)


    # -c crossing (SHARED OVER):
    if (inspected_crossing.over == crossing.over) and inspected_crossing.order_over < crossing.order_over:
        # if crossing goes through to other edge, both inspected crossing and through crossing disappear
        for through_crossing in crossing_data_for_knots:
                if through_crossing.over == crossing.under and through_crossing.order_over > crossing.order_under:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

                if through_crossing.under == crossing.under and through_crossing.order_under > crossing.order_under:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

        # change crossing_data_for_links accordingly (not special through case)
        # inspected crossing's over goes from (c,d) to (c,b)
        crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, crossing.over[0], crossing.under[1], inspected_crossing.under[0], inspected_crossing.under[1], inspected_crossing.sign)

    # -c crossing (SHARED UNDER):
    if (inspected_crossing.under == crossing.over) and inspected_crossing.order_over > crossing.order_over:
        # if crossing goes through to other edge, both inspected crossing and through crossing disappear
        for through_crossing in crossing_data_for_knots:
                if through_crossing.over == crossing.under and through_crossing.order_over > crossing.order_under:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

                if through_crossing.under == crossing.under and through_crossing.order_under > crossing.order_under:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

        # change crossing_data_for_links accordingly (not special through case)
        # inspected crossing's under goes from (c,d) to (c,b)
        crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], crossing.over[0], crossing.under[1], inspected_crossing.sign)


    # -d crossing (SHARED OVER):
    if (inspected_crossing.over == crossing.over) and inspected_crossing.order_over > crossing.order_over:
        # if crossing goes through to other edge, both inspected crossing and through crossing disappear
        for through_crossing in crossing_data_for_knots:
                if through_crossing.over == crossing.under and through_crossing.order_over < crossing.order_under:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

                if through_crossing.under == crossing.under and through_crossing.order_under < crossing.order_under:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

        # change crossing_data_for_links accordingly (not special through case)
        # inspected crossing's over goes from (c,d) to (a,d)
        crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, crossing.under[0], crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], inspected_crossing.sign)

    # -d crossing (SHARED UNDER):
    if (inspected_crossing.under == crossing.over) and inspected_crossing.order_over > crossing.order_over:
        # if crossing goes through to other edge, both inspected crossing and through crossing disappear
        for through_crossing in crossing_data_for_knots:
                if through_crossing.over == crossing.under and through_crossing.order_over < crossing.order_under:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

                if through_crossing.under == crossing.under and through_crossing.order_under < crossing.order_under:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

        # change crossing_data_for_links accordingly (not special through case)
        # inspected crossing's under goes from (c,d) to (a,d)
        crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], crossing.under[0], crossing.over[1], inspected_crossing.sign)





    return crossing_data_for_links


"""
Find the linking number of the two disjoint cycles
"""
def linking_number(two_disjoint_cycles, crossing_data_for_links):
    # initialize variables
    link_num = 0
    cycleA = []
    cycleB = []

    # seperate cycles
    # print("disjoint cycles: ", two_disjoint_cycles)
    cycleA, cycleB = seperate_cycles(two_disjoint_cycles)
    print("cycleA:", cycleA)
    print("cycleB", cycleB)
    # print("seperated into: ", cycleA, cycleB)

    # compare edges
    for a in range(len(cycleA)-1):
        for b in range(len(cycleB)-1):
            #print statement is inspecting lk# between each edge
            # print("cycleA egde", [cycleA[a],cycleA[a+1]], "cycleB egde", [cycleB[b], cycleB[b+1]], "lk = ", crossing_data_for_links[int(cycleA[a])][int(cycleA[a+1])][int(cycleB[b])][int(cycleB[b+1])])
            print(crossing_data_for_links[int(cycleA[a])][int(cycleA[a+1])][int(cycleB[b])][int(cycleB[b+1])])
            if crossing_data_for_links[int(cycleA[a])][int(cycleA[a+1])][int(cycleB[b])][int(cycleB[b+1])] > 0:
                print(crossing_data_for_links[int(cycleA[a])][int(cycleA[a+1])][int(cycleB[b])][int(cycleB[b+1])])
                print("edge1", [cycleA[a],cycleA[a+1]], "edge2", [cycleB[b], cycleB[b+1]])
            link_num += crossing_data_for_links[int(cycleA[a])][int(cycleA[a+1])][int(cycleB[b])][int(cycleB[b+1])]
    link_num = link_num/2

    # print("LINKING NUMBER:", link_num)

    return link_num

"""
For correctly editing the crossing_data_for_links matrix when calculating linking number
"""
def edit_crossing_data_for_links(crossings, a,b,c,d,value):
    crossings[a][b][c][d] = value
    crossings[a][b][d][c] = (-value)
    crossings[b][a][c][d] = (-value)
    crossings[b][a][d][c] = value
    crossings[c][d][a][b] = value
    crossings[d][c][a][b] = (-value)
    crossings[c][d][b][a] = (-value)
    crossings[d][c][b][a] = value

    return crossings

## TESTING PURPOSES ONLY:
if __name__ == "__main__":
    graph = input()
    filepath = "/" + graph + ".txt"
    links, knots = Gordian(filepath)
    print(f" There are {len(links)} links:")
    for link in links:
        print(link)

    print(f" There are {len(knots)} knots:")
    for knot in knots:
        print(knot)

