# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 11:03:09 2023

@author: Lenovo
"""

n=int(input())
list=[int(i) for i in input().split()]
list.sort()
for i in list:
    print(i,end=" ")