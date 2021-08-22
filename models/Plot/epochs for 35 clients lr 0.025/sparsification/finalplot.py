# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 20:31:00 2021

@author: ishan
"""

import matplotlib.pyplot as plt
epochs=[0.05, 0.1, 0.15, 0.2]
rounds=[101, 101, 111, 113]
plt.plot(epochs, rounds, linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)

# setting x and y axis range
plt.ylim(90, 150)
plt.xlim(0.04, 0.21)
  
# naming the x axis
plt.xlabel('epochs')
# naming the y axis
plt.ylabel('rounds')
  
# giving a title to my graph
plt.title('epochs vs rounds (clients-35 lr-0.05)')