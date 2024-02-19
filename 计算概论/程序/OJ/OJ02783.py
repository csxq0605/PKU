# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 09:49:32 2023

@author: Lenovo
"""

while True:
    n=int(input())
    if n==0:
        break
    l=[list(map(int,input().split())) for i in range(n)]
    l.sort(key=lambda x:(x[1],x[0]))
    maxd=float("inf")
    ans=0
    for i in range(n):
        if l[i][0]<maxd:
            ans+=1
            maxd=l[i][0]
    print(ans)