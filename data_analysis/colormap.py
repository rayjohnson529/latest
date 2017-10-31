# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 22:43:54 2017

@author: Ray
"""

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

plt.title("Squared list of a Range between 1 and 1000.\n", fontsize = 18)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

plt.scatter(x_values, y_values)

plt.axis([0, 1100, 0, 1100000])

# remove the outlines from data points
plt.scatter(x_values, y_values, edgecolor='none', s=40)

plt.scatter(x_values, y_values, c = y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

plt.savefig('squares_plot.png', bbox_inches='tight')