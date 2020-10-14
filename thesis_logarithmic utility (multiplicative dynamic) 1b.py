# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:31:06 2020

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

# storage vector for the outcomes of choosing b (20 trajectories)
trajectories = np.zeros((20,10001))

# setting random seed
np.random.seed(6)

# stating wealth 100$ to feed the loop
w = 100

# loop that creates the 20 trajectories
for i in range(0,20):
    w = 100
    for element in range(1,10001):
        if np.random.randint(0, 2, 1) == 1:
            w = w*1.5
            trajectories[i, element] = w
        else:
            w = w*0.6
            trajectories[i, element] = w
        
# 100$ at time t
trajectories[:,0] = 100

# calculating logarithmic utility/log-wealth
trajectories = np.log(trajectories)

# define expected utility term
EU_term = np.log(0.95)

# define trajectory EU
trajectory_EU = list(np.log(100) +(EU_term)*(t) for t in range(0, 10001))

# plotting the trajectories
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
for i in range(1, 20):
    plt.plot(trajectories[i,:])
plt.plot(trajectory_EU, color='red')

# saving the image
plt.savefig('thesis - logarithmic utility 1b.pdf')

#################################################
