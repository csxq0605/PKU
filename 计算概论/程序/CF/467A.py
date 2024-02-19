# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:09:33 2023

@author: Lenovo
"""

n=int(input())
list=[]
num=0
for i in range(n):
    list.append(input().split())
for i in range(n):
    if int(list[i][1])-int(list[i][0])>=2:
        num+=1
print(num)