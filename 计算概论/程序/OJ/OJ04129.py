# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 11:23:28 2023

@author: Lenovo
"""

from collections import deque
DIRS=[(-1,0),(1,0),(0,-1),(0,1)]
def bfs(grid,start,r,c,k):
    queue=deque([(start,0)])
    visited=[[[False]*k for _ in range(c)]for _ in range(r)]
    visited[start[0]][start[1]][0]=True
    while queue:
        (x,y),depth=queue.popleft()
        for dx,dy in DIRS:
            nx,ny,nd=x+dx,y+dy,(depth+1)%k
            if 0<=nx<r and 0<=ny<c and (grid[nx][ny]!='#' or nd==0):
                if visited[nx][ny][nd]:
                    continue
                if grid[nx][ny]=='E':
                    return depth+1
                visited[nx][ny][nd]=True
                queue.append(((nx,ny),depth+1))
    return -1

t=int(input())
for _ in range(t):
    r,c,k=map(int,input().split())
    grid=[list(input()) for _ in range(r)]
    start=next((i,j) for i in range(r) for j in range(c) if grid[i][j]=='S')
    ans=bfs(grid,start,r,c,k)
    if ans==-1: 
        print("Oop!")
    else: 
        print(ans)