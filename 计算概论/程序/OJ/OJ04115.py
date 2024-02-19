# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:13:27 2023

@author: Lenovo
"""

from collections import deque

class Node:
    def __init__(self,x,y,tools,steps):
        self.x=x
        self.y=y
        self.tools=tools
        self.steps=steps

M,N,T=map(int,input().split())
maze=[list(input()) for _ in range(M)]
visit=[[[0]*(T+1) for _ in range(N)] for _ in range(M)]
directions=[[-1,0],[1,0],[0,-1],[0,1]]
start=end=None
flag=0
for i in range(M):
    for j in range(N):
        if maze[i][j]=='@':
            start=Node(i,j,T,0)
            visit[i][j][T]=1
        if maze[i][j]=='+':
            end=(i,j)
            maze[i][j]='*'
queue=deque([start])
while queue:
    node=queue.popleft()
    if (node.x,node.y)==end:
        print(node.steps)
        flag=1
        break 
    for direction in directions:
        nx,ny=node.x+direction[0],node.y+direction[1]
        if 0<=nx<M and 0<=ny<N:
            if maze[nx][ny]=='*':
                if not visit[nx][ny][node.tools]:
                    queue.append(Node(nx,ny,node.tools,node.steps+1))
                    visit[nx][ny][node.tools]=1
            elif maze[nx][ny]=='#':
                if node.tools>0 and not visit[nx][ny][node.tools-1]:
                    queue.append(Node(nx,ny,node.tools-1,node.steps+1))
                    visit[nx][ny][node.tools-1]=1
if not flag:
    print("-1")