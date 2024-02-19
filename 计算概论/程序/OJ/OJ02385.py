# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:11:58 2023

@author: Lenovo
"""

t,w=map(int,input().split())
l=[0]*(t+1)
for i in range(1,t+1):
    l[i]=int(input())
dp=[[0]*(w+1) for i in range(t+1)]
for i in range(1,t+1):
    for j in range(0,w+1):
        if j==0:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])
        if l[i]-j&1==1:
            dp[i][j]+=1
print(max(dp[t]))