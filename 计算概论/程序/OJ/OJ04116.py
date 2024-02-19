# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 07:59:27 2023

@author: Lenovo
"""

import heapq

class position:
    def __init__(self,x,y,t):
        self.x=x
        self.y=y
        self.t=t
    def __lt__(self,other):
        return self.t<other.t

t=int(input())
results=[]
for _ in range(t):
    n,m=map(int,input().strip().split())
    maze=[[0]*m for _ in range(n)]
    visited=[[0]*m for _ in range(n)]
    start,end=None,None
    for i in range(n):
        line=list(input().strip())
        for j in range(m):
            if line[j]=='r':
                start=position(i,j,0)
                visited[i][j]=1
            elif line[j]=='a':
                end=(i,j)
            elif line[j]=='x':
                maze[i][j]=1
            elif line[j]=='#': 
                maze[i][j]=-1
    queue=[]
    heapq.heappush(queue,start)
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    while queue:
        x,y,time=queue[0].x,queue[0].y,queue[0].t
        if (x,y)==end: 
            break
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and maze[nx][ny]!=-1:
                visited[nx][ny]=1
                if maze[nx][ny]==0:
                    new_time=time+1
                else:
                    new_time=time+2
                heapq.heappush(queue,position(nx,ny,new_time))
        heapq.heappop(queue)
    if not queue:
        results.append('Impossible')
    else:
        results.append(time)
for res in results:
    print(res)