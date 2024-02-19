# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 21:06:44 2023

@author: Lenovo
"""

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    check,flag=[0]*(n+1),[True]*(n+1)
    for i in l:
        if i<=n:
            check[i]+=1
    if not check[0]:
        print(0)
        continue
    minn=float("inf")
    for i in range(n+1):
        if not check[i]:
            break
        elif check[i]<minn:
            minn=check[i]
        else:
            flag[i]=False
    dp=[float("inf")]*i+[0]
    for j in range(i,-1,-1):
        if not flag[j]:
            continue
        for k in range(j,i+1):
            if not flag[k]:
                continue
            dp[j]=min(dp[j],dp[k]+k*(check[j]-1)+j)
    print(dp[0])