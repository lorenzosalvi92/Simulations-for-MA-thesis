# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:34:29 2020

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

# define desplayed domain
f = np.linspace(0,0.6)

# the function
p = 100 * (1 + (f*0.5)) * (1-(f*0.4)) - 100
e = 100 * (f*0.5) - 100 *(f*0.4)
l = e - p

# parameter-settings + plot
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.gca().yaxis.grid(True)
plt.xlabel("f")
plt.ylabel("W-L / Profit / (W-L) - Profit")
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(f,p,'b', label = "Profit")
plt.plot(f,e,'r', label = "W-L")
plt.plot(f,l,'g', label = "(W-L) - Profit")
plt.axvline(x=0.25, linestyle='dashed')
plt.legend(loc="upper left")

# saving the figure
plt.savefig('thesis - kelly criterion 1.pdf')

#################################################

