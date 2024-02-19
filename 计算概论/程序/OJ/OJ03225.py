# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:41:17 2023

@author: Lenovo
"""

import math
for a in range(2,101):
    for b in range(a,int(math.sqrt(10000-a**2))+1):
        for c in range(int(math.sqrt(a**2+b**2)),101):
            if a**2+b**2==c**2:
                print(f"{a}*{a} + {b}*{b} = {c}*{c}")