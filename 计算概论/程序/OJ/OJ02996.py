# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:00:56 2023

@author: Lenovo
"""

def nextper(a):
    size=len(a)
    flag=size-1
    while flag!=0 and a[flag-1]>a[flag]:
        flag-=1
    if flag==0:
        a.sort()
        return
    for i in range(size-1,flag-1,-1):
        if a[i]>a[flag - 1]:
            a[i],a[flag - 1]=a[flag-1],a[i]
            break
    a[flag:]=a[flag:][::-1]

n=int(input())
k=int(input())
a=[int(i) for i in input().split()]
for _ in range(k):
    nextper(a)
print(' '.join(map(str,a)))