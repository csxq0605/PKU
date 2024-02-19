# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 00:05:19 2023

@author: Lenovo
"""

n=int(input())
l,num=[],2
for i in range(n):
    w=[int(_) for _ in input().split()]
    l.append(w)
for i in range(1,n-1):
    x,h=map(int,l[i])
    if x-h>l[i-1][0]:
        num+=1
    elif x+h<l[i+1][0]:
        num+=1
        l[i][0]+=h
print(num if n>1 else 1)