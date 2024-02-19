# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:14:40 2023

@author: Lenovo
"""

import heapq

n=int(input())
l,ans=[],0
for _ in range(n):
    heapq.heappush(l,int(input()))
while n>=2:
    a=heapq.heappop(l)
    b=heapq.heappop(l)
    ans+=a+b
    n-=1
    heapq.heappush(l,a+b)
print(ans)