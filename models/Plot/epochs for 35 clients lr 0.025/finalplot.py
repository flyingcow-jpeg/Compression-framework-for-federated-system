# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 20:31:00 2021

@author: ishan
"""

import matplotlib.pyplot as plt
epochs=[5,6, 7, 9 ,11]
rounds=[125, 101, 111, 112, 113]
plt.plot(epochs, rounds, linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)

# setting x and y axis range
plt.ylim(90, 150)
plt.xlim(4, 12)
  
# naming the x axis
plt.xlabel('epochs')
# naming the y axis
plt.ylabel('rounds')
  
# giving a title to my graph
plt.title('epochs vs rounds (clients-35 lr-0.025)')