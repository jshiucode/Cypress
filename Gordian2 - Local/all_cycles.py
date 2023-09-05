"""
Converts all cycles in fundamental set of cycles from list form to dictionary form
"""
def dictify_cycles(fundamental_set):
    cycles_dictified = []
    for cycle in fundamental_set:
        dic_cycle = {}
        if cycle[0] != cycle[len(cycle)-1]:
            print("Invalid Cycle:", cycle)
            continue
        for i in range(len(cycle)-1):
            if cycle[i] not in dic_cycle.keys():
                dic_cycle[cycle[i]] = [str(cycle[i+1])]
            elif cycle[i] in dic_cycle.keys():
                dic_cycle[cycle[i]].append(str(cycle[i+1]))
            if cycle[i+1] not in dic_cycle.keys():
                dic_cycle[cycle[i+1]] = [str(cycle[i])]
            elif cycle[i+1] in dic_cycle.keys():
                dic_cycle[cycle[i+1]].append(str(cycle[i]))
        cycles_dictified.append(dic_cycle)

    return cycles_dictified

"""
Outputs list of of all binary strings (list form) of length n
"""
def bin_strings(n):
    def genbin(n, bin_strings, bs = []):
        if len(bs) == n:
            bin_strings.append(bs)
        else:
            genbin(n, bin_strings, bs + [0])
            genbin(n, bin_strings, bs + [1])

    bin_strings = []
    genbin(n, bin_strings, bs = [])
    bin_strings.remove([0] * n)
    return bin_strings

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


