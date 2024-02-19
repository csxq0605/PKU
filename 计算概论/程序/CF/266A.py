# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 13:46:05 2023

@author: Lenovo
"""

num=0
stones=int(input())
line=input()
for i in range(stones-1):
    if line[i]==line[i+1]:
        num+=1
print(num)
