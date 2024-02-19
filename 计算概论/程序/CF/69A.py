# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:05:13 2023

@author: Lenovo
"""

n=int(input())
list=[]
numx,numy,numz=0,0,0
for i in range(n):
    quene=input().split()
    list.append(quene)
for i in range(n):
    numx+=int(list[i][0])
for i in range(n):
    numy+=int(list[i][1])
for i in range(n):
    numz+=int(list[i][2])
if numx==0 and numy==0 and numz==0:
    print("YES")
else:
    print("NO")