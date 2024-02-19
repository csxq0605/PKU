# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:00:17 2023

@author: Lenovo
"""

for _ in range(int(input())):
    e,f=map(int,input().split())
    tw=f-e
    n=int(input())
    p,w=[],[]
    for i in range(n):
        pi,wi=map(int,input().split())
        p.append(pi)
        w.append(wi)
    dp=[0]+[float("inf")]*tw
    for i in range(n):
        for j in range(w[i],tw+1):
            dp[j]=min(dp[j],dp[j-w[i]]+p[i])
    print(f"The minimum amount of money in the piggy-bank is {dp[tw]}."if dp[tw]!=float("inf") else "This is impossible.")