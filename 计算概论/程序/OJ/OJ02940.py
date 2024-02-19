# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 00:19:30 2023

@author: Lenovo
"""

a,n=map(int,input().split())
l=[0,1,11,111,1111,11111,111111,1111111,11111111,111111111]
ans=0
for i in range(1,n+1):
    ans+=a*l[i]
print(ans)