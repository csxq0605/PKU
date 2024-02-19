# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 11:31:55 2023

@author: Lenovo
"""
n,m,a=map(int,input().split())
if n%a==0:
    N=int(n/a)
else:
    N=n//a+1
if m%a==0:
    M=int(m/a)
else:
    M=m//a+1
print(N*M)