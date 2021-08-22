# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 20:31:00 2021

@author: ishan
"""

import matplotlib.pyplot as plt
epochs=[5,6,7,8,9,10,11,12,15]
rounds=[68,68,68,68,67,67,68,69,80]
plt.plot(epochs, rounds, linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)

# setting x and y axis range
plt.ylim(65,88)
plt.xlim(3,17)
  
# naming the x axis
plt.xlabel('epochs')
# naming the y axis
plt.ylabel('rounds')
  
# giving a title to my graph
plt.title('epochs vs rounds (clients-35 lr-0.05)')