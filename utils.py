import numpy as np


# the function to calculate the fitness value of a,b as input of power fucntion based on the weights of CFG
# and also calculate the mutant score and mutant mask
def CFgraph(a, b):
    # f is fitness value and s is the number of found mutant(s) and mask is for index of found mutant(s)
    f = 0
    s = 0
    mask = np.zeros(3)
    # begin of test algorithm
    # p is the results of the a^b
    p = 1
    f += 20
    if b <= 0:
        f += 8
        s += 1
        mask[0] += 1
        return f, s, p, mask

    else:
        f += 2

    for i in range(1, b):
        p += a
        f += 8

    if b <= 1:
        f += 12
        s += 1
        mask[1] += 1

    else:
        f += 18
        s += 2
        mask[1] += 1
        mask[2] += 1

    return f, s, p, mask