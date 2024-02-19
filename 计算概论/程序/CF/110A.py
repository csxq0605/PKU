# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:06:36 2023

@author: Lenovo
"""

n=input()
num=0
for i in range(len(n)):
    if n[i]=="4"or n[i]=="7":
        num+=1
if num==4 or num==7:
    print("YES")
else:
    print("NO")