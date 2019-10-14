# -*- coding: utf-8 -*-


import numpy as np




def numbGen(n=2000000):
    digit = '0.'
    
    for i in range(1,n+1):
        digit = digit + str(i)
    
    return digit


longNum = numbGen(200000)



result = int(longNum[2])*int(longNum[2*10]) * int(longNum[2*100])*int(longNum[2*1000]) * int(longNum[2*10000]) * int(longNum[2*100000]) * int(longNum[2*100000])
print(result) 