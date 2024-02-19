# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:58:26 2023

@author: Lenovo
"""

def count(x,y):
    ans=0
    dir=[[1,0],[-1,0],[0,1],[0,-1]]
    for i in range(4):
        dx,dy=x+dir[i][0],y+dir[i][1]
        if not martix[dx][dy]:
            ans+=1
    return ans
n,m=map(int,input().split())
martix,ans=[[0]*(m+2),[0]*(m+2)],0
for i in range(1,n+1):
    martix.insert(i,[0]+list(map(int,input().split()))+[0])
for i in range(1,n+1):
    for j in range(1,m+1):
        if martix[i][j]:
            ans+=count(i,j)
print(ans)