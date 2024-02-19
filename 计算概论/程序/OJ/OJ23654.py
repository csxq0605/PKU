# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:34:02 2023

@author: Lenovo
"""

def j(n):
    l = [int(c) for c in str(n)]
    if sum(l)==20:
        return 1
    return 0
 
n = int(input())
while n:
    n += 1
    if j(n):
        break
 
print(n)