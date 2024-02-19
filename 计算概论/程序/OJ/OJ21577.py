# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:08:57 2023

@author: Lenovo
"""

m,n=map(int,input().split())
martix=[[1]*(n+2)]
martix.extend([[1]+list(map(int, input().split()))+[1] for _ in range(m)])
maze=[[0]*(n+1) for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if not martix[i][j]:
            maze[i][j]=maze[i][j-1]+1
        else:
            maze[i][j]=0
smax=0
for i in range(1,m+1):
    for j in range(1,n+1):
        if maze[i][j]!=0:
            width=1
            length=maze[i][j]
            area=width*length
            smax=max(smax,area)
            for k in range(i-1,0,-1):
                if maze[k][j]:
                    width+=1
                    length=min(length,maze[k][j])
                    smax=max(smax,width*length)
                else:
                    break
print(smax)