# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 18:51:48 2019

@author: Lorenzo
"""

'''                                                                
Allocate a share of your money into two options:
a) bond earning risk-free return 0.01
b) stock with 50/50 chance of gain or loss, with gain of 50% and loss of 40%.
'''

import numpy as np
# import pandas as pd
from matplotlib import pyplot as plt
# from pylab import rcParams
from collections import Counter
import matplotlib.pylab as pylab

# creating array with 5 different percentages of wealth to bet (the third is the optimal share)
bet_size = np.asarray([0.05, 0.1, 0.20, 0.50, 0.65])
s = bet_size.size

# setting random seed
np.random.seed(5)

# coin flips: if 1, +50\% of wager; if 0, -40\% of wager
coinflips = np.random.randint(0, 2, 10001)
# counting the coinflips
counter = Counter(coinflips)

# creating storage matrix for six trajectories over 10000 time steps
data = np.zeros((5,10001))

# creating the trajectories
for j in range(0,5):
    print(bet_size[j,])
    X_0 = 100
    # starting capital
    r = 0.01
    # risk-free return
    for i in range(1,10001):
       if coinflips[i,] == 1: X_0 = X_0*(1+(bet_size[j,]*0.5)+(1-bet_size[j,])*r)
       else: X_0 = X_0*(1-(bet_size[j,]*0.4) +(1-bet_size[j,])*r)
       #print(w)
       data[j,i] = X_0

# 100 $ as a starting value for all the trajectories
data[:,0] = 100

# plotting the trajectories
# the optimal share trajectory is the magenta, dashed line
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.gca().yaxis.grid(True)
plt.xlabel("t")
plt.ylabel("wealth")
plt.yscale("log")
plt.plot((data[0,]), color='green', label="f = 0.05")
plt.plot((data[1,]), color='red', label="f = 0.1")
plt.plot((data[2,]), color='magenta', linestyle='dashed', label="f = 0.2")
plt.plot((data[3,]), color='blue', label="f = 0.5")
plt.plot((data[4,]), color='yellow', label="f = 0.65")
plt.legend(loc="upper left")

# saving the first image
plt.savefig('thesis - kelly criterion 2.pdf')
