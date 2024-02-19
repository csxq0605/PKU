# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 20:00:42 2023

@author: Lenovo
"""

import sys
sys.setrecursionlimit(10**8)

def count(x,v):
    if x<0:
        return 0
    else:
        return f[x]-count(x-v,v)

n,x=map(int,input().split())
l=[int(i) for i in input().split()]
f,num,ans=[0]*(x+1),0,[0]*n
f[0]=1
for i in range(n):
    for j in range(x,l[i]-1,-1):
        f[j]+=f[j-l[i]]
for i in range(n):
    if f[x]-count(x-l[i],l[i])==0:
        ans[num]=l[i]
        num+=1
print(num)
for i in range(num):
    print(ans[i],end=" ")