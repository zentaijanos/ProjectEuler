#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:49:09 2019
Project Euler 7: 10001st prime
@author: zentai

method1:
    loop over long long time above natural numbers
    on each number check if its prime or not (func)
    if yes upgrade the n variable
        run the code till n == 10001
    print(x)
"""



def prime_checker(num):
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               return False
       else:           
           return True
    else:
       return False
nth = 0


while nth < 10001:
    for n in range(5000000):

        result = prime_checker(n)
        if (result == True):
            nth=nth+1
            if ( nth == 10001):
                 print(n)
                 break
        else:
            pass
    
print(nth)