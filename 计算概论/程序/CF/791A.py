# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 13:50:11 2023

@author: Lenovo
"""

a,b=map(int,input().split())
num=0
while a<=b:
    a=a*3
    b=b*2
    num+=1
print(num)