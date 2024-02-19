# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:20:41 2023

@author: Lenovo
"""

n=int(input())
l=[int(i)%2 for i in input().split()]
print(l.index(sum(l)==1)+1)