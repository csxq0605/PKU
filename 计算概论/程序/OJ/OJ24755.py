# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 18:46:36 2023

@author: Lenovo
"""

n=int(input())
def f(n):
    num=0
    if n==0 or n==1:
        return 1
    else:
        for i in range(n):
            num+=f(i)*f(n-1-i)
        return num
print(f(n))