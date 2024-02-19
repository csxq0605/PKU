# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:29:03 2023

@author: Lenovo
"""

n,b=map(int,input().split())
l,num,h,i=[],0,0,0
for _ in range(n):
    l.append(int(input()))
l.sort(reverse=True)
while h<b:
    h+=l[i]
    num+=1
    i+=1
print(num)