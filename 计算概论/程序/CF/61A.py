# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:21:55 2023

@author: Lenovo
"""

num1=input()
num2=input()
num=[]
for i in range(len(num1)):
    if num1[i]==num2[i]:
        num.append(0)
    else:
        num.append(1)
for i in num:
    print(i,end="")