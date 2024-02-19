# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:32:44 2023

@author: Lenovo
"""

import heapq
n=int(input())
stops,fuel,line=[0],[0],[]
for i in range(n):
    line.append(list(map(int,input().split())))
line.sort()
for i in line:
    x,num=i
    stops.append(x)
    fuel.append(num)
l,p=map(int,input().split())
queue,ans=[],0
for i in range(n,-1,-1):
    d=l-stops[i]
    while d>p:
        if not queue:
            print(-1)
            quit()
        p+=-1*heapq.heappop(queue)
        ans+=1
    heapq.heappush(queue,-fuel[i])
    p-=d
    l=stops[i]
print(ans)