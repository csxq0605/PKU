# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 23:13:45 2023

@author: Lenovo
"""

class metal:
    def __init__(self,no,n,v,contraryvalue):
        self.no=no
        self.n=n
        self.v=v
        self.contraryvalue=contraryvalue

k=int(input())
for _ in range(k):
    w=int(input())
    s=int(input())
    l=list(map(int,input().split()))
    value=0
    metals=[]
    for i in range(0,s*2,2):
        metals.append(metal(i//2+1,l[i],l[i+1],l[i+1]/l[i]))
    metals.sort(key=lambda x:x.contraryvalue)
    while w>0 and metals:
        metal_i=metals.pop()
        if w>=metal_i.n:
            value+=metal_i.v
            w-=metal_i.n
        else:
            value+=metal_i.contraryvalue*w
            w=0
    print("%.2f" % value)