# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 00:41:33 2023

@author: Lenovo
"""

def mid(x,y,z):
    l=[x,y,z]
    l.sort()
    return l[1]

n=int(input())
a=[int(input())for i in range(n)]
b=a.copy()
ans=0
for i in range(1,n-1):
    b[i]=mid(a[i],b[i-1],b[i+1])
for i in range(n):
    ans+=abs(a[i]-b[i])
for i in range(n-1):
    ans+=abs(b[i]-b[i+1])
print(ans)