# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 11:18:00 2021

@author: rroy
"""
import numpy as np
import matplotlib.pyplot as plt


#sizechansimule=5
#data = np.random.rand(sizechansimule)
#plt.xlim(-1,3)
#plt.ylim(-0.5,1)
#plt.title('Histogram of simulated data')
#plt.grid(True)
#plt.hist(data, bins=5, color='g',edgecolor='red',alpha=1)

n=500
p = 0.4
valeurX = [0, 1]
compte = np.array([0, 0])

for k in range(n):
    U = np.random.rand()
    if (U < p):
        compte[1] = compte[1] + 1
    else : 
        compte[0] = compte[0] + 1
        
freqX = compte/n
print('frequence = ', freqX)
plt.bar(valeurX, freqX, width = 0.02, color = 'red')