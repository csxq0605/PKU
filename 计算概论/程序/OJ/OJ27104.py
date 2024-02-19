# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:20:22 2023

@author: Lenovo
"""

n=int(input())
a=list(map(int,input().split()))
intervals=[(max(0,i-a[i]),min(n-1,i+a[i])) for i in range(n)]
intervals.sort()
ans,right,temp,i=0,0,0,0
while i<n and right<n:
    while i<n and intervals[i][0]<=right:
        temp=max(temp,intervals[i][1])
        i+=1
    right=temp+1
    ans+=1
print(ans)