# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 14:39:32 2023

@author: Lenovo
"""

from math import sqrt
n=int(input())
if n<6 or n%2==1:
    print("Error!")
else:
    l,a,b=[True]*(n+1),2,int(sqrt(n))+1
    while a<b:
        if l[a]==True:
            for i in range(a*2,n+1,a):
                l[i]=False
        a+=1
    l=[i for i in range(2,n+1) if l[i]==True]
    for y in range(len(l)):
        for z in range(y,len(l)):
            if l[y]+l[z]==n:
                print(f"{n}={l[y]}+{l[z]}")