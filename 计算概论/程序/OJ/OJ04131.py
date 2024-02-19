# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 10:21:17 2023

@author: Lenovo
"""

n,m=map(int,input().split())
things=[]
for _ in range(n):
    w,d=map(int,input().split())
    things.append((w,d))
dp=[0 for _ in range(m+1)]
for i in range(n):
    w,d=things[i]
    for j in range(m,w-1,-1):
        dp[j]=max(dp[j],dp[j-w]+d)
print(dp[m])