# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 09:02:32 2023

@author: Lenovo
"""

n=int(input())
s=[int(i) for i in input().split()]
r=[0]*n
d=[0]*n
for i in range(n):
    maxn=1
    for j in range(i):
        if r[j]==1 and s[i]!=s[j]:
            maxn=max(2,maxn)
            d[i]=s[i]-s[j]
        elif (s[i]-s[j])*d[j]<0 and r[j]+1>maxn:
            maxn=r[j]+1
            d[i]=s[i]-s[j]
    r[i]=maxn
print(max(r))