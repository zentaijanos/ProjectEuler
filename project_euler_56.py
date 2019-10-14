#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:04:54 2019
Project Euler: 56 - Powerful digit sum
@author: zentai

a**b under 100, for a,b
sum(result, number)
"""



maxNum = 0
for i in range(1,100+1):
    for j in range(1,100+1):
        result = i**j
        res2=sum([int(i) for i in str(result)])
        if (res2 > maxNum):
            maxNum = res2
print(maxNum)