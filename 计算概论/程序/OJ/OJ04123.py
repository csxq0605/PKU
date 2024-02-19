# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:32:15 2023

@author: Lenovo
"""

d=[(1,2),(2,1),(-1,2),(-2,1),(-1,-2),(-2,-1),(1,-2),(2,-1)]
maze=[[0]*11 for _ in range(11)]
ans=0
def dfs(step,x,y):
    global ans,maze
    if step==n*m:
        ans+=1
        return
    for i in range(8):
        nx,ny=d[i]
        nx,ny=x+nx,y+ny
        if 0<=nx<n and 0<=ny<m and not maze[nx][ny]:    
            maze[nx][ny]=1
            dfs(step+1,nx,ny)
            maze[nx][ny]=0

t=int(input())
for i in range(t):
    n,m,x0,y0=map(int,input().split())
    maze=[[0]*11 for _ in range(11)]
    ans=0
    maze[x0][y0]=1
    dfs(1,x0,y0)
    print(ans)