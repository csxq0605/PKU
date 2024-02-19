# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:27:57 2023

@author: Lenovo
"""
import heapq

n,k=map(int,input().split())
l=[-int(i) for i in input().split()]
heap,out=[],[]
for i in range(k-1):
    heapq.heappush(heap,(l[i],i))
for i in range(k-1,n):
    heapq.heappush(heap,(l[i],i))
    num,No=heapq.heappop(heap)
    while No<i-k+1:
        num,No=heapq.heappop(heap)
    out.append(str(-num))
    heapq.heappush(heap,(num,No))
print(" ".join(out))