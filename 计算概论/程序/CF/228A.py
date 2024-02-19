# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 10:38:31 2023

@author: Lenovo
"""

list=[int(i) for i in input().split()]
num=[]
for i in list:
    if i not in num:
        num.append(i)
print(4-len(num))
