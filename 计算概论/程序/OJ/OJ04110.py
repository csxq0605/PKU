# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 23:58:15 2023

@author: Lenovo
"""

class metal:
    def __init__(self,v,n,contraryvalue):
        self.n=n
        self.v=v
        self.contraryvalue=contraryvalue

n,w=map(int,input().split())
value=0
metals=[]
for i in range(n):
    l=[int(i) for i in input().split()]
    metals.append(metal(l[0],l[1],l[0]/l[1]))
metals.sort(key=lambda x:x.contraryvalue)
while w>0 and metals:
    metal_i=metals.pop()
    if w>=metal_i.n:
        value+=metal_i.v
        w-=metal_i.n
    else:
        value+=metal_i.contraryvalue*w
        w=0
print("%.1f" % value)