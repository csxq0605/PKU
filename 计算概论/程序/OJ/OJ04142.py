# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:42:49 2023

@author: Lenovo
"""

def check(x):
    s=x*x*x*x*x-15*x*x*x*x+85*x*x*x-225*x*x+274*x-121
    return s

left,right=1.5,2.4
while right-left>=1e-7:
    mid=(left+right)/2
    if check(mid)>0:
        left=mid
    elif check(mid)<0:
        right=mid
    else:
        break
print("%.6f" % mid)