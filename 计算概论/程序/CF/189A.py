# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 23:04:12 2023

@author: Lenovo
"""

n,a,b,c=map(int,input().split())
l=[a,b,c]
f=[0]*(n+1)
for i in range(n+1):
    if i!=0 and f[i]==0:
        continue
    for j in range(3):
        index=i+l[j]
        if index<=n:
            f[index]=max(f[index],f[i]+1)
print(f[n])