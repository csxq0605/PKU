# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:41:55 2023

@author: Lenovo
"""

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
l.append(0)
num,flag=0,1
for i in range(n):
    if l[i]>l[i+1] and flag==1:
        flag=0
        num+=l[i]
    elif l[i]<l[i+1] and flag==0:
        flag=1
        num-=l[i]
print(num)