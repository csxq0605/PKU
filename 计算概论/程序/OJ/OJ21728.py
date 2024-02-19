# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 09:41:18 2023

@author: Lenovo
"""

n=int(input())
t=[0]+list(map(int,input().split()))
ind=[0]+list(map(int,input().split()))
ans=0
for i in range(1,n+1):
    ans+=t[ind[i]]*(n-i)
print("%.2f"%(ans/n))