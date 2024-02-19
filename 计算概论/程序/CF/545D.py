# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:06:20 2023

@author: Lenovo
"""

n=int(input())
l=[int(i) for i in input().split()]
l.sort()
num,t=0,0
for i in l:
    if i>=t:
        num+=1
        t+=i
print(num)