# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:33:38 2023

@author: Lenovo
"""

n,b=map(int,input().split())
value=[0]+[int(_) for _ in input().split()]
weight=[0]+[int(_) for _ in input().split()]
dp=[[0]*(b+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,b+1):
        if weight[i]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])
print(dp[n][b])