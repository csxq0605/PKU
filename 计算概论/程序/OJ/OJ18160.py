# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 11:37:14 2023

@author: Lenovo
"""

for _ in range(int(input())):
    N,M=map(int,input().split())
    grid=[]
    for _ in range(N):
        row=list(input())
        grid.append(row)
    visited=[[False]*M for _ in range(N)]  
    dir_x=[-1,0,1,0,-1,-1,1,1] 
    dir_y=[0,-1,0,1,-1,1,-1,1]
    result=[0]
    for i in range(N):
        for j in range(M):
            if grid[i][j]=='W' and not visited[i][j]:
                s=1
                stack=[(i,j)]
                visited[i][j]=True
                while stack:
                    x,y=stack.pop()
                    for k in range(8):
                        nx,ny=x+dir_x[k],y+dir_y[k]
                        if 0<=nx<N and 0<=ny<M and grid[nx][ny]=='W' and not visited[nx][ny]:
                            stack.append((nx,ny))
                            s+=1
                            visited[nx][ny]=True
                result.append(s)                            
    print(max(result))