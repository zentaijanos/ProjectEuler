#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:46:35 2019
Project Euler 4: Largest palindrome product
@author: zentai 
"""
import time
start = time.time()
x = range(100,1000)
maxElement = 0

for i in range(len(x)):
    for j in range(len(x)):
        c = x[i]*x[j]
        if ( str(c) == str(c)[::-1] and c > maxElement):
            maxElement = c
        else:
            pass
print('Result:\n',maxElement,'\n')
elapsed = (time.time() - start)
print("Time: " + str(elapsed) + " seconds")