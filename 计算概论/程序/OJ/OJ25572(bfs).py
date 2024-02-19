# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 23:53:51 2023

@author: Lenovo
"""

from collections import deque
def bfs(start):
    d=[[-1,0],[1,0],[0,1],[0,-1]]
    queue=deque([start])
    check=set()
    check.add(start)
    while queue:
        (x0,y0),(x1,y1)=queue.popleft()
        if martix[x0][y0]==9 or martix[x1][y1]==9:
            return "yes"
        for i in range(4):
            dx0,dy0,dx1,dy1=x0+d[i][0],y0+d[i][1],x1+d[i][0],y1+d[i][1]
            if 0<=dx0<n and 0<=dy0<n and 0<=dx1<n and 0<=dy1<n and martix[dx0][dy0]!=1 and martix[dx1][dy1]!=1 and ((dx0,dy0),(dx1,dy1)) not in check:
                queue.append(((dx0,dy0),(dx1,dy1)))
                check.add(((dx0,dy0),(dx1,dy1)))
    return "no"
            
n=int(input())
martix,start=[],None
for _ in range(n):
    martix.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if martix[i][j]==5:
            if not start:
                start=(i,j)
            else:
                start=(start,(i,j))
print(bfs(start))