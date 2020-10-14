# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:52:30 2019

@author: Lorenzo
"""
#################################################

import numpy as np
# import pandas as pd
from matplotlib import pyplot as plt
# from pylab import rcParams
# from collections import Counter
import matplotlib.pylab as pylab

#################################################

# storage matrix
trajectory = np.zeros((1,10001))

# setting random seed
np.random.seed(6)

# setting initial value for the loop
w = 100

# loop that creates the trajectory
for element in range(1,10001):
    if np.log2(w + 1) > (0.5*np.log2(w+50) + 0.5*np.log2(w-40)):
        w = w + 1
        trajectory[:, element] = w
    else:
        if np.random.randint(0, 2, 1) == 1:
            w = w + 50
            trajectory[:, element] = w
        else:
            w = w - 40
            trajectory[:, element] = w
        
# 100$ at time t
trajectory[0,0] = 100

# calculate logarithmic utility/log-wealth
trajectory = np.log(trajectory)

# plotting the trajectory
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.xlabel('time', fontdict=None, labelpad=None)
plt.ylabel('utility/logarithm of wealth', fontdict=None, labelpad=None)   
plt.grid()              
plt.plot(trajectory[0,:])

#################################################

