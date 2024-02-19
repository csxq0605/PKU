# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 10:33:02 2023

@author: Lenovo
"""

n=int(input())
list1=[int(i) for i in input().split()]
list2=[0]*n
for i in range(n):
    list2[list1[i]-1]+=i+1
for i in list2:
    print(i,end=" ")