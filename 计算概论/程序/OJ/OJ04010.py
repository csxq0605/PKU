# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:26:02 2023

@author: Lenovo
"""

num,l=1,[]
for i in range(1,501):
    num*=2011
    l.append(num%10000)
for _ in range(int(input())):
    print(l[int(input())%500-1])