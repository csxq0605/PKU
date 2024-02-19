# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:21:14 2023

@author: Lenovo
"""

martix=[]
for i in range(5):
    list=[int(x) for x in input().split()]
    martix.append(list)
for i in range(5):
    for j in range(5):
        if martix[i][j]==1:
            l,w=i+1,j+1
            break
print(abs(l-3)+abs(w-3))