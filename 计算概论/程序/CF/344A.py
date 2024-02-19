# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 23:14:09 2023

@author: Lenovo
"""
n=int(input())
list=[]
num=1
for i in range(n):
    list.append(input())
for i in range(n-1):
    if list[i][1]==list[i+1][0]:
        num+=1
print(num)