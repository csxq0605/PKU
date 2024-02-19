# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:07:14 2023

@author: Lenovo
"""

n=int(input())
s=[int(i) for i in input().split()]
r=[0]*(n+1)
for i in range(n):
    maxn=1
    for j in range(i):
        if s[j]<s[i] and r[j]+1>maxn:
            maxn=r[j]+1
    r[i]=maxn
l=[0]*(n+1)
for i in range(n-1,-1,-1):
    maxn=1
    for j in range(n-1,i-1,-1):
        if s[j]<s[i] and l[j]+1>maxn:
            maxn=l[j]+1
    l[i]=maxn
ans=0
for i in range(n):
    ans=max(ans,l[i]+r[i]-1)
print(ans)