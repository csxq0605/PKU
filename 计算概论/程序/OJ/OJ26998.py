# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:09:21 2023

@author: Lenovo
"""

ans=[]
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    dp=[0]*n
    result=1
    for i in range(n):
        maxn=1
        for j in range(i):
            if l[j]&l[i]!=0 and dp[j]+1>maxn:
                maxn=dp[j]+1
        dp[i]=maxn
        result=max(result,maxn)
    ans.append(result)
for i in ans:
    print(i)