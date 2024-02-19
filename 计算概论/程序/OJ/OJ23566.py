# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:33:37 2023

@author: Lenovo
"""

n,m=map(int,input().split())
shops,minus=[0]*(m+1),[0]*(m+1)
for _ in range(n):
    shop,value=map(int,input().split())
    shops[shop]+=value
for _ in range(1,m+1):
    minus[_]=list(map(int,input().split("-")))
ans=sum(shops)-sum(shops)//200*30
for i in range(1,m+1):
    if shops[i]>=minus[i][0]:
        ans-=minus[i][1]
print(ans)