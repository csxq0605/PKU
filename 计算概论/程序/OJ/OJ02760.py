# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 15:11:13 2023

@author: Lenovo
"""

n=int(input())
delta=[[0]]
for i in range(n):
    delta.append([0]+list(map(int,input().split())))
dp=[[0]*(n+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+delta[i][j]
print(max(dp[n]))