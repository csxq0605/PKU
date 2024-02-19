# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 09:50:34 2023

@author: Lenovo
"""

n,m,ka=map(int,input().split())
dp=[[0]*(m+1) for _ in range(n+1)]
b,d=[0]*(ka+1),[0]*(ka+1)
m-=1
for i in range(1,ka+1):
    b[i],d[i]=map(int,input().split())
for i in range(1,ka+1):
    for j in range(n,b[i]-1,-1):
        for k in range(m,d[i]-1,-1):
            dp[j][k]=max(dp[j][k],dp[j-b[i]][k-d[i]]+1)
for k in range(m+1):
    if dp[n][k]==dp[n][m]:
        r=m+1-k
        break
print('{} {}'.format(dp[n][m],r))