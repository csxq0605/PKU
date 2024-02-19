# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:40:42 2023

@author: Lenovo
"""

while True:
    try:
        n=int(input())
        l=list(map(int,input().split()))
        l.sort()
        maxi=l.pop()
        sumi=sum(l)
        if sumi<maxi:
            num=sumi
        else:
            num=(sumi+maxi)/2
        print("%.1f" % num)
    except:
        break