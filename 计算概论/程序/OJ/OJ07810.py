# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 16:00:46 2023

@author: Lenovo
"""

def check(n):
    if n%19==0:
        return "Yes"
    while n:
        if n%100==19:
            return "Yes"
        n//=10
    return "No"

n=int(input())
for i in range(n):
    print(check(int(input())))