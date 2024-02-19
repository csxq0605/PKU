# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 12:42:31 2023

@author: Lenovo
"""

t,n=map(int,input().split())
l=[[0]]
for i in range(n):
    l.append(list(map(int,input().split())))
ans=[0]+[-float("inf")]*t
for i in range(1,n+1):
    for j in range(t,l[i][0]-1,-1):
        ans[j]=max(ans[j],ans[j-l[i][0]]+l[i][1])
print(ans[t] if ans[t]>=0 else -1)