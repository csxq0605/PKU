# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:34:50 2023

@author: Lenovo
"""

l=[[[] for i in range(32)]for _ in range(13)]
n=int(input())
for i in range(n):
    num,month,day=input().split()
    l[int(month)][int(day)].append(num)
for i in range(1,13):
    for j in range(1,32):
        if len(l[i][j])>=2:
            print(i,j,*l[i][j])