#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:09:17 2019
PE 63 Powerful digit counts
@author: zentai
"""

n = 0

powers = [1,2,3,4,5,6,7,8,9]

for i in range(1,1000000):
    for j in range(1,100):
        power = i**j
        if(str(len(str(power)))==str(j)):
            n=n+1
        #print(power,str(len(str(power)))==str(j))
print(n)
        
        
# update: same code faster,
# realize that from math expression that n < 10