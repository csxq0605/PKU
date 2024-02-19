# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 23:46:30 2023

@author: Lenovo
"""

v,p=map(int,input().split())
x=[0]+list(map(int,input().split()))
dis=[[0]*(v+1)for _ in range(v+1)]
dp=[[0]*(v+1) for _ in range(v+1)]
for i in range(1,v+1):
    for j in range(i+1,v+1):
        dis[i][j]=dis[i][j-1]+x[j]-x[(i+j)//2]
for i in range(1,v+1):
    dp[i][i]=0
    dp[i][1]=dis[1][i]
for j in range(2,p+1):
    for i in range(j+1,v+1):
        dp[i][j]=float("inf")
        for k in range(j-1,i):
            dp[i][j]=min(dp[i][j],dp[k][j-1]+dis[k+1][i])
print(dp[v][p])