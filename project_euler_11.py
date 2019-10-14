#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:39:38 2019
Project Euler 11: Largest product in a grid
@author: zentai
20x20 mtx:
vegigiteralni soronkent es oszloponkent,
sor, oszlop, diagonális muveletek
minden egyes listában vegigmenni külön, és megkeresni a legnagyobb egymás mellett álló 4 elemet
ezek szorzatát megtartani
összehasonlítani az oszlop/soronkénti tárolt elemekkel melyik a legnagyobb.
"""

import time
start = time.time()

import numpy as np

data = np.loadtxt("pe_11.txt",dtype=int)

maxD = 0
for j in range(len(data[0])):
    for i in range(len(data[0])):
        #print(data[0][i])
        if (data[j][i] > maxD):
            #print("van")
            maxD = data[j][i]
            print(j,i)
        else:
            pass



print(maxD)





end = time.time()
print('Time:',(end-start))