# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 22:24:29 2023

@author: Lenovo
"""

n=int(input())
line=[0]+list(map(int,input().split()))
queue=[0]*(n+1)
for i in range(1,n+1):
    l,r=max(1,i-line[i]),min(n,i+line[i])
    queue[l]=max(queue[l],r)
right=ans=0
index=1
while right<n:
    tmpright=right
    while index<=right+1:
        tmpright=max(tmpright,queue[index])
        index+=1
    ans+=1
    right=tmpright
print(ans)