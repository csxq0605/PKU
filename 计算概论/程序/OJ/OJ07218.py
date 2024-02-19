# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 21:10:30 2023

@author: Lenovo
"""

import heapq
for _ in range(int(input())):
    r,c=map(int,input().split())
    martix=[["#"]*(c+2)]+[["#"]+list(input())+["#"]for i in range(r)]+[["#"]*(c+2)]
    dir=[[1,0],[-1,0],[0,1],[0,-1]]
    for i in range(1,r+1):
        for j in range(1,c+1):
            if martix[i][j]=="S":
                sx,sy=i,j
                break
    heap,flag=[],False
    heapq.heappush(heap,(0,sx,sy))
    vis=set([(sx,sy)])
    while heap:
        step,x,y=heapq.heappop(heap)
        if martix[x][y]=="E":
            flag=True
            break
        for i in range(4):
            dx,dy=x+dir[i][0],y+dir[i][1]
            if martix[dx][dy]!="#" and (dx,dy) not in vis:
                heapq.heappush(heap,(step+1,dx,dy))
                vis.add((dx,dy))
    print(step if flag else "oop!")