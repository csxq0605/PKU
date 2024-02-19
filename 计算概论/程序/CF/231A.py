# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 23:11:46 2023

@author: Lenovo
"""
a=0
n=int(input())
list=[]
for i in range(n):
    list.append(input())
for i in range(n):
    if int(list[i][0])+int(list[i][2])+int(list[i][4])>=2:
        a+=1
print(a)