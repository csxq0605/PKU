# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 10:25:23 2023

@author: Lenovo
"""

import heapq
class position:
    def __init__(self,x,t):
        self.x=x
        self.t=t
    def __lt__(self,other):
        return self.t<other.t

n,k=map(int,input().split())
visited=[0]*100010
queue=[]
heapq.heappush(queue,position(n,0))
visited[n]=1
while queue:
    x,time=queue[0].x,queue[0].t
    if x==k:
        print(time)
        break
    if x-1>=0 and not visited[x-1]:
        visited[x-1]=1
        heapq.heappush(queue,position(x-1,time+1))
    if x+1<=100000 and not visited[x+1]:
        visited[x+1]=1
        heapq.heappush(queue,position(x+1,time+1))
    if 2*x<=100000 and not visited[2*x]:
        visited[2*x]=1
        heapq.heappush(queue,position(2*x,time+1))
    heapq.heappop(queue)