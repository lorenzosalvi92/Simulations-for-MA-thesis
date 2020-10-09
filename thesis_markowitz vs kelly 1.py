# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:44:59 2020

@author: Lorenzo
"""


import numpy as np
# import pandas as pd
from matplotlib import pyplot as plt
# from pylab import rcParams
# from collections import Counter
import matplotlib.pylab as pylab

#################################################

return_riskfree = 0.01
expectedreturn_risky = 0.05

returns_matrix = np.array([expectedreturn_risky,return_riskfree])

fractions_matrix = np.array([[0,1],[0.1,0.9],[0.2,0.8],[0.3,0.7],
                          [0.4,0.6],[0.5,0.5],[0.6,0.4],[0.7,0.3]
                          ,[0.8,0.2],[0.9,0.1],[1,0]])
# notice that the second root is at approximately f = -0.175

ev_portfolio = fractions_matrix.dot(returns_matrix)

std_riskfree = 0
std_risky = (0.5*(0.5**2) + 0.5*(0.4**2) - 0.05**2)**(1/2)
var_risky = (0.5*(0.5**2) + 0.5*(0.4**2) - 0.05**2)

std_portfolio = np.array(np.zeros(11))

for i in range(0,11):
    std_portfolio[i,]=((fractions_matrix[i,0]**2)*(var_risky))**(1/2)

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
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.gca().yaxis.grid(True)
plt.xlabel("STD")
plt.ylabel("EV")
plt.gcf().subplots_adjust(bottom=0.25)

# plotting the function
x = np.linspace(0,0.6)
ax.plot(x,0.01 + (0.05-0.01)/0.45*x,color='black',label='Efficient frontier')
plt.scatter(std_portfolio,ev_portfolio, s = 80, color = 'blue', label = '0<f<1') 
#plt.scatter(0.5,0.0544, s = 80, color = 'green', label = 'w_1>1 and w_1<0') 
#plt.scatter(-0.1,0.0133, s = 80, color = 'green') 
plt.scatter(0, 0.01, marker='o', s=80, color="red", label = 'f=0 and f=1')   
plt.scatter(0.45, 0.05, marker='o', s=80, color="red")  
plt.scatter(0.2, 0.01, marker='o', s=80, color="grey", label='Inefficient portfolios')
plt.scatter(0.4,0.03, marker ='o', s=80, color="grey")
plt.legend(loc="upper left")


# saving the image
plt.savefig('thesis - markowitz vs kelly 1.pdf')


