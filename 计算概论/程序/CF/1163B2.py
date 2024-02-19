# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 16:17:13 2023

@author: Lenovo
"""

a,b=[0]*100001,[0]*100001
n=int(input())
ans=i=1
for num in map(int,input().split()):
    a[num]+=1
    b[a[num]]+=1
    if a[num]*b[a[num]]==i and i!=n:
        ans=i+1
    elif a[num]*b[a[num]]==i-1:
        ans=i
    i+=1
print(ans)