# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 10:45:16 2023

@author: Lenovo
"""

t=int(input())
line=list(map(int,input().split()))
line.sort()
l,r=0,len(line)-1
ans,gap=0,float("inf")
while l<r:
    mid=line[l]+line[r]
    tmpgap=abs(mid-t)
    if not tmpgap:
        ans=t
        break
    elif tmpgap<gap:
        ans=mid
        gap=tmpgap
    elif tmpgap==gap:
        ans=min(ans,mid)
    if mid>t:
        r-=1
    else:
        l+=1
print(ans)