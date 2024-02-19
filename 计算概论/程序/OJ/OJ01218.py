# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:29:06 2023

@author: Lenovo
"""

n=int(input())
for i in range(n):
    cell=int(input())
    prison=[0]*cell
    for j in range(cell):
        for _ in range(cell):
            if (_+1)%(j+1)==0:
                prison[_]=(prison[_]+1)%2
    print(sum(prison))