# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 17:03:43 2023

@author: Lenovo
"""

def check(laptops):
    minn=laptops[0][1]
    for i in laptops[1::]:
        value,quality=map(int,i)
        if minn>quality:
            print("Happy Alex")
            return
        else:
            minn=quality
    print("Poor Alex")
    return

n=int(input())
laptops=[]
for _ in range(n):
    laptops.append([int(i) for i in input().split()])
laptops.sort(key=lambda x:x[0])
check(laptops)