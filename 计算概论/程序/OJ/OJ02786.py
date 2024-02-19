# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 11:22:36 2023

@author: Lenovo
"""

dp=[0]*1000001
dp[1],dp[2]=1,2
for i in range(3,1000001):
    dp[i]=(2*dp[i-1]+dp[i-2])%32767
for _ in range(int(input())):
    print(dp[int(input())])