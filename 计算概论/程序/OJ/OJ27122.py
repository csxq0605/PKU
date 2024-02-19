# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 23:54:32 2023

@author: Lenovo
"""

def check(x):
    count=1
    pre=position[0]
    i=1
    while i<n:
        if position[i]>=pre+x:
            count+=1
            pre=position[i]
        i+=1
    return count>=m

n,m=map(int,input().split())
position=list(map(int,input().split()))
position.sort()
left=1
right=(position[-1]-position[0])//(m-1)
while left<right:
    mid=left+(right-left+1)//2
    if check(mid):
        left=mid
    else:
        right=mid-1
print(left)