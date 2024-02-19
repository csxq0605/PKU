# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 19:03:21 2023

@author: Lenovo
"""

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    le,ri=l[0]+1,l[-1]-n
    l1,l2=[le],[ri]
    for i in range(1,n):
        le=max(le,l[i]+i+1)
        ri=max(ri,l[-1-i]-n+i)
        l1.append(le)
        l2.append(ri)
    ans=0
    for i in range(2,n):
        ans=max(ans,l1[i-2]+l[i-1]+l2[-1-i])
    print(ans)