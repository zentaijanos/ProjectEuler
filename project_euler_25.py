#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:54:11 2019
Project Euler 25: 1000-digit Fibonacci number
@author: zentai
"""

f = [1,1]

for i in range(10000):
    F_n = f[i] + f[i+1]
    if ( len(str(F_n)) > 1000):
        print(i)
        break
    f.append(F_n)

