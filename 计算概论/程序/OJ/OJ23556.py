# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 00:18:51 2023

@author: Lenovo
"""

n=int(input())
dp=[0]*(n+1)
dp[0]=dp[1]=1
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])