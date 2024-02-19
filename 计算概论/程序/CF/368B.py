# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:14:34 2023

@author: Lenovo
"""

n,m=map(int,input().split())
a=[int(i) for i in input().split()]
l=[]
for i in range(m):
    l.append(int(input())-1)
ans,s=[0]*(n+1),set()
for i in range(n-1,-1,-1):
    if a[i] not in s:
        s.add(a[i])
        ans[i]=ans[i+1]+1
    else:
        ans[i]=ans[i+1]
for i in l:
    print(ans[i])