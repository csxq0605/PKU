# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 13:56:32 2023

@author: Lenovo
"""

def check(x):
    t,num=0,0
    for i in range(1,n+1):
        if a[i]-t<x:
            num+=1
        else:
            t=a[i]
    if l-t<x:
        num+=1
    return num<=m

l,n,m=map(int,input().split())
a=[0]*(n+1)
for i in range(1,n+1):
    a[i]=int(input())
le,ri=0,l
while le+1<ri:
    mid=(le+ri)//2
    if check(mid):
        le=mid
    else:
        ri=mid
print(le)