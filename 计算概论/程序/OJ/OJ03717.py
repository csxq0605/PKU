# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:37:57 2023

@author: Lenovo
"""

m,n=map(int,input().split())
dp=[[0]*(n+1)for i in range(m+1)]
dp[1][1]=1
for i in range(1,m+1):
    for j in range(1,n+1):
        if i==1 and j==1:
            continue
        dp[i][j]=dp[i][j-1]+dp[i-1][j]
print(dp[m][n])