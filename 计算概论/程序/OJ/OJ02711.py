# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 21:15:56 2023

@author: Lenovo
"""

n=int(input())
s=[int(i) for i in input().split()]
r,l=[0]*(n+1),[0]*(n+1)
for i in range(n):
    maxn=1
    for j in range(i):
        if s[j]<s[i] and r[j]+1>maxn:
            maxn=r[j]+1
    r[i]=maxn
for i in range(n-1,-1,-1):
    maxn=1
    for j in range(n-1,i-1,-1):
        if s[j]<s[i] and l[j]+1>maxn:
            maxn=l[j]+1
    l[i]=maxn
minn=n
for i in range(n):
    if minn>n-l[i]-r[i]+1:
        minn=n-l[i]-r[i]+1
print(minn)