# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 23:49:43 2023

@author: Lenovo
"""

n,m=map(int,input().split())
cost=list(map(int,input().split()))
l=list(map(int,input().split()))
dp=[0]+[float("inf")]*n
for i in range(m):
    num,c=l[i],cost[i]
    k=1
    while num>0:
        tmp=min(num,k)
        num-=tmp
        for j in range(n,c*tmp-1,-1):
            dp[j]=min(dp[j],dp[j-tmp*c]+tmp)
        k*=2
print(dp[n] if dp[n]!=float("inf") else "Fail")