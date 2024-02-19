# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 18:16:11 2023

@author: Lenovo
"""

n=int(input())
a,b,c=1,1,1
for i in range(n-1):
    d=a+b+c
    b=b+a
    c=c+a
    a=d
print(a+b+c)