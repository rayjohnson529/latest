# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 21:05:34 2017

@author: Ray
"""

import matplotlib.pyplot as plt
from randomwalk import RandomWalk

# make a random walk and plot the points.

rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s = 15)
plt.show()

plt.savefig('randomwalk6.png', bbox_inches='tight')