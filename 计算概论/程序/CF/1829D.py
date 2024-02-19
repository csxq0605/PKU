# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 17:46:36 2023

@author: Lenovo
"""

from functools import lru_cache
@lru_cache(None)

def dfs(n,m):
    if n==m:
        return 1
    if n%3!=0 or n<m:
        return 0
    return dfs(n//3,m)+dfs(n//3*2,m)

t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    if n==m:
        print("YES")
        continue
    elif n<m:
        print("NO")
        continue
    else:
        print("YES" if dfs(n,m) else "NO")