# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:58:20 2023

@author: Lenovo
"""

def check(x):
    l=[0]*n
    for i in range(n):
        l[i]=a[i]-x*b[i]
    l.sort(reverse=True)
    return sum(l[0:n-k])>=0

while True:
    n,k=map(int,input().split())
    if n==0 and k==0:
        break
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    left,right=0,1
    while right-left>=1/10000:
        mid=(right+left)/2
        if check(mid):
            left=mid
        else:
            right=mid
    print("%.0f"%(100*mid))