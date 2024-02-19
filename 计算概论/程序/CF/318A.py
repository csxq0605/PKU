# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:10:26 2023

@author: Lenovo
"""


n,k=map(int,input().split())
if n%2==1:    
    if k<=n//2+1:
        print(k*2-1)
    else:
        print((k-n//2-1)*2)
else:
    if k<=n//2:
        print(k*2-1)
    else:
        print((k-n//2)*2)