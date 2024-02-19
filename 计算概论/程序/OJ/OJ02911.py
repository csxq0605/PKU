# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:31:21 2023

@author: Lenovo
"""

import math
MAX=int(input())
for a in range(32,int(math.sqrt(MAX))+1):
    for b in range(32,a):
        for k in range(1,10):
            if a**2-b**2==k*1111:
                print(a**2)