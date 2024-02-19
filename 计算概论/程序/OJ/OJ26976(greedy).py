# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 10:28:17 2023

@author: Lenovo
"""

n=int(input())
l=list(map(int,input().split()))
if n<=1:
    print(1)
else:    
    preDiff=0 
    curDiff=0 
    result=1 
    for i in range(n-1):
        curDiff=l[i+1]-l[i]
        if (preDiff>=0 and curDiff<0) or (preDiff<=0 and curDiff>0):
            result+=1
            preDiff=curDiff
    print(result)