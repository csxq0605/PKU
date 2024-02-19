# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:37:41 2023

@author: Lenovo
"""

t = int(input())
for _ in range(t):
    a, n = input().split()
    n = int(n)
    a = list(a)
    for _ in range(n):
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                del a[i]
                break
        else:
            a.pop()
    print(''.join(a))