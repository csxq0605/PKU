# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:54:46 2023

@author: Lenovo
"""

t=int(input())
for i in range(t):
    n=int(input())
    l=[int(_) for _ in input().split()]
    l.sort()
    ans=n//2
    for i in range(1,n):
        if l[i]!=l[i-1]:
            ans=max(ans,i*(n-i))
    print(ans)