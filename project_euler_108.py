#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 09:25:02 2019
Project Euler 108: Diophantine reciprocals I
@author: zentai

n et leptetve kiszamolni a a tort egysegeket.
1/x + 1/y = 1/n
"""



diop_numb = 0

#for n in range(1,11):
len_list=[]
store = []


#for n in range(1,11):


def calcFract(n):
    for y in range(1,21):
        for x in range(1,21):
            if(1/x + 1/y == 1/n and
               (x,y) not in store and 
               (x,y)[::-1] not in store):
                store.insert(1+len(store),(x,y))                
            else:
                store
    return store

for n in range(1,10):
    #len_list.append(len(calcFract(n)))
    length = len(calcFract(n))
    if (length == 1000):
        print('bingo')
    else:
        print('nincs')
            

#print(len_list)