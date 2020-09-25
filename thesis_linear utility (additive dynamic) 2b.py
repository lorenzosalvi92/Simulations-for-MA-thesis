# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:52:30 2019

@author: Lorenzo
"""

'''
The decision-setting:

a) get 1\$ with probability 1
b) get +50\$ with probability 0.5 and -40\$ with probability 0.5
    
Assume utility function of the following form: u(x) = x (utility equals wealth)
'''

import numpy as np
# import pandas as pd
from matplotlib import pyplot as plt
# from pylab import rcParams
# from collections import Counter
import matplotlib.pylab as pylab

# storage matrix for 20 trajectories
trajectories = np.zeros((20,10001))

# setting random seed
np.random.seed(6)

# loop that creates the trajectory
for i in range(0,20):
    w = 100
    for element in range(1,10001):
        if 1 > (0.5*(50) + 0.5*(-40)):
            w = w + 1
            trajectories[i, element] = w
        else:
            if np.random.randint(0, 2, 1) == 1:
                w = w + 50
                trajectories[i, element] = w
            else:
                w = w - 40
                trajectories[i, element] = w

# 100$ at time t
trajectories[:,0] = 100

# defining EU_constant
EU_constant = 5

# defining trajectory EU
trajectory_EU = list(100+(EU_constant)*(t) for t in range(0, 10001))

# plotting the trajectories + EU trajectory
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.xlabel('time', fontdict=None, labelpad=None)
plt.ylabel('linear utility/wealth', fontdict=None, labelpad=None)   
plt.grid()            
for i in range(0,20):
    plt.plot(trajectories[i,:])
plt.plot(trajectory_EU, color='red')

# saving the image
plt.savefig('thesis - linear utility 2b.pdf')