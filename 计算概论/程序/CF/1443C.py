# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 15:18:25 2023

@author: Lenovo
"""

t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    l=sorted(zip(a,b))
    ans=minn=sum(b)
    for i in l:
        ans-=i[1]
        minn=min(max(ans,i[0]),minn)
    print(minn)