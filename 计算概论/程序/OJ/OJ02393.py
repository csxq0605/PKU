# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 16:22:01 2023

@author: Lenovo
"""

n,s=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
money,index=l[0][0]*l[0][1],0
for i in range(1,n):
    if l[index][0]+s*(i-index)<=l[i][0]:
        money+=l[i][1]*(l[index][0]+s*(i-index))
    else:
        money+=l[i][1]*l[i][0]
        index=i
print(money)