# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 22:47:01 2023

@author: Lenovo
"""

n=int(input())
list=[]
for i in range(n):
    list.append(input())
for j in range(len(list)):
    if len(list[j])<=10:
        print(list[j])
    else:
        print(list[j][0]+str(len(list[j])-2)+list[j][len(list[j])-1])