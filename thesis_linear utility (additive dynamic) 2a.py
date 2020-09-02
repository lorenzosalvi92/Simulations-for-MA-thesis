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
from matplotlib import pyplot as plt
from pylab import rcParams

# storage matrix
trajectory = np.zeros((1,10001))

# setting random seed
np.random.seed(6)

# setting initial value for the loop
w = 100

# loop that creates the trajectory
for element in range(1,10001):
    if np.random.randint(0, 2, 1) == 1:
        w = w + 50
        trajectory[:, element] = w
    else:
        w = w - 40
        trajectory[:, element] = w
        
# 100$ at time t
trajectory[0,0] = 100

# defining EU_constant
EU_constant = 5

# defining trajectory EU
trajectory_EU = list(100+(EU_constant)*(t) for t in range(0, 10001))

# plotting the trajectory
plt.xlabel('time', fontdict=None, labelpad=None)
plt.ylabel('linear utility/wealth', fontdict=None, labelpad=None)   
plt.grid()              
rcParams['figure.figsize'] = 15, 10
plt.plot(trajectory[0,:])
plt.plot(trajectory_EU, color='red')

# saving the image
plt.savefig('thesis - linear utility 2a.png')