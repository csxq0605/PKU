# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:23:28 2023

@author: Lenovo
"""

m,n=map(int,input().split())
martix=[]
for _ in range(m):
    martix.append([int(i) for i in input().split()])
x,y=map(int,input().split())
martix[x-1],martix[y-1]=martix[y-1],martix[x-1]
ans=sum(martix[0])+sum(martix[m-1])
for i in range(1,m-1):
    ans+=martix[i][0]+martix[i][n-1]
print(ans)