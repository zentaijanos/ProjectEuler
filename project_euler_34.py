#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 09:12:41 2019
Project Euler 34: Digit factorials
@author: zentai
"""
import numpy as np

def factorial(x_nth):
# kod tovabbfejlesztese.    
    
    if type(x_nth) == str:
        x_nth = int(x_nth)
        number = np.linspace(1,x_nth,x_nth,dtype=int)
        factor = number[0]
        for i in range(x_nth-1):
            factor = factor * number[i+1]
        return factor
        
    else:
        number = np.linspace(1,x_nth,x_nth,dtype=int)
        factor = number[0]
        for i in range(x_nth-1):
            factor = factor * number[i+1]
        return factor
    
numbers = np.linspace(3,10,10,dtype=int)

digit = 10
StringDigit = str(digit)
result = 0

for n in range(len(StringDigit)):
    result = result + factorial(StringDigit[n])

if (result == digit):
    print(result)
else:
    print('nem')





























