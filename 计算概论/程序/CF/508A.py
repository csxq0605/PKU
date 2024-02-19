# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 21:45:31 2023

@author: Lenovo
"""

n,m,k=map(int,input().split())
l,a,flag=[],0,True
martix=[[0]*(m+2) for _ in range(n+2)]
for i in range(k):
    w=[int(_) for _ in input().split()]
    l.append(w)
while flag and a<k:
    x,y=map(int,l[a])
    a+=1
    martix[x][y]=1
    if martix[x][y]+martix[x-1][y]+martix[x-1][y-1]+martix[x][y-1]==4:
        flag=False
    elif martix[x][y]+martix[x+1][y]+martix[x+1][y-1]+martix[x][y-1]==4:
        flag=False
    elif martix[x][y]+martix[x-1][y]+martix[x-1][y+1]+martix[x][y+1]==4:
        flag=False
    elif martix[x][y]+martix[x+1][y]+martix[x+1][y+1]+martix[x][y+1]==4:
        flag=False
if flag:
    print(0)
else:
    print(a)