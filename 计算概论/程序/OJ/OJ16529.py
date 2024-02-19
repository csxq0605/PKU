# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 10:15:10 2023

@author: Lenovo
"""

n=int(input())
p=list(map(float,input().split()))
minp,profit=p[0],0
for price in p:
    minp=min(minp,price)
    profit=max(profit,price/minp)
print("%.2f"%(100*profit))