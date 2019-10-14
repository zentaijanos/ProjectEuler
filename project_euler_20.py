#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:48:47 2019
Project Euler 20: Factorial digit sum
@author: zentai
create N th factorial.
Split the numbers of it.
Add the numbers up.
"""
import math

number = math.factorial(100)

numb = str(number)

Sum = 0
for i in range(len(numb)):
    Sum = Sum + int(numb[i])
print(Sum)