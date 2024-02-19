# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 12:56:25 2023

@author: Lenovo
"""

import math

line=[]
while True:
    try:
      line.append([int(i) for i in input().split()]) 
    except EOFError:
        break
for i in line:
    a=max(i[0],i[1])
    b=min(i[0],i[1])
    x=float(a-b)
    if b==int(x*(math.sqrt(5.0)+1)/2):
        print(0)
    else:
        print(1)