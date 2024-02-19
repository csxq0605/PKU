# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 13:25:09 2023

@author: Lenovo
"""

n=int(input())
for i in range(n):
    l,x=map(int,input().split())
    line=[int(i)%x for i in input().split()]
    if set(line)=={0}:
        print(-1)
    elif sum(line)%x==0:
        for j in range(l):
            if line[j]!=0:
                head=j+1
                break
        for j in range(l-1,-1,-1):
            if line[j]!=0:
                back=l-j
                break
        print(l-min(head,back))
    else:
        print(l)