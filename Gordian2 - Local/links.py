from helpers import listify_cycles

"""
Finds all the pairs of cycles that are linked
"""
def find_links(all_cycles, crossings):
    cycles = []
    for cycle in all_cycles:
        cycles.append(listify_cycles(list(cycle.keys())[0], cycle, []))
    linked_cycles = []
    #Compare all cycles with all other cycles (dont need to repeat pairs)
    for cycleA in cycles:
        for cycleB in cycles[cycles.index(cycleA) + 1:]:
            if set(cycleA).intersection(set(cycleB)) != set():
                continue
            link_num = 0
            #compare edges
            for a in range(len(cycleA)-1):
                for b in range(len(cycleB)-1):
                    link_num += crossings[int(cycleA[a])][int(cycleA[a+1])][int(cycleB[b])][int(cycleB[b+1])]
            link_num = link_num/2
            if link_num != 0:
                linked_cycles.append((cycleA, cycleB, link_num))
            elif link_num >= 4: #potential crossings
                linked_cycles.append((cycleA, cycleB, link_num, "POTENTIAL"))

    return linked_cycles




