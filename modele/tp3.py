# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 13:27:10 2021

@author: rroy
"""
import numpy as np

matP = np.array([[2, 4, 0, 1], 
                [0, 1, 1, 1]])

v1 = matP [:, 0].reshape(2, 1)
v1 = matP [:, 0].reshape(1, 2)

v2 = np.array([[4], [1]])


v3 = np.dot(v1, v2)

print (v3)
