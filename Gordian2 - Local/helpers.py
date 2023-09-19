"""
Turns dictionary formatted cycle into oriented list formatted cycle
"""
def listify_cycles(loc, cycle, graveyard):
    graveyard.append(loc)
    for next in cycle[loc]:
        if next in graveyard:
            continue
        elif next not in graveyard:
            return listify_cycles(next, cycle, graveyard)
    return graveyard + [graveyard[0]]



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
Outputs list of all binary strings (list form) of length n
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