# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 22:37:24 2023

@author: Lenovo
"""

n=int(input())
l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
l.sort(key=lambda x:(-x[1],x[0]))
ans1=ans2=0
for i in range(n):
    ans1+=l[i][0]
    ans2=max(ans2,ans1+l[i][1])
print(ans2)