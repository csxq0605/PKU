# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:20:26 2023

@author: Lenovo
"""

n=int(input())
line=[int(i) for i in input().split()]
num=1
tem=1
for i in range(n-1):
    if line[i]<=line[i+1]:
       tem+=1
    else:
        num=max(num,tem)
        tem=1
print(max(num,tem))