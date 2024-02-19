# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:13:45 2023

@author: Lenovo
"""

n=int(input())
x=[int(i) for i in input().split()]
y=[int(i) for i in input().split()]
del x[0]
del y[0]
for i in y:
    if i not in x:
        x.append(i)
x.sort()
if len(x)>=n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")