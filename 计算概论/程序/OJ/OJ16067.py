# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 10:16:08 2023

@author: Lenovo
"""

while True:
    n=int(input())
    if n==0:
        break
    l=[list(map(int,input().split()))for _ in range(n)]
    l.sort(key=lambda x:x[1])
    r=ans=0
    for i in range(n):
        if l[i][0]>=r:
            ans+=1
            r=l[i][1]
    print(ans)