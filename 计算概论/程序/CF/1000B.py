# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:58:18 2023

@author: Lenovo
"""

n,m=map(int,input().split())
l=[0]+[int(i) for i in input().split()]+[m]
s,ans=0,[0]*(n+2)
for i in range(1,n+2):
    if s==0:
        ans[i]=ans[i-1]+l[i]-l[i-1]
        s=1
    else:
        ans[i]=ans[i-1]
        s=0
num=ans[n+1]
for i in range(1,n+2):
    if l[i]-l[i-1]>1 and i&1==0:
        num=max(num,ans[i]+m-l[i]-(ans[n+1]-ans[i])+l[i]-l[i-1]-1)
print(num)