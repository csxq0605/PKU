# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 23:32:45 2023

@author: Lenovo
"""

n,m1,m2=map(int,input().split())
x,y,ans=[],[],[[0]*n for _ in range(n)]
for _ in range(m1):
    x.append([int(i) for i in input().split()])
for _ in range(m2):
    y.append([int(i) for i in input().split()])
y_s=sorted(y,key=lambda x:x[1])
l=pow(10,len(str(y_s[-1][1])))
for i in range(m1):
    xi=x[i]
    for j in range(m2):
        yj=y[j]
        if xi[1]==yj[0]:
            ans[xi[0]][yj[1]]+=xi[2]*yj[2]
for i in range(n):
    for j in range(n):
        if ans[i][j]!=0:
            print(i,j,ans[i][j])