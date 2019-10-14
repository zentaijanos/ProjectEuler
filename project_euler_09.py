#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:25:09 2019
Project Euler 9: Special Pythegorean triplet
@author: zentai

Brute force:
    Calculate the Pyth. triplet till c square not equal 1000.
c = sqrt( a^2 + b^2)
"""
import numpy as np
import time
start = time.time()



x = range(1,1001)


for i in range(len(x)):
    for j in range(len(x)):
        c = np.sqrt( np.power(x[i],2) + np.power(x[j],2) )
        if ( x[i] + x[j] + c == 1000):
            #print(x[i],x[j],c)
            result = x[i]*x[j]*c
        else:
            pass
print(int(result))
elapsed = (time.time() - start)
print("Time: " + str(elapsed) + " seconds")