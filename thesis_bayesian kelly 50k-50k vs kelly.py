# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 18:51:48 2019

@author: Lorenzo
"""

#######################################################

import numpy as np
import random
from matplotlib import pyplot as plt
#from pylab import rcParams
from collections import Counter
from scipy.interpolate import interp1d
np.seterr(divide = 'ignore') 
# import pandas as pd
# from pylab import rcParams
# from collections import Counter
import matplotlib.pylab as pylab

#######################################################

# setting parameters
# number of trials
n = 10000
# probability of success
p = 0.5
# probability of failure
q = 0.5
# expected value
m = 5000
# standard deviation
sd = round(np.sqrt(n*p*q))
# fixed number of successes (expected value +/- a certain number of standard deviations)
successes = np.asarray([m-5*sd, round(m-4.5*sd), m-4*sd, round(m-3.5*sd), m-3*sd, round(m-2.5*sd), m-2*sd, round(m-1.5*sd), m-1*sd, round(m-0.5*sd), m, round(m+0.5*sd), m+1*sd, round(m+1.5*sd), m+2*sd, round(m+2.5*sd), m+3*sd, round(m+3.5*sd), m+4*sd, round(m+4.5*sd), m+5*sd])
coinflips = np.zeros((21,10000))

# create matrix with different streaks of successes and failures
for j in range(0,21):
        ones = np.ones((1,int(successes[j,])))
        zeros = np.zeros((1,int(n - successes[j,])))
        x = np.concatenate((ones, zeros), axis = 1)
        coinflips[j,:] = x
        random.shuffle(coinflips[j,:])

# test: check that number of 1s and 0s is plausible (replace '0' with other columns' numbers to check them)
counter = Counter(coinflips[0,:])

# define interest rate
r = 0.01

# define "prior" Kelly fractions 
fraction_1 = (50000/(50000+50000))*(1+r)*1/(0.4+r) - (1-(50000/(50000+50000)))*(1+r)*1/(0.5-r)
fraction_2 = (50480/(50480+49520))*(1+r)*1/(0.4+r) - (1-(50480/(50480+49520)))*(1+r)*1/(0.5-r)
fraction_3 = (49520/(50480+49520))*(1+r)*1/(0.4+r) - (1-(49520/(50480+49520)))*(1+r)*1/(0.5-r)

#####################################################

data_bayesian_kelly50k50k = np.zeros((21,10000))

for y in range(0,21):
    # starting capital
    X_bayesian_kelly50k50k = 100
    # starting optimal fraction 
    f_bayesian_kelly50k50k = 0.20
    # probability of winning (Beta distribution with parameters 4,4)
    a = 50000
    b = 50000
    sum_a_b = a + b
    p = a / sum_a_b
    for i in range(0,10000):
       if coinflips[y,i] == 1: 
           X_bayesian_kelly50k50k = X_bayesian_kelly50k50k*(1+f_bayesian_kelly50k50k*0.5+(1-f_bayesian_kelly50k50k)*r)
           a = a + 1
           sum_a_b = sum_a_b + 1
           f_bayesian_kelly50k50k = (a/sum_a_b)*(1+r)*1/(0.4+r) - (1-a/sum_a_b)*(1+r)*1/(0.5-r)
       else: 
           X_bayesian_kelly50k50k = X_bayesian_kelly50k50k*(1-f_bayesian_kelly50k50k*0.4+(1-f_bayesian_kelly50k50k)*r)
           sum_a_b = sum_a_b + 1
           f_bayesian_kelly50k50k = (a/sum_a_b)*(1+r)*1/(0.4+r) - (1-a/sum_a_b)*(1+r)*1/(0.5-r)
       data_bayesian_kelly50k50k[y,i] =  X_bayesian_kelly50k50k

starting_value_bayesian_kelly50k50k = 100*np.ones((21,1))
data_bayesian_kelly50k50k = np.append(starting_value_bayesian_kelly50k50k, data_bayesian_kelly50k50k, axis = 1)
terminal_values_bayesian_kelly50k50k = np.log(data_bayesian_kelly50k50k[:,10000])

#####################################################

data_1xkelly = np.zeros((21,10000))

for y in range(0,21):
    # starting capital
    X_1xkelly = 100
    # starting optimal fraction 
    f_1xkelly = 0.2
    for i in range(0,10000):
       if coinflips[y,i] == 1: 
           X_1xkelly = X_1xkelly*(1+f_1xkelly*0.5+(1-f_1xkelly)*r)
       else: 
           X_1xkelly = X_1xkelly*(1-f_1xkelly*0.4 +(1-f_1xkelly)*r)
       data_1xkelly[y,i] = X_1xkelly
   
starting_value_1xkelly = 100*np.ones((21,1))
data_1xkelly = np.append(starting_value_1xkelly, data_1xkelly, axis = 1)
terminal_values_1xkelly = np.log(data_1xkelly[:,10000])

#####################################################

# interpolating the values between the chosen points
int_1 = interp1d(successes, terminal_values_bayesian_kelly50k50k)
int_2 = interp1d(successes, terminal_values_1xkelly)

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.ylabel('logarithm of terminal wealth', fontdict=None, labelpad=None)
plt.xlabel('number of successes', fontdict=None, labelpad=None)   
plt.grid()          
plt.plot(successes,int_1(successes), '-', color = 'red', label = 'Bayesian Kelly 50k,50k')
plt.plot(successes,int_2(successes), '-', color = 'blue', label = 'Pure Kelly, p = .5')
plt.legend(loc="upper left")

# saving the image
plt.savefig('thesis - bayesian kelly 50k-50k vs kelly.pdf')

plt.show()

#####################################################

data_bayesian_kelly_over = np.zeros((21,10000))

for y in range(0,21):
    # starting capital
    X_bayesian_kelly_over = 100
    # starting optimal fraction 
    f_bayesian_kelly_over = 0.22
    # probability of winning (Beta distribution with parameters 3,1)
    a = 50480
    b = 49520
    sum_a_b = a + b
    p = a / sum_a_b
    for i in range(0,10000):
       if coinflips[y,i] == 1: 
           X_bayesian_kelly_over = X_bayesian_kelly_over*(1+f_bayesian_kelly_over*0.5+(1-f_bayesian_kelly_over)*r)
           a = a + 1
           sum_a_b = sum_a_b + 1
           f_bayesian_kelly_over = (a/sum_a_b)*(1+r)*1/(0.4+r) - (1-a/sum_a_b)*(1+r)*1/(0.5-r)
       else: 
           X_bayesian_kelly_over = X_bayesian_kelly_over*(1-f_bayesian_kelly_over*0.4+(1-f_bayesian_kelly_over)*r)
           sum_a_b = sum_a_b + 1
           f_bayesian_kelly_over = (a/sum_a_b)*(1+r)*1/(0.4+r) - (1-a/sum_a_b)*(1+r)*1/(0.5-r)
       data_bayesian_kelly_over[y,i] =  X_bayesian_kelly_over

starting_value_bayesian_kelly_over = 100*np.ones((21,1))
data_bayesian_kelly_over = np.append(starting_value_bayesian_kelly_over, data_bayesian_kelly_over, axis = 1)
terminal_values_bayesian_kelly_over = np.log(data_bayesian_kelly_over[:,10000])

#####################################################

data_1xkelly_wo = np.zeros((21,10000))

for y in range(0,21):
    # starting capital
    X_1xkelly_wo = 100
    # starting optimal fraction 
    f_1xkelly_wo = 0.22
    for i in range(0,10000):
       if coinflips[y,i] == 1: 
           X_1xkelly_wo = X_1xkelly_wo*(1+f_1xkelly_wo*0.5+(1-f_1xkelly_wo)*r)
       else: 
           X_1xkelly_wo = X_1xkelly_wo*(1-f_1xkelly_wo*0.4 +(1-f_1xkelly_wo)*r)
       data_1xkelly_wo[y,i] = X_1xkelly_wo
   
starting_value_1xkelly_wo = 100*np.ones((21,1))
data_1xkelly_wo = np.append(starting_value_1xkelly_wo, data_1xkelly_wo, axis = 1)
terminal_values_1xkelly_wo = np.log(data_1xkelly_wo[:,10000])

#####################################################

# interpolating the values between the chosen points
int_3 = interp1d(successes, terminal_values_bayesian_kelly_over)
int_4 = interp1d(successes, terminal_values_1xkelly_wo)

plt.ylabel('logarithm of terminal wealth', fontdict=None, labelpad=None)
plt.xlabel('number of successes', fontdict=None, labelpad=None)   
plt.grid()    
plt.plot(successes,int_3(successes), '-', color = 'black', label = 'Bayesian Kelly 50480,49520')
plt.plot(successes,int_4(successes), '-', color = 'cyan', label = 'Pure Kelly, p = 50480/100k')
plt.legend(loc="upper left")

# saving the image
plt.savefig('thesis - bayesian kelly 50k-50k vs kelly (1).pdf')

plt.show()

#####################################################

data_bayesian_kelly_under = np.zeros((21,10000))

for y in range(0,21):
    # starting capital
    X_bayesian_kelly_under = 100
    # starting optimal fraction 
    f_bayesian_kelly_under = 0.18
    # probability of winning (Beta distribution with parameters 3,1)
    a = 49520
    b = 50480
    sum_a_b = a + b
    p = a / sum_a_b
    for i in range(0,10000):
       if coinflips[y,i] == 1: 
           X_bayesian_kelly_under = X_bayesian_kelly_under*(1+f_bayesian_kelly_under*0.5+(1-f_bayesian_kelly_under)*r)
           a = a + 1
           sum_a_b = sum_a_b + 1
           f_bayesian_kelly_under = (a/sum_a_b)*(1+r)*1/(0.4+r) - (1-a/sum_a_b)*(1+r)*1/(0.5-r)
       else: 
           X_bayesian_kelly_under = X_bayesian_kelly_under*(1-f_bayesian_kelly_under*0.4+(1-f_bayesian_kelly_under)*r)
           sum_a_b = sum_a_b + 1
           f_bayesian_kelly_under = (a/sum_a_b)*(1+r)*1/(0.4+r) - (1-a/sum_a_b)*(1+r)*1/(0.5-r)
       data_bayesian_kelly_under[y,i] =  X_bayesian_kelly_under

starting_value_bayesian_kelly_under = 100*np.ones((21,1))
data_bayesian_kelly_under = np.append(starting_value_bayesian_kelly_under, data_bayesian_kelly_under, axis = 1)
terminal_values_bayesian_kelly_under = np.log(data_bayesian_kelly_under[:,10000])

#####################################################

data_1xkelly_wo1 = np.zeros((21,10000))

for y in range(0,21):
    # starting capital
    X_1xkelly_wo1 = 100
    # starting optimal fraction 
    f_1xkelly_wo1 = 0.18
    for i in range(0,10000):
       if coinflips[y,i] == 1: 
           X_1xkelly_wo1 = X_1xkelly_wo1*(1+f_1xkelly_wo1*0.5+(1-f_1xkelly_wo1)*r)
       else: 
           X_1xkelly_wo1 = X_1xkelly_wo1*(1-f_1xkelly_wo1*0.4 +(1-f_1xkelly_wo1)*r)
       data_1xkelly_wo1[y,i] = X_1xkelly_wo1
   
starting_value_1xkelly_wo1 = 100*np.ones((21,1))
data_1xkelly_wo1 = np.append(starting_value_1xkelly_wo1, data_1xkelly_wo1, axis = 1)
terminal_values_1xkelly_wo1 = np.log(data_1xkelly_wo1[:,10000])

#####################################################

# interpolating the values between the chosen points
int_5 = interp1d(successes, terminal_values_bayesian_kelly_under)
int_6 = interp1d(successes, terminal_values_1xkelly_wo1)

plt.ylabel('logarithm of terminal wealth', fontdict=None, labelpad=None)
plt.xlabel('number of successes', fontdict=None, labelpad=None)   
plt.grid()   
plt.plot(successes,int_5(successes), '-', color = 'black', label = 'Bayesian Kelly 49520,50480')
plt.plot(successes,int_6(successes), '-', color = 'cyan', label = 'Pure Kelly, p = 49520/100k')
plt.legend(loc="upper left")

# saving the image
plt.savefig('thesis - bayesian kelly 50k-50k vs kelly (2).pdf')

plt.show()

#####################################################