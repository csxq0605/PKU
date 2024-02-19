# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 10:52:54 2023

@author: Lenovo
"""

n,m=map(int,input().split())
l=[0]*n
D=[[0]*n for _ in range(n)]
A=[[0]*n for _ in range(n)]
L=[[0]*n for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    l[a]+=1
    l[b]+=1
    A[a][b]=1
    A[b][a]=1
for i in range(n):
    D[i][i]=l[i]
for i in range(n):
    for j in range(n):
        L[i][j]=str(D[i][j]-A[i][j])
for k in range(n):
    print(" ".join(L[k]))