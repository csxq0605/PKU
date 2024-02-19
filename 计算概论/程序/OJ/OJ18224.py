# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:21:48 2023

@author: Lenovo
"""

import math
m=int(input())
l=list(map(int,input().split()))
for _ in range(m):
    num,flag=l[_],False
    i=1
    while not flag and i<=int(math.sqrt(num)):
        j=i
        while not flag and j<=int(math.sqrt(num-i**2)):
            if i**2+j**2==num:
                print(bin(num),oct(num),hex(num))
                flag=True
            j+=1
        i+=1