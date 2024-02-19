# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 16:12:52 2023

@author: Lenovo
"""

import heapq
n,m=map(int,input().split())
graph=[[]for i in range(n+1)]
for i in range(m):
    a,b,l=map(int,input().split())
    graph[a].append((l,b))
    graph[b].append((l,a))
dis=[0,0]+[float("inf")]*n
path,line,queue=[0]+[-1]*n,[],[]
heapq.heappush(queue,(0,1))
while queue:
    length,fro=heapq.heappop(queue)
    for l,to in graph[fro]:
        if dis[fro]+l<dis[to]:
            dis[to]=dis[fro]+l
            path[to]=fro
            heapq.heappush(queue,(length+l,to))
if dis[n]==float("inf"):
    line=[-1]
else:
    cnt=n
    while cnt!=-1:
        line.append(cnt)
        cnt=path[cnt]
print(*line[::-1])