# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:00:47 2023

@author: Lenovo
"""

n=int(input())
for a in range(2,n+1):
    for b in range(2,int(pow(a**3/3,1/3))+1):
        for c in range(b,int(pow(a**3/2,1/3)+1)):
            for d in range(c,a):
                if a**3==b**3+c**3+d**3:
                    print(f'Cube = {a}, Triple = ({b},{c},{d})')    