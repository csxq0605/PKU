# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 11:08:58 2023

@author: Lenovo
"""

n=int(input())
total=0.0
list=[float(i) for i in input().split()]
for i in list:
    total+=i
print(round(total/(n*100),14)*100)