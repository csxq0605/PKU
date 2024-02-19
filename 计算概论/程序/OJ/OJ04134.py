# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 08:27:23 2023

@author: Lenovo
"""

def check(num):
    left,right=0,n-1
    if l[right]<=num:
        return l[right]
    elif l[left]>=num:
        return l[left]
    while right>left+1:
        mid=(right+left)//2
        if l[mid]>num:
            right=mid
        elif l[mid]<num:
            left=mid
        else:
            return l[mid]
    if (l[right]-num)>=(num-l[left]):
        return l[left]
    else:
        return l[right]

n=int(input())
l=[int(i) for i in input().split()]
m=int(input())
for _ in range(m):
    num=int(input())
    print(check(num))