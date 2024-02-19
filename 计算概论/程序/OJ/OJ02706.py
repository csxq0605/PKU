# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 00:31:22 2023

@author: Lenovo
"""

import math
def multiply(t):
    carry=0
    for i in range(99,-1,-1):
        tmp=(ans[i]<<t)+carry
        carry=tmp//100000
        ans[i]=tmp-carry*100000

p=int(input())
ans=[0]*100
print(int(p*math.log10(2)+1))
ans[99]=1
t=p//14
while t>0:
    multiply(14)
    t-=1
multiply(p%14)
ans[99]-=1
for i in range(1,101):
    print(f"{ans[i-1]:05d}",end="")
    if i%10==0:
        print("")