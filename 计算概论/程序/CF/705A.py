# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 10:57:56 2023

@author: Lenovo
"""

n=int(input())
if n%2==1:
    print("I hate that I love that "*(n//2)+"I hate it")
else:
    print("I hate that I love that "*(n//2-1)+"I hate that I love it")
