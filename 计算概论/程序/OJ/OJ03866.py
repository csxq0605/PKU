# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 10:52:54 2023

@author: Lenovo
"""

ans=0
def dfs(x,y):
    if mp[x][y]=='#' or visited[x][y]:
        return
    if x<1 or x>h or y<1 or y>w:
        return
    global ans
    ans+=1
    visited[x][y]=True
    dfs(x,y+1)
    dfs(x,y-1)
    dfs(x-1,y)
    dfs(x+1,y)

while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    ans=0
    mp=[['']*(w+2) for _ in range(h+2)]
    visited=[[False]*(w + 2) for _ in range(h+2)]
    for i in range(1,h+1):
        row=input()
        for j in range(1,w+1):
            mp[i][j]=row[j-1]
            if mp[i][j]=='@':
                x,y=i,j
    dfs(x,y)
    print(ans)