# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:25:04 2023

@author: Lenovo
"""

n,m=map(int,input().split())
for i in range(n):
    if i%4==0 or i%4==2:
        print("#"*m)
    elif i%4==1:
        print("."*(m-1)+"#")
    else:
        print("#"+"."*(m-1))