# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 14:42:24 2023

@author: Lenovo
"""

def dfs(i,a,x):
    if dp[i][a]!=-1:
        return dp[i][a]
    left=right=10**8
    flag=True
    for j in range(i+1,n+1):
        if p[i][2]-p[j][2]>maxn:
            flag=False
            break
        if p[j][0]<=x<=p[j][1]:
            left=dfs(j,0,p[j][0])+p[i][2]-p[j][2]+x-p[j][0]
            right=dfs(j,1,p[j][1])+p[i][2]-p[j][2]+p[j][1]-x
            flag=False
            break
    dp[i][a]=min(left,right)
    if flag and p[i][2]<=maxn:
        dp[i][a]=p[i][2]
    return dp[i][a]

for _ in range(int(input())):
    dp=[[-1,-1] for _ in range(1010)]
    p=[] 
    n,x,y,maxn=map(int,input().split())
    p.append([x,x,y]) 
    for _ in range(n):
        p.append([int(i) for i in input().split()])
    p.sort(key=lambda x:x[2],reverse=True)
    print(dfs(0,1,x))