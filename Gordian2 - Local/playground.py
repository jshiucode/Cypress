# from helpers import listify_cycles

# cycle1 = {'5': ['4', '6'], '0': ['4', '6'], '6': ['0', '5'], '4': ['0', '5']}
# list_cycle_1 = listify_cycles(list(cycle1.keys())[0], cycle1, [])
# cycle2 = {'5': ['6', '4'], '0': ['6', '4'], '6': ['0', '5'], '4': ['0', '5']}
# list_cycle_2 = listify_cycles(list(cycle2.keys())[0], cycle2, [])

# from helpers import orient_cycle_at_smallest

# print(orient_cycle_at_smallest(list_cycle_1))
# print(orient_cycle_at_smallest(list_cycle_2))



one = {'5': ['4', '6'], '0': ['4', '6'], '6': ['0', '5'], '4': ['0', '5']}
two = {'5': ['6', '4'], '0': ['6', '4'], '6': ['0', '5'], '4': ['0', '5']}
both = [one, two]
for dic in both:
    for vertex in dic.keys():
        dic[vertex].sort()

print(one == two)
