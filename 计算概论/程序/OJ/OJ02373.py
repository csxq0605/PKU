# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:30:37 2023

@author: Lenovo
"""

import heapq

n,l=map(int,input().split())
a,b=map(int,input().split())
cow=[0]*(l+1)
for _ in range(n):
    s,e=map(int,input().split())
    for j in range(s+1,e):
        cow[j]=1
d=[-1]*(l+1)
a2=a*2
b2=b*2
heap=[]
for i in range(a2,l+1,2):
    if i<=b2:
        if cow[i]==0:
            d[i]=1
            if i<=b2+2-a2:
                heapq.heappush(heap,(d[i],i))
        continue
    else:
        if cow[i]==0:
            while heap and heap[0][1]<i-b2:
                heapq.heappop(heap)
            if heap:
                d[i]=heap[0][0]+1
        if d[i-a2+2]>=0:
            heapq.heappush(heap,(d[i-a2+2],i-a2+2))
print(d[l])