# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:00:25 2023

@author: Lenovo
"""

n=int(input())
l=[int(i) for i in input().split()]
l_max,r_max,num=[0]*(n+1),[0]*(n+1),0
for i in range(n):
    l_max[i+1]=max(l_max[i],l[i])
for i in range(n-1,-1,-1):
    r_max[i]=max(r_max[i+1],l[i])
for i in range(n):
    num+=min(l_max[i+1],r_max[i])-l[i]
print(num)