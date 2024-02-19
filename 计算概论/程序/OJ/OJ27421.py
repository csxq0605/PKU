# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 00:04:02 2023

@author: Lenovo
"""

import heapq
m,n=map(int,input().split())
martix=[list(map(int,input().split()))for i in range(m)]
vis=[[0]*n for i in range(m)]
dir=[[-1,0],[1,0],[0,1],[0,-1]]
heap=[]
for i in range(m):
    for j in range(n):
        if i==0 or j==0 or i==m-1 or j==n-1:
            heapq.heappush(heap,(martix[i][j],i,j))
            vis[i][j]=1
ans=0
while heap:
    h,x,y=heapq.heappop(heap)
    for i in range(4):
        dx,dy=x+dir[i][0],y+dir[i][1]
        if 0<=dx<m and 0<=dy<n and not vis[dx][dy]:
            if martix[dx][dy]<h:
                ans+=h-martix[dx][dy]
            heapq.heappush(heap,(max(martix[dx][dy],h),dx,dy))
            vis[dx][dy]=1
print(ans)