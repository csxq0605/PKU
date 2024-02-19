# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 16:15:32 2023

@author: Lenovo
"""

n,m=map(int,input().split())
l=[int(i) for i in input().split()]
l.sort()
d=0
minus=[0]*(n-1)
for i in range(n-1):
    minus[i]=l[i+1]-l[i]
minus.sort()
for i in range(n-m):
    d+=minus[i]
print(d)