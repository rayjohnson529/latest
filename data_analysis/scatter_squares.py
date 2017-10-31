# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 22:24:17 2017

@author: Ray
"""

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 12, 25]
import matplotlib.pyplot as plt

plt.scatter(x_values, y_values, s = 100)

# Set chart title and label axes

plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

plt.tick_params(axis='both', which='major', labelsize = 14)
plt.show()

