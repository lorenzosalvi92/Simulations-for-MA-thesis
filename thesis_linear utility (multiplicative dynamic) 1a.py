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

# storage vector for 20 trajectories
trajectory = np.zeros((1,10001))

# setting random seed
np.random.seed(6)

# stating wealth 100$
w = 100
        
# loop that creates the trajectory
for element in range(1,10001):
    if (w*1.01) - w > (0.5*(w*1.5) + 0.5*(w*0.6)) - w:
        w = w*1.01
        trajectory[:, element] = w
    else:
        if np.random.randint(0, 2, 1) == 1:
            w = w*1.5
            trajectory[:, element] = w
        else:
            w = w*0.6
            trajectory[:, element] = w
        
# 100$ at time t
trajectory[0,0] = 100

# defining expected utility factor
EU_factor = 1.05

# defining trajectory EU
trajectory_EU = list(100*(EU_factor)**(t) for t in range(0, 10001))

# plotting the trajectory
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.xlabel('time', fontdict=None, labelpad=None)
plt.ylabel('utility/wealth', fontdict=None, labelpad=None)   
plt.yscale('log')  
plt.grid()            
plt.plot(trajectory[0,:])
plt.plot(trajectory_EU, color='red')

# saving the image
plt.savefig('thesis - linear utility 1a.pdf')

#################################################

