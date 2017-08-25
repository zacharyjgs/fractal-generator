"""
This program allows one to generate a cool fractal
image and explore the properties of matrix transformations
and randomess.
"""

#import various packages
import matplotlib.pyplot as plt
import numpy as np
import random

#initializes the seed vector
v = np.array([[1],[0]])

#randomly chooses from a list of transposes to find new vector
def findNew(seed):
    tlist = [np.array([[0.],[0.]]),np.array([[0.5],[0.]]),np.array([[0.],[0.5]])]
    new = 0.5*seed + random.choice(tlist)
    return new

#repeats the random transposes to create the fractal
def makeFractal(seed, pcount):
    plist = [seed]
    new = seed
    for p in range(1,pcount):
        new = findNew(new)
        plist.append(new)
    return np.array(plist)

#repeats the transpose one million times
plist = makeFractal(v, 1000000)
plt.plot(plist[:,0,0], plist[:,1,0], 'o', markersize=0.2)
plt.show()
