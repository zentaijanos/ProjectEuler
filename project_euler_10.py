#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:25:32 2019
Project Euler 10: Summation of primes
@author: zentai

Loop for 2 million, and detect all primes, and during the loop, sum them up.
"""


import math
import time

start = time.time()

def is_prime(number):
    if number > 1:
        if number == 2:
            return 2
        if number % 2 == 0:
            return 0
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return 0
        return number
    return 0

Sum = 0
N = 2000000

for n in range(2,N):        
    Sum = Sum + is_prime(n)
print(Sum)

elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds")


