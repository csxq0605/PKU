# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:11:57 2023

@author: Lenovo
"""

while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    l=[int(i) for i in input().split()]
    price=l[:n]
    number=l[n:]
    dp=[0]+[-1]*m
    for i in range(n):
        for j in range(m+1):
            if dp[j]>=0:
                dp[j]=number[i]
            else:
                dp[j]=-1
        for j in range(m-price[i]+1):
            if dp[j]>=0:
                dp[j+price[i]]=max(dp[j+price[i]],dp[j]-1)
    ans=0
    for i in range(1,m+1):
        if dp[i]>=0:
            ans+=1
    print(ans)