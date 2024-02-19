# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 10:40:54 2023

@author: Lenovo
"""

n=int(input())
f=0
if n%2==0:
    f+=n//2
else:
    f=f+n//2-n
print(f)