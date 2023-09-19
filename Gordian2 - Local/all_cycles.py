from helpers import bin_strings

"""
Finds cycles between all linear combinations of fundamental set of cycles
"""
def find_all_cycles(fundamental_cycles):

    """
    Fundamental cycle-cycle-cycle... (dictionary format) combining function to find new cycle
    """
    def find_combined(cycles):
        def two_cycles(cycle1, cycle2):
            new_cycle = {}
            for v in list(cycle2.keys()) + list(cycle1.keys()):
                if v not in cycle1.keys() and v in cycle2.keys():
                    new_cycle[v] = cycle2[v]
                elif v not in cycle2.keys() and v in cycle1.keys():
                    new_cycle[v] = cycle1[v]
                else:
                    new_cycle[v] = list(set(cycle1[v]).union(set(cycle2[v])))
                    for overlap in list(set(cycle1[v]).intersection(set(cycle2[v]))):
                        new_cycle[v].remove(overlap)
                        if new_cycle[v] == []: #remove vertices attached to nothing
                            del new_cycle[v]
            return new_cycle


        root_cycle = cycles[0]
        for cycle_dic in cycles[1:]:
            root_cycle = two_cycles(root_cycle, cycle_dic)
        return root_cycle

    all_cycles = fundamental_cycles
    binary_strings = bin_strings(len(fundamental_cycles))
    for string in binary_strings:
        cycles = []
        for i, val in enumerate(string):
            if val == 1:
                cycles.append(fundamental_cycles[i])

        new_cycle = find_combined(cycles)

        #checking new cycle
        append = True
        for v in new_cycle.keys():
            if len(new_cycle[v]) > 2 or multi_cycle(list(new_cycle.keys())[0], new_cycle.copy(), []) or new_cycle in all_cycles:
                append = False
                break
        
        if append:
            all_cycles.append(new_cycle)

    return all_cycles


"""
Detects if cycle (dictionary format) is actually multiple disjoint cycles
False: single cycle
True: multiple cycles
"""
def multi_cycle(loc, cycle, graveyard):
    graveyard.append(loc)
    for next in cycle[loc]:
        if next in graveyard:
            continue
        elif next not in graveyard:
            return multi_cycle(next, cycle, graveyard)
    for v in graveyard:
        del cycle[v]
    if len(cycle) != 0:
        return True
    else:
        return False


