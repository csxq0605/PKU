# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 00:30:33 2023

@author: Lenovo
"""

n,m=map(int,input().split())
l=list(map(int,input().split()))
ans=0
for i in range(n):
    if l[i]<=m:
        m-=l[i]
        ans+=1
    else:
        print(ans)
        break