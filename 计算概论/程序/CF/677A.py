# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:08:25 2023

@author: Lenovo
"""

n,h=map(int,input().split())
w=0
a=input().split()
for i in range(n):
    if int(a[i])>h:
        w+=2
    else:
        w+=1
print(w)