from knots import orient_crossings
from graph_creator import get_crossings_for_knots


crossing_data_for_knots = get_crossings_for_knots("../Tests/testing-orient_crossings/input.txt")
edges = [[8,7], [9,10], [5,6], [4,3], [1,2]]
output = orient_crossings(crossing_data_for_knots, edges)
for c in output: print(c)
