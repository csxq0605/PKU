# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:20:59 2023

@author: Lenovo
"""

n=int(input())
for i in range(n):
    l,num=map(int,input().split())
    position=[int(i) for i in input().split()]
    sum_max,sum_min=0,0
    for i in position:    
        sum_max=max(sum_max,max(l-i,i))
        sum_min=max(sum_min,min(l-i,i))
    print(f'{sum_min} {sum_max}')