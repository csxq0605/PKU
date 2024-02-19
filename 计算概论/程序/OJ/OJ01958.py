# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 23:32:15 2023

@author: Lenovo
"""

f=[[0]*15 for _ in range(5)]
f[3][1],f[4][1]=1,1
for i in range(2,13):
    f[3][i]=2*f[3][i-1]+1
    f[4][i]=float("inf")
print(1)
for i in range(2,13):
    for j in range(1,i+1):
        f[4][i]=min(f[4][j]*2+f[3][i-j],f[4][i])
    print(f[4][i])