# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 20:58:28 2023

@author: Lenovo
"""

n=int(input())
l=list(map(int,input().split()))
num,numlist=0,[1]*n
for i in range(1,n):
    if l[i]>l[i-1]:
        numlist[i]=numlist[i-1]+1
    elif l[i]<l[i-1]:
        numlist[i-1]=numlist[i]+1
for i in range(n-2,-1,-1):
    if l[i]>l[i+1]:
        numlist[i]=max(numlist[i+1]+1,numlist[i])
    elif l[i]<l[i+1]:
        numlist[i+1]=max(numlist[i]+1,numlist[i+1])
for i in range(n):
    num+=numlist[i]
print(num)