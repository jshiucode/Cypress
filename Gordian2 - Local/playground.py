from graph_creator import Crossing


# crossing = Crossing(a, b, c, d, False, order_a, order_b, sign)
a = Crossing(1,2,1,2,True,1,2,1)
b = Crossing(2,1,1,2,True,1,2,1)

print(a.representation() == b.representation())