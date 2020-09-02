# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:31:06 2020

@author: Lorenzo
"""

"""
The decision-setting:
    
a) get 1% of your wealth with probability 1
b) +50% with probability .5, -40% with probaiblity .5
    
Assume utility function of the following form: u(x) = x (utility equals wealth)
"""

import numpy as np
# import pandas as pd
from matplotlib import pyplot as plt
from pylab import rcParams
# from collections import Counter

# storage vector for 20 trajectories
trajectory = np.zeros((1,10001))

# setting random seed
np.random.seed(6)

# stating wealth 100$
w = 100

# loop that generate the trajectory
for element in range(1,10001):
    if np.random.randint(0, 2, 1) == 1:
        w = w*1.5
        trajectory[:, element] = w
    else:
        w = w*0.6
        trajectory[:, element] = w
        
# 100$ at time t
trajectory[0,0] = 100

# defining EU_factor
EU_factor = 1.05

# defining trajectory EU
trajectory_EU = list(100*(EU_factor)**(t) for t in range(0, 10001))

# plotting the trajectory
plt.xlabel('time', fontdict=None, labelpad=None)
plt.ylabel('utility/wealth', fontdict=None, labelpad=None)   
plt.yscale('log')  
plt.grid()            
rcParams['figure.figsize'] = 15, 10
plt.plot(trajectory[0,:])
plt.plot(trajectory_EU, color='red')

# saving the image
plt.savefig('thesis - linear utility 1a.png')

