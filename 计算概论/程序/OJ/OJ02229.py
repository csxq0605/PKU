# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 10:52:40 2023

@author: Lenovo
"""

n=int(input())
dp=[1]+[0]*n
for i in range(1,n+1):
    if i%2==1:
        dp[i]=dp[i-1]
    else:
        dp[i]=dp[i-1]+dp[i//2]
print(dp[n]%10**9)