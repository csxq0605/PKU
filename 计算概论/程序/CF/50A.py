# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 11:58:38 2023

@author: Lenovo
"""

n,m=map(int,input().split())
if n%2==0:
    l=n//2
    print(l*m)
else:
    l=n//2
    w=m//2
    print(l*m+w)