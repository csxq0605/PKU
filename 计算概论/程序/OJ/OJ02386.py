# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 23:50:51 2023

@author: Lenovo
"""

N,M=map(int, input().split())
grid=[]
for _ in range(N):
    row=list(input().strip())
    grid.append(row)
visited=[[False]*M for _ in range(N)]  
dir_x=[-1,0,1,0,-1,-1,1,1] 
dir_y=[0,-1,0,1,-1,1,-1,1]
pondCount = 0
for i in range(N):
    for j in range(M):
        if grid[i][j]=='W' and not visited[i][j]:
            pondCount+=1
            stack=[(i,j)]
            visited[i][j]=True
            while stack:
                x,y=stack.pop()
                for k in range(8):
                    nx,ny=x+dir_x[k],y+dir_y[k]
                    if nx>=0 and nx<N and ny>=0 and ny<M and grid[nx][ny]=='W' and not visited[nx][ny]:
                        stack.append((nx,ny))
                        visited[nx][ny]=True
print(pondCount)