# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:13:33 2023

@author: Lenovo
"""

t=int(input())
for _ in range(t):
    a=input()
    l=len(a)
    f=[float("inf")]*(l+1)
    f[0]=-1
    for i in range(1,l+1):
        for j in range(1,i+1):
            if a[j-1:i]==a[j-1:i][::-1]:
                f[i]=min(f[i],f[j-1]+1)
    print(f[l])