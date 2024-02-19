# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 10:27:54 2023

@author: Lenovo
"""

n=int(input())
dp=[0]*(n+1)
dp[0]=dp[1]=1
for i in range(2,n+1):
    for j in range(1,i+1):
        dp[i]+=dp[i-j]*dp[j-1]
print(dp[n])