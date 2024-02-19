# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 10:39:04 2023

@author: Lenovo
"""

def dfs(w,k):
    if w==0:
        return 1
    if k<=0:
        return 0
    return dfs(w,k-1)+dfs(w-l[k],k-1)

n=int(input())
l=[0]
for _ in range(n):
    l.append(int(input()))
print(dfs(40,n))