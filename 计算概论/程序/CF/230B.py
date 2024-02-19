# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:25:42 2023

@author: Lenovo
"""

n=1000000
ls,x,l=[True]*n,2,set()
for x in range(2,n):
    if ls[x]==True:
        l.add(x**2)
        for i in range(x**2,n,x):
            ls[i]=False
input()
for i in map(int,input().split()):
    print(["NO","YES"][i in l])