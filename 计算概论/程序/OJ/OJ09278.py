# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 00:06:44 2023

@author: Lenovo
"""

n=int(input())
dp=[0]*(n+1)
dp[2]=1
for i in range(3,n+1):
    dp[i]=(i-1)*(dp[i-1]+dp[i-2])
print(dp[n])