# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 11:19:01 2023

@author: Lenovo
"""

n,k=map(int,input().split())
l=[0]+[int(input()) for i in range(n)]
dp=[[-float("inf")]*k for i in range(n+1)]
dp[0][0]=0
for i in range(1,n+1):
    for j in range(k):
        dp[i][j]=max(dp[i-1][j],dp[i-1][((j-l[i])%k+k)%k]+l[i])
print(dp[n][0])