# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 01:08:28 2023

@author: Lenovo
"""

import sys
sys.setrecursionlimit(1<<30)
d=[(-1,0),(1,0),(0,1),(0,-1)]
flag=0
def dfs(body):
    global flag
    if end in body:
        flag=1
        return
    for i in range(4):
        dx0,dy0,dx1,dy1=body[0][0]+d[i][0],body[0][1]+d[i][1],body[1][0]+d[i][0],body[1][1]+d[i][1]
        if 0<=dx0<n and 0<=dy0<n and 0<=dx1<n and 0<=dy1<n and martix[dx0][dy0]!=1 and martix[dx1][dy1]!=1 and (check[dx0][dy0] or check[dx1][dy1]):
            check[dx0][dy0]=check[dx1][dy1]=False
            dfs([[dx0,dy0],[dx1,dy1]])
            check[dx0][dy0]=check[dx1][dy1]=True
            check[body[0][0]][body[0][1]]=check[body[1][0]][body[1][1]]=False
    return
            
n=int(input())
martix,body,check=[],[],[[True]*n for _ in range(n)]
for _ in range(n):
    martix.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if martix[i][j]==9:
            end=[i,j]
        elif martix[i][j]==5:
            body.append([i,j])
            check[i][j]=False
dfs(body)
print("yes" if flag else "no")