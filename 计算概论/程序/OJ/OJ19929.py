# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 22:12:56 2023

@author: Lenovo
"""

m,n=map(int,input().split())
a=list(map(int,input().split()))
w=list(map(int,input().split()))
dp=[0]*(n+1)
for i in range(m):
    for j in range(a[i],-1,-1):
        dp[a[i]]=max(dp[a[i]],dp[j]+w[i])
print(max(dp))