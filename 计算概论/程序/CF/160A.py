# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:09:59 2023

@author: Lenovo
"""

n=int(input())
list=[int(i) for i in input().split()]
list.sort(reverse=True)
num=0
total=sum(list)
mine=float(0)
while mine<=total/2:
    mine+=list[num]
    num+=1
print(num)