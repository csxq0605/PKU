# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 00:42:06 2023

@author: Lenovo
"""

import heapq
n=int(input())
l,ans=list(map(int,input().split())),0
heapq.heapify(l)
while n>=2:
    a=heapq.heappop(l)
    b=heapq.heappop(l)
    ans+=a+b
    n-=1
    heapq.heappush(l,a+b)
print(ans)