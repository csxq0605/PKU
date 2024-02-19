# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 11:30:18 2023

@author: Lenovo
"""

def solve():
    res = 0
    cd = []
    for i in range(n):
        for j in range(n):
            cd.append(c[i] + d[j])
    cd.sort()
    for i in range(n):
        for j in range(n):
            ab = -(a[i] + b[j])
            res += upper_bound(cd, ab) - lower_bound(cd, ab)
    print(res)

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2  
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

def lower_bound(arr, target):
    left, right = 0, len(arr)    
    while left < right:
        mid = (left + right) // 2        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid    
    return left

n = int(input())
a,b,c,d=[],[],[],[]
for i in range(n):
    ai,bi,ci,di=map(int,input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)
    d.append(di)
solve()