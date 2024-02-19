# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 22:29:51 2023

@author: Lenovo
"""

h,l,n=map(int,input().split())
v=[l/int(i) for i in input().split()]
v.sort(reverse=True)
t=v[n//2]
s=0.5*10*t*t
ans=h-s
print("%.2f" % ans)