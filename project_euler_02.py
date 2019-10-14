#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 14:36:14 2019
Project Euler 2: Fibonacci numbers
@author: zentai

Algo: X_n+2 = X_n+1 + X_n
Task: Add then even value Fibo numbers under 4 mill. 


xn = [1,2]

for i in range(0,400):

    if(xn[i] % 2 == 0):
        result = xn[i]+xn[i+1]
        xn.append(result)
    else:
        None

print(xn)
"""

x = 1
y = 1
z = 0
result = 0

while z < 4000000:
   z = (x+y)         
   if z%2 == 0:
       result = result + z

   #next iteration

   x = y
   y = z

print(result)