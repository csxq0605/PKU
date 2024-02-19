# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:07:17 2023

@author: Lenovo
"""
x=0
n=int(input())
for i in range(n):
    operation=input()
    if operation[0]=="X":
        if operation[1:3]=="++":
            x+=1
        else:
            x-=1
    else:
        if operation[0:2]=="++":
            x+=1
        else:
            x-=1
print(x)