# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 16:25:57 2023

@author: Lenovo
"""

import math
while True:
    n=int(input())
    if n==0:
        break
    l=[]
    for i in range(n):
        v,t=map(int,input().split())
        if t<0:
            continue
        l.append(math.ceil(4.5/v*3600+t))
    l.sort()
    print(l[0])