# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:43:00 2023

@author: Lenovo
"""

ncases=int(input())
for _ in range(ncases):
    n,m,b=map(int,input().split())
    l,initial=[],m
    for i in range(n):
        l.append(list(map(int,input().split())))
    l.sort(key=lambda x:(x[0],-x[1]))
    t=0
    for i in range(len(l)):
        if t!=l[i][0]:
            t=l[i][0]
            m=initial
        if m>0 and b>0:
            b-=l[i][1]
            m-=1
        if b<=0:
            print(t)
            break
    if b>0:
        print("alive")