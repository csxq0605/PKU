# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:07:18 2023

@author: Lenovo
"""

n,k,d=map(int,input().split())
mod=10**9+7
a=[1]+[0]*n
b=[1]+[0]*n
for i in range(1,n+1):
    for j in range(1,min(n,k)+1):
        a[i]=(a[i]+a[i-j])%mod
    for j in range(1,min(d,i+1)):
        b[i]=(b[i]+b[i-j])%mod
print((a[n]-b[n])%mod)