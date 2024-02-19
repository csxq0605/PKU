# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 22:32:09 2023

@author: Lenovo
"""

n=int(input())
for i in range(6,n+1):
    if i>=6 and n%i==0:
        print(n//i)
        break