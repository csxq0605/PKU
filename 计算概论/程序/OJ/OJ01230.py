# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 08:43:00 2023

@author: Lenovo
"""

for _ in range(int(input())):
    n,k=map(int,input().split())
    maze=[[0]*101 for i in range(101)]
    w=h=ans=0
    for i in range(n):
        ax,ay,bx,by=map(int,input().split())
        sx,ex=min(ax,bx),max(ax,bx)
        w=max(w,ex)
        h=max(h,by)
        for j in range(sx,ex+1):
            maze[by][j]=i+1
    for i in range(w+1):
        num=0
        for j in range(h+1):
            if maze[j][i]!=0:
                num+=1
        while num>k:
            ind,max_count=-1,0
            for j in range(h+1):
                if maze[j][i]!=0:
                    index,count=i+1,0
                    while maze[j][index]==maze[j][i]:
                        index+=1
                        count+=1
                    if count>max_count:
                        max_count=count
                        ind=j
            for l in range(i,i+max_count+1):
                maze[ind][l]=0
            num-=1
            ans+=1
    print(ans)