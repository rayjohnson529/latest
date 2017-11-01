# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 20:42:31 2017

@author: Ray
"""

import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x ** 3 for x in x_values]

plt.title("Values and Values Cubed Scatterplot.\n", fontsize = 24)
plt.ylabel("Values Cubed", fontsize = 14)
plt.xlabel("Values", fontsize = 14)

plt.axis([1, 5001, 8, 50000000000])

plt.scatter(x_values, y_values)




# remove the outlines from data points
plt.scatter(x_values, y_values, edgecolor='none', s=40)

plt.scatter(x_values, y_values, c = (0.4, .7, 0.8), edgecolor='none', s=40)

plt.savefig('cubes_plot.png', bbox_inches='tight')

# You have to make the y axis 50,000,000 for the plot to show up