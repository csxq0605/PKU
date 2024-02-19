# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:01:26 2023

@author: Lenovo
"""

n,k=map(int,input().split())
for i in range(k):
    if n%10==0:
        n=int(n/10)
    else:
        n=n-1
print(n)