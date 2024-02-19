# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:12:07 2023

@author: Lenovo
"""

def dfs(i,j):
    global roomarea
    if colors[i][j]:
        return
    roomarea+=1
    colors[i][j]=color
    if not (rooms[i][j]&1):
        dfs(i,j-1)
    if not (rooms[i][j]&2):
        dfs(i-1,j)
    if not (rooms[i][j]&4):
        dfs(i,j+1)
    if not (rooms[i][j]&8):
        dfs(i+1,j)

n=int(input())
m=int(input())
rooms,color,maxn=[],0,0
colors=[[0]*m for _ in range(n)]
for _ in range(n):
    rooms.append([int(i) for i in input().split()])
for i in range(n):
    for j in range(m):
        if not colors[i][j]:
            color+=1
            roomarea=0
            dfs(i,j)
            maxn=max(maxn,roomarea)
print(color)
print(maxn)