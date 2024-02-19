# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 00:32:47 2023

@author: Lenovo
"""

def game(x):
    if x%2==0:
        print(f"{x}/2={x//2}")
        return x//2
    else:
        print(f"{x}*3+1={3*x+1}")
        return 3*x+1

n=int(input())
while n!=1:
    n=game(n)