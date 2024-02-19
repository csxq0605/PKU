# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 11:03:55 2023

@author: Lenovo
"""

dp=[[0]*15001 for _ in range(21)]
numc,numg=map(int,input().split())
pos=[0]+list(map(int,input().split()))
weight=[0]+list(map(int,input().split()))
dp[0][7500]=1
for i in range(1,numg + 1):
    for j in range(15001):
        if dp[i-1][j]:
            for k in range(1,numc+1):
                dp[i][j+weight[i]*pos[k]]+=dp[i-1][j]
print(dp[numg][7500])