# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 10:35:07 2023

@author: Lenovo
"""

def best_combine(n,a):
    dp=[0]*(a+1)
    for price in prices:
        for i in range(a,price-1,-1):
            dp[i]=max(dp[i],dp[i-price]+price)
    return dp[a]

n,t=map(int,input().split())
prices=list(map(int,input().split()))
if sum(prices)<t:
    print(0)
else:    
    result=best_combine(n,sum(prices)-t)
    print(sum(prices)-result)