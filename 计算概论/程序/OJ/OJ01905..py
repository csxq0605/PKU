# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 10:28:51 2023

@author: Lenovo
"""

import math
def check(x):
    r=(4*x*x+l*l)/8/x
    s=2*r*math.asin(l/2/r)
    return s>=l_new

while True:
    l,n,c=map(float,input().split())
    if l==-1 and n==-1 and c==-1:
        break
    l_new=round((1+n*c)*l)
    left,right,mid=0,l/2,0
    while right-left>1e-9:
        mid=(left+right)/2
        if check(mid):
            right=mid
        else:
            left=mid
    print("%.3f" % right)