import numpy as np

x=10
crossings = np.zeros((x,x,x,x))

def edit(crossings):
    crossings[1][1][1][1] = 1
    return crossings

crossings[2][2][2][2] = -crossings[2][2][2][2]
crossings = edit(crossings)
print(crossings[2][2][2][2])
print(crossings[1][1][1][1])