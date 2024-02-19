# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:18:35 2023

@author: Lenovo
"""

n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    num=0
    if a%b!=0:
        num=b-a%b
    print(num)