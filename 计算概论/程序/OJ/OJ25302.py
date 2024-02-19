# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:48:16 2023

@author: Lenovo
"""

for _ in range(int(input())):
    n=int(input())
    x,y=[],[]
    for i in range(n):
        xi,yi=map(int,input().split())
        x.append(xi)
        y.append(yi)
    ans=0
    for i in range(n):
        tmp=0
        for j in range(n):
            if x[j]<=x[i]<y[j]:
                tmp+=1
        ans=max(ans,tmp)
    print(ans)