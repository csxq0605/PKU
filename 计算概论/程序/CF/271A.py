# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 21:10:56 2023

@author: Lenovo
"""
def j(n):
    l = [c for c in str(n)]
    l_s = set(l)
    if len(l) == len(l_s):
        return 1
    return 0

n = int(input())
while n:
    n += 1
    if j(n):
        break

print(n)