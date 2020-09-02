# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:31:06 2020

@author: Lorenzo
"""

"""
One shot gamble:
a) status quo (100$)
b) +50% with probability .5, -40% with probaiblity .5
EV: positive. Let us see what happens if 100k people accept b).
"""

import numpy as np
# import pandas as pd
from matplotlib import pyplot as plt
from pylab import rcParams
# from collections import Counter

# storage vector for 20 trajectories
trajectories = np.zeros((100000,101))

# setting random seed
np.random.seed(6)

# stating wealth 100$ to feed the loop
w = 100

# loops that create the 20 trajectories
for i in range(0,100000):
    # stating wealth 100\$, to feed the loop a starting value
    w = 100
    for element in range(1,101):
        if np.random.randint(0, 2, 1) == 1:
            w = w*1.5
            trajectories[i, element] = w
        else:
            w = w*0.6
            trajectories[i, element] = w
        
# 100$ at time t
trajectories[:,0] = 100

# defining EU_factor
EU_factor = 1.05

# defining trajectory EU
trajectory_EU = list(100*(EU_factor)**(t) for t in range(0, 101))

# plotting the trajectories
plt.xlabel('time', fontdict=None, labelpad=None)
plt.ylabel('wealth', fontdict=None, labelpad=None)
plt.yscale('log') 
plt.grid()            
rcParams['figure.figsize'] = 15, 10
for i in range(0,500):
    plt.plot(trajectories[i,:], color='black')
plt.plot(trajectory_EU, color='red')

# saving the image
plt.savefig('thesis - the illusion of EV.png')

# counting the percentage of people who end up with wealth <=1, between 1 and 50,
# between 50 and 100, between 100 and 300, larger than 300 at time 100
perc_less_1 = 0
perc_1_50 = 0
perc_50_100 = 0
perc_100_300 = 0
perc_300_12k = 0
perc_larger_EV = 0

# for loop to divide the observations at time 100 into these 5 categories
for i in range(0,100000):
    if trajectories[i,99] <= 1:
        perc_less_1 = perc_less_1 + 1
    elif 1 < trajectories[i,99] <= 50:
        perc_1_50 = perc_1_50 + 1
    elif 50 < trajectories[i,99] <= 100:
        perc_50_100 = perc_50_100 + 1
    elif 100 < trajectories[i,99] <= 300:
        perc_100_300 = perc_100_300 + 1
    elif 300 < trajectories[i,99] <= 12523:
        perc_300_12k = perc_300_12k + 1
    else:
        perc_larger_EV = perc_larger_EV + 1

perc_less_1 = perc_less_1 / 100000
perc_1_50 = perc_1_50 / 100000
perc_50_100 = perc_50_100 / 100000
perc_100_300 = perc_100_300 / 100000
perc_300_12k = perc_300_12k / 100000
perc_larger_EV = perc_larger_EV / 100000

median = np.median(trajectories[:,100])

