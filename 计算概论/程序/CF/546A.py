# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:41:26 2023

@author: Lenovo
"""

k,n,w=map(int,input().split())
m=(w*(w+1)//2)*k
if m>n:
    print(m-n)
else:
    print(0)