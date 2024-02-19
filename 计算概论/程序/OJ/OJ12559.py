# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 23:05:40 2023

@author: Lenovo
"""
import sys
sys.setrecursionlimit(10**8)
maxi,mini="",""
def check(array):
    global maxi,mini
    while array:
        top=array[0]
        for i in array:
            if top+i<i+top:
                top=i
        maxi+=top
        mini=top+mini
        array.remove(top)
        check(array)
    return maxi+' '+mini

n=int(input())
numbs=input().split()
print(check(numbs))