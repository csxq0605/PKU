# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:41:19 2023

@author: Lenovo
"""

n=int(input())
dic=[]
for a1 in range(n,-1,-1):
    for a2 in range(n,-1,-2):
        for a3 in range(n-n%3+3-a2%3,-1,-3):
            if a3<=n and (a1+a2+a3)%5==0:
                tot=a1+a2+a3
                dic.append(tot)
dic.sort()
print(dic[-1])