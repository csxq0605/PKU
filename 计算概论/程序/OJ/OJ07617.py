# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 08:48:30 2023

@author: Lenovo
"""

n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
k=int(input())
for i in l[0:k]:    
    print(i)