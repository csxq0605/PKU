# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 18:37:29 2023

@author: Lenovo
"""

n,m=map(int,input().split())
f=[0]*(n+1)
f[0]=1
for i in range(1,m):
    f[i]=f[i-1]*2
f[m]=f[m-1]*2-1
for i in range(m+1,n+1):
    f[i]=f[i-1]*2-f[i-m-1]
print(f[n])