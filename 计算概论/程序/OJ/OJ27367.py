# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 11:02:20 2023

@author: Lenovo
"""

n,m=map(int,input().split())
res=[]
for i in range(n):
    l=list(map(int,input().split()))
    t=im=0
    for j in range(1,m+1):
        if l[j]>=90:
            t+=1
        if l[j]>l[j-1] and j!=1:
            im+=l[j]-l[j-1]
    res.append([t,im,l[0]])
res.sort(key=lambda x:(-x[0],-x[1],x[2]))
for i in range(n):
    print(res[i][2])