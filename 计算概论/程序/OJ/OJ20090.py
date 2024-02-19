# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 17:05:54 2023

@author: Lenovo
"""

ans=[7,1,3,9]
for _ in range(int(input())):
    n=int(input())
    if n==1:
        print(1)
    else:
        print(ans[n%4-2])