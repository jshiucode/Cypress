one = ['5', '6', '7', '0', '1', '2', '3', '4', '5']
two = ['0', '1', '2', '3', '4', '5', '0']
three = ['5', '6', '7', '1', '2', '3', '4', '5']
four = ['7', '8', '9', '6', '7']

def orient_cycle_start_zero(cycle):
    cycle = [int(node) for node in cycle]
    smallest = min(cycle)
    hold_cycle = []
    end_cycle = []
    print(smallest)
    for i, node in enumerate(cycle):
        if i == 0 and node == smallest:
            return cycle
        if node == smallest:
            end_cycle.extend(cycle[i:])
            break
        else:
            hold_cycle.append(node)
    
    end_cycle.extend(hold_cycle[1:])
    end_cycle.append(smallest)
    return end_cycle

print(orient_cycle_start_zero(three))