# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:23:49 2023

@author: Lenovo
"""

n=int(input())
for i in range(n):
    num=int(input())
    if num==0:
        print(0)
    else:
        print((num+1)//2-1)