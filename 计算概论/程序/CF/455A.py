# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:12:17 2023

@author: Lenovo
"""

n=int(input())
z=[0]*100001
for i in map(int,input().split()):
    z[i]+=i
a=b=0
for i in z:
    a,b=max(a,b+i),a
print(a)