# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 19:43:16 2023

@author: Lenovo
"""

def max_money(n, m):
    p=[0]*(n+1)
    q=[0]*(n+1)
    minn=m[1]
    p[1]=0
    for i in range(2,n+1):
        minn=min(m[i],minn)
        p[i]=max(p[i-1],m[i]-minn)
    maxn=m[n]
    q[n]=0
    for i in range(n-1,0,-1):
        maxn=max(m[i],maxn)
        q[i]=max(q[i+1],maxn-m[i])
    money=0
    for i in range(1,n+1):
        money=max(p[i-1]+q[i],money)
    return money

t = int(input())
for _ in range(t):
    n=int(input())
    m=[0]+list(map(int,input().split()))
    result=max_money(n,m)
    print(result)