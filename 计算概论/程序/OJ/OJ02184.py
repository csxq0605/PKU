# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 10:42:55 2023

@author: Lenovo
"""

N,H=200000,100000
dp=[-float("inf")]*(N+1)
dp[H]=0
w=[]
v=[]
n=int(input())
for i in range(n):
    wi,vi=map(int,input().split())
    w.append(wi)
    v.append(vi)
for i in range(n):
    if w[i]>0:
        for j in range(N,w[i]-1,-1):
            dp[j]=max(dp[j],dp[j-w[i]]+v[i])
    else:
        for j in range(0,N+w[i]+1):
            dp[j]=max(dp[j],dp[j-w[i]]+v[i])
res=0
for j in range(H,N+1):
    if dp[j]>=0:
        res=max(res,dp[j]+j-H)
print(res)