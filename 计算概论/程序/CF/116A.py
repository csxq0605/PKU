# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:07:48 2023

@author: Lenovo
"""

n=int(input())
num=0
num_a=0
for i in range(n):
    line=input().split()
    num_a=num_a+int(line[1])-int(line[0])
    if num>=num_a:
        num=num
    else:
        num=num_a
print(num)