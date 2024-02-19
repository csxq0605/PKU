# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:39:24 2023

@author: Lenovo
"""

from collections import defaultdict
n=int(input())
line=[0]+list(map(int,input().split()))
l,summ,ans=[0]*(n+1),0,0
check=defaultdict(int)
result=defaultdict(int)
for i in range(n+1):
    summ+=line[i]
    l[i]=summ-520*i
for i in range(n+1):
    x=l[i]
    if check[x]:
        ans=max(ans,i-result[x])
    else:
        check[x]=True
        result[x]=i
print(ans*520)