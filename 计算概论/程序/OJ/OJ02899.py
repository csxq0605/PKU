# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 00:21:35 2023

@author: Lenovo
"""

martix=[list(map(int,input().split())) for _ in range(5)]
n,m=map(int,input().split())
if 0<=n<=4 and 0<=m<=4:
    martix[n],martix[m]=martix[m],martix[n]
    for i in range(5):    
        print(*martix[i])
else:
    print("error")