# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 22:15:31 2017

@author: Ray
"""

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth=5)

# Set chart title and label axes.

plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# Set the size of the tick labels.
plt.tick_params(axis = 'both', labelsize = 14)

plt.show()