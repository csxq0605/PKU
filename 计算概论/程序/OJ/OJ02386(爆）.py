# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 23:36:58 2023

@author: Lenovo
"""

N,M=map(int,input().split())
grid=[]
for _ in range(N):
    row=list(input().strip())
    grid.append(row)
visited=[[False]*M for _ in range(N)]

def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=M or grid[x][y]=='.' or visited[x][y]:
        return
    visited[x][y]=True
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx=x + dx
            ny=y + dy
            dfs(nx,ny)

pondCount=0
for i in range(N):
    for j in range(M):
        if grid[i][j]=='W' and not visited[i][j]:
            dfs(i,j)
            pondCount+=1
print(pondCount)