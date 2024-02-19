# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 00:26:59 2023

@author: Lenovo
"""

l=list(input())
tmp=""
for i in range(len(l)):
    if ord("0")<=ord(l[i])<=ord("9"):
        tmp+=l[i]
    else:
        if tmp!="":
            print(int(tmp))
        tmp=""
if tmp!="":
    print(int(tmp))