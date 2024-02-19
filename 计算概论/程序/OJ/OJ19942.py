# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:07:02 2023

@author: Lenovo
"""

m,n,p,q=map(int,input().split())
l,x=[],[]
for i in range(m):
    l.append([int(_) for _ in input().split()])
for i in range(p):
    x.append([int(_) for _ in input().split()])
ans=[[0]*(n+1-q) for _ in range(m+1-p)]
for i in range(m+1-p):
    for j in range(n+1-q):
        for a in range(p):
            for b in range(q):
                ans[i][j]+=x[a][b]*l[i+a][j+b]
        ans[i][j]=str(ans[i][j])
for _ in range(m+1-p):
    print(" ".join(ans[_]))