# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:52:11 2023

@author: Lenovo
"""

import math
def sum_2(x):
    s=0
    while x>0:
        s+=(x&1) 
        x=x>>1 
    return s

while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    ls=list(map(int,input().split()))
    w=(1<<(m+1))-1	
    result=1
    for i in range(n):
        number=ls[i+n]+1	
        limit=int(math.log(number,2))	
        rest=number-(1<<limit)	
        for j in range(limit):
            result=(result|(result<<(ls[i]*(1<<j))))&w 
        if rest>0:
            result=(result|(result<<(ls[i]*rest)))&w
    print(bin(result).count('1')-1)