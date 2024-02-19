# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:08:43 2023

@author: Lenovo
"""

n,t=map(int,input().split())
line=input()
ln=""
list=[i for i in line]
for i in range(t):
    p=[]
    for j in range(n-1):
        if list[j]=="B" and list[j+1]=="G":
            p.append(j)
    for k in p:
        list[k],list[k+1]=list[k+1],list[k]
for i in range(n):
    ln+=list[i]
print(ln)