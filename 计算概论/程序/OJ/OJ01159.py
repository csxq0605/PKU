# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 00:53:17 2023

@author: Lenovo
"""

n=int(input())
line1=input()
line2=line1[::-1]
dp=[[0]*(n+1)for i in range(2)]
k=0
for i in range(1,n+1):
    k=(k+1)%2
    for j in range(1,n+1):
        if line1[i-1]==line2[j-1]:
            dp[k][j]=dp[1-k][j-1]+1
        else:
            dp[k][j]=max(dp[k][j-1],dp[1-k][j])
print(n-dp[k][n])