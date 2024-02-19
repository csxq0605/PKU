# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 23:37:00 2023

@author: Lenovo
"""

n,m=map(int,input().split())
martix,martix_new=[[0]*(m+2)],[["0"]*m for _ in range(n)]
l=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
for _ in range(n):
    w=[int(i) for i in input().split()]
    w.append(0)
    w.insert(0,0)
    martix.append(w)
martix.append([0]*(m+2))

for i in range(1,n+1):
    for j in range(1,m+1):
        num=0
        for _ in range(8):
            xi,yi=map(int,l[_])
            num+=martix[i+xi][j+yi]
        if martix[i][j]==0 and num==3:
            martix_new[i-1][j-1]="1"
        elif martix[i][j]==1 and 2<=num<=3:
            martix_new[i-1][j-1]="1"
for i in range(n):
    print(" ".join(martix_new[i]))