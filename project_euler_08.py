#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:05:22 2019

Project Euler 8: Largest product in series
@author: zentai

Given a list, 1000 long. Multiply the near 4 elements, and determine the biggest value given sequence.
New N is 13 here.
How to loop properly throug of the list with 4 elements.
kell egy 4 len multiply resz, ami tudja, ha ki van csuszva belole. - Határfeltételek kezelése
es kell egy max elem kereső.


Algoritmus gyorsitas, ha 0 van, akkor kuka, illetve talan a szorzatokat mar ismeri ami mar szerepelt. (tarolas? ez gyorsit?)

"""
import time

start = time.time()

with open('pe_08.txt', 'r') as file:
    data = file.read().replace('\n', '')


result = 1
maxMult=0
for i in range(len(data)-12):
    #if (int(data[i])==0 or int(data[i+1])==0 or int(data[i+2])==0 or int(data[i+3])==0 or int(data[i+4])==0 or int(data[i+5])==0 or int(data[i+6])==0 or int(data[i+7])==0 or int(data[i+8])==0 or int(data[i+9])==0 or int(data[i+10])==0 or int(data[i+11])==0 or int(data[i+12])):
    #    pass   
        
    result = int(data[i])*int(data[i+1])*int(data[i+2])*int(data[i+3])*int(data[i+4])*int(data[i+5])*int(data[i+6])*int(data[i+7])*int(data[i+8])*int(data[i+9])*int(data[i+10])*int(data[i+11])*int(data[i+12])
    if result > maxMult:
        maxMult = result
print(maxMult)

elapsed = (time.time() - start)
print("Time: " + str(elapsed) + " seconds")





