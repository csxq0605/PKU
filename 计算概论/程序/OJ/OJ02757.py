# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 21:27:27 2023

@author: Lenovo
"""

n=int(input())
s=[int(i) for i in input().split()]
r=[0]*(n+1)
for i in range(n):
    maxn=1
    for j in range(i):
        if s[j]<s[i] and r[j]+1>maxn:
            maxn=r[j]+1
    r[i]=maxn
print(max(r))