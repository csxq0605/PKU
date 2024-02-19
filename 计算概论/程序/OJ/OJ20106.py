# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 10:48:27 2023

@author: Lenovo
"""

import heapq
m,n,p=map(int,input().split())
martix=[list(input().split())for i in range(m)]
dir=[(-1,0),(1,0),(0,1),(0,-1)]
for _ in range(p):
    sx,sy,ex,ey=map(int,input().split())
    if martix[sx][sy]=="#" or martix[ex][ey]=="#":
        print("NO")
        continue
    vis,heap,ans=set(),[],[]
    heapq.heappush(heap,(0,sx,sy))
    vis.add((sx,sy,-1))
    while heap:
        tire,x,y=heapq.heappop(heap)
        if x==ex and y==ey:
            ans.append(tire)
        for i in range(4):
            dx,dy=dir[i]
            x1,y1=dx+x,dy+y
            if 0<=x1<m and 0<=y1<n and martix[x1][y1]!="#" and (x1,y1,i) not in vis:
                t1=tire+abs(int(martix[x][y])-int(martix[x1][y1]))
                heapq.heappush(heap,(t1,x1,y1))
                vis.add((x1,y1,i))
    print(min(ans) if ans else "NO")