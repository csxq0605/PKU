# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 00:14:38 2023

@author: Lenovo
"""

n=int(input())
l=list(map(int,input().split()))
l.sort()
ans1,j=[],0
for i in range(1,n+1):
    if i==l[j]:
        j+=1
    else:
        ans1.append(i)
print(*ans1)
print(*l[j::])