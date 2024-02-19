# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 14:57:08 2023

@author: Lenovo
"""

n=int(input())
l=[int(_) for _ in input().split()]
tot,c,m,num=sum(l),0,0,0
if tot%3==0:
    for i in l[:-1]:
        c+=i
        if c==2*tot/3:
            num+=m
        if c==tot/3:
            m+=1
print(num)